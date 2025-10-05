import dotenv, asyncio
import streamlit as st
from agents import Agent, Runner, SQLiteSession, WebSearchTool

dotenv.load_dotenv()

if "agent" not in st.session_state:
    st.session_state["agent"] = Agent(
        name="Chat GPT Clone",
        instructions="""
        You are a helpful assistant.
        
        You have access to the following tools:
            - Web Search Tool: User this when the user asks a questions that isn't in your training data. 
            Use this tool when the users asks about current or future events,
            when you think you don't know the answer, try searching for it in the web first

        """,
        tools=[
            WebSearchTool()
        ]
    )
agent = st.session_state["agent"]

if "session" not in st.session_state:
    st.session_state["session"] = SQLiteSession(
        "chat-history",
        "cht-gpt-clone-memory.db"
    )

session = st.session_state["session"]

async def paint_histroy():
    messages = await session.get_items()

    for message in messages:
        if "role" in message:
            with st.chat_message(message["role"]):
                if message["role"] == "user":
                    st.write(message["content"])
                else:
                    if message["type"] == "message":
                      st.write(message["content"][0]["text"])

asyncio.run(paint_histroy())


async def run_agent(message):
    with st.chat_message("ai"):
        text_placeholder = st.empty()
        stream = Runner.run_streamed(
            agent,
            message,
            session=session,
        )
        response = ""
        async for event in stream.stream_events():
            if event.type == "raw_response_event":
                if event.data.type == ("response.web_search_call.in_progress" or "response.web_search_call.searching"):
                    text_placeholder.status("🔎 Web Searching ... ", state="running")
                elif event.data.type == "response.content_part.added":
                    text_placeholder.empty()
                elif event.data.type == "response.created":
                    text_placeholder.status("🏃‍➡️ Start Response ... ", state="running")
                elif event.data.type == "response.output_text.delta":
                    response += event.data.delta
                    text_placeholder.write(response)

prompt = st.chat_input("Write a message for your assistant")


if prompt:
    with st.chat_message("human"):
        st.write(prompt)
    asyncio.run(run_agent(prompt))


with st.sidebar:
    reset = st.button("Reset Memory")
    if reset:
        asyncio.run(session.clear_session())
    st.write(asyncio.run(session.get_items()))
