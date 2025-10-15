from typing import Literal

from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from pydantic import BaseModel


class SupervisorOutput(BaseModel):
    next_agent: Literal["korean_agent", "greek_agent", "spanish_agent", "__end__"]
    reasoning: str


class AgentsState(MessagesState):
    current_agent: str
    transfered_by: str
    reasoning: str
    error: str


llm = init_chat_model("openai:gpt-4o")


def make_agent(prompt, tools):
    def agent_node(state: AgentsState):
        llm_with_tools = llm.bind_tools(tools)
        response = llm_with_tools.invoke(
            f"""
            {prompt}

            Conversation History:
            {state["messages"]}
            """
        )
        return {"messages": [response]}

    agent_builder = StateGraph(AgentsState)

    (
        agent_builder
        .add_node("agent", agent_node)
        .add_node("tools", ToolNode(tools=tools))

        .add_edge(START, "agent")
        .add_conditional_edges("agent", tools_condition)
        .add_edge("tools", "agent")
        .add_edge("agent", END)
    )
    return agent_builder.compile()


def supervisor(state: AgentsState):
    structured_llm = llm.with_structured_output(SupervisorOutput)
    response = structured_llm.invoke(
        f"""
            You are a supervisor that routes conversations to the appropriate language agent.
            Analyse the customers request and the conversation history and decide which agent should handle the conversation.
            The options for the next agent are:
            - greek_agent
            - spanish_agent
            - korean_agent      

            <CONVERSATION_HISTORY>
            {state.get("messages", [])}
            </CONVERSATION_HISTORY>

            IMPORTANT:
            Never transfer to the same agent twice in a row.
            If an agent has replied end the conversation by returning __end__
        """
    )

    return Command(
        goto=response.next_agent,
        update={"reasoning": response.reasoning},
    )


@tool
def handoff_tool(transfer_to: str, transfered_by: str):
    """
     Handoff to another agent.

     Use this tool when the customer speaks a language that you don't understand.

     Possible values for `transfer_to`:
     - `korean_agent`
     - `greek_agent`
     - `spanish_agent`

     Possible values for `transfered_by`:
     - `korean_agent`
     - `greek_agent`
     - `spanish_agent`

     Args:
         transfer_to: The agent to transfer the conversation to
         transfered_by: The agent that transferred the conversation
     """

    if transfer_to == transfered_by:
        return {
            "error": " Stop trying to transfer to your self"
        }
    return Command(
        update={
            "current_agent": transfer_to,
            "transfered_by": transfered_by,
        },
        goto=transfer_to,
        graph=Command.PARENT
    )


graph_builder = StateGraph(AgentsState)

(
    graph_builder
    .add_node("supervisor", supervisor, destinations={"korean_agent", "greek_agent", "spanish_agent", END})
    .add_edge(START, "supervisor")

    .add_node("korean_agent", make_agent(
        prompt="You're a Korean customer support agent. You only speak and understand Korean.",
        tools=[]))

    .add_node("greek_agent", make_agent(
        prompt="You're a Greek customer support agent. You only speak and understand Greek.",
        tools=[]))

    .add_node("spanish_agent", make_agent(
        prompt="You're a Spanish customer support agent. You only speak and understand Spanish.",
        tools=[]))

    .add_edge(START, "supervisor")
    .add_edge("korean_agent", "supervisor")
    .add_edge("greek_agent", "supervisor")
    .add_edge("spanish_agent", "supervisor")
)

graph = graph_builder.compile()
