from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

MODEL = "openai:gpt-5"

history_agent = create_react_agent(
    model=MODEL,
    tools=[],
    name="history_agent",
    prompt="You are a history expert. You only answer questions about history.",
)
geography_agent = create_react_agent(
    model=MODEL,
    tools=[],
    name="geography_agent",
    prompt="You are a geography expert. You only answer questions about geography.",
)
maths_agent = create_react_agent(
    model=MODEL,
    tools=[],
    name="maths_agent",
    prompt="You are a maths expert. You only answer questions about maths.",
)
philosophy_agent = create_react_agent(
    model=MODEL,
    tools=[],
    name="philosophy_agent",
    prompt="You are a philosophy expert. You only answer questions about philosophy.",
)


supervisor = create_supervisor(
    agents=[
        history_agent,
        maths_agent,
        geography_agent,
        philosophy_agent,
    ],
    model=init_chat_model(MODEL),
    prompt="""
    You are a supervisor that routes student questions to the appropriate subject expert. 
    You manage a history agent, geography agent, maths agent, and philosophy agent. 
    Analyze the student's question and assign it to the correct expert based on the subject matter:
        - history_agent: For historical events, dates, historical figures
        - geography_agent: For locations, rivers, mountains, countries
        - maths_agent: For mathematics, calculations, algebra, geometry
        - philosophy_agent: For philosophical concepts, ethics, logic
    """,
).compile()