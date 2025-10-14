import pytest
from langgraph.types import interrupt

from main import graph

config = {
    "configurable": {
        "thread_id": "1"
    }
}


@pytest.mark.parametrize(
    "email, expected_category, expected_score",
    [
        ("this is urgent!", "urgent", 10),
        ("i wanna talk to you", "normal", 5),
        ("i have an offer for you", "spam", 1),
    ]
)
def test_full_graph(email, expected_category, expected_score):
    result = graph.invoke(
        {"email": email},
        config=config
    )

    assert result["category"] == expected_category
    assert result["priority_score"] == expected_score


def test_individual_nodes():


    result = graph.nodes["categorize_email"].invoke({"email": "check out this offer"})
    assert result["category"] == "spam"

    result = graph.nodes["assing_priority"].invoke({"category": "spam"})
    assert result["priority_score"] == 1

    result = graph.nodes["draft_response"].invoke({"category": "spam"})
    assert "Go away" in result["response"]




def test_partial_excution():

    graph.update_state(
        config=config,
        values={
            "email" : "please check out this offer",
            "category" : "spam",
        },
        as_node="categorize_email"
    )

    result = graph.invoke(
        None,
        config=config,
        interrupt_after="draft_response"
    )

    assert result["priority_score"] == 1






# uv run pytest test.py -vv
