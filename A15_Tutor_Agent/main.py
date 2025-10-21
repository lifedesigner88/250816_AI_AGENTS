from langgraph.graph import START, END, StateGraph, MessagesState
from agents.classification_agent import classification_agent
from agents.feynman_agent import feynman_agent
from agents.teacher_agent import teacher_agent
from agents.quiz_agent import quiz_agent
from dotenv import load_dotenv

load_dotenv()


class TutorState(MessagesState):
    current_agent: str


graph_builder = StateGraph(TutorState)


def route_check(state: TutorState):
    current_agent = state.get("current_agent", "classification_agent")
    return current_agent

(
    graph_builder
    .add_node(
        "classification_agent",
        classification_agent,
        destinations=(
            "teacher_agent",
            "feynman_agent",
            "quiz_agent"
        ))

    .add_node("quiz_agent", quiz_agent)
    .add_node("feynman_agent", feynman_agent)
    .add_node("teacher_agent", teacher_agent)

    .add_conditional_edges(START, route_check, [
        "quiz_agent",
        "teacher_agent",
        "feynman_agent",
        "classification_agent",
    ])

    .add_edge("classification_agent", END)
)

graph = graph_builder.compile()
