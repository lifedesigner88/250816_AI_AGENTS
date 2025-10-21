from langgraph.graph import START, END, StateGraph, MessagesState
from agents.classification_agent import classification_agent
from dotenv import load_dotenv

load_dotenv()


class TutorState(MessagesState):
    pass


graph_builder = StateGraph(TutorState)

(
    graph_builder
    .add_node("classification_agent", classification_agent)
    .add_edge(START, "classification_agent")
    .add_edge("classification_agent", END)
)

graph = graph_builder.compile()
