import dotenv

dotenv.load_dotenv()

import asyncio

import streamlit as st
from agents import Runner, SQLiteSession, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from models import UserAccountContext
from my_agents.triage_agent import triage_agent

user_account_ctx = UserAccountContext(
    customer_id=1,
    name="nico",
    tier="basic"
)

if "session" not in st.session_state:
    st.session_state["session"] = SQLiteSession(
        "chat-history",
        "customer-support-memory.db",
    )
session = st.session_state["session"]

if "agent" not in st.session_state:
    st.session_state["agent"] = triage_agent

async def paint_history():
    session_messages = await session.get_items()
    for m in session_messages:
        if "role" in m:
            with st.chat_message(m["role"]):
                if m["role"] == "user":
                    st.write(m["content"])
                else:
                    if m["type"] == "message":
                        st.write(m["content"][0]["text"].replace("$", r"\$"))


asyncio.run(paint_history())


async def run_agent(user_message):
    with st.chat_message("ai"):
        text_placeholder = st.empty()
        response = ""
        st.session_state["text_placeholder"] = text_placeholder
        try:
            stream = Runner.run_streamed(
                st.session_state["agent"],
                user_message,
                session=session,
                context=user_account_ctx,
            )

            async for event in stream.stream_events():
                if event.type == "raw_response_event":
                    if event.data.type == "response.output_text.delta":
                        response += event.data.delta
                        text_placeholder.write(response.replace("$", r"\$"))

                elif event.type == "agent_updated_stream_event":
                    if st.session_state["agent"].name != event.new_agent.name:
                        st.session_state["agent"] = event.new_agent

                        st.write(f"🤖 Transfered from {st.session_state["agent"].name} to {event.new_agent.name}")

                        text_placeholder = st.empty() # 새로운 텍스트 홀더 생성
                        st.session_state["text_placeholder"] = text_placeholder
                        response = ""

        except InputGuardrailTripwireTriggered:
            st.write("I can't help you with that.")

        except OutputGuardrailTripwireTriggered:
            st.write("Cant show you that answer.")
            st.session_state["text_placeholder"].empty()


message = st.chat_input(
    "Write a message for your assistant",
)

if message:

    if "text_placeholder" in st.session_state:
        st.session_state["text_placeholder"].empty()

    if message:
        with st.chat_message("human"):
            st.write(message)
        asyncio.run(run_agent(message))

with st.sidebar:
    reset = st.button("Reset memory")
    if reset:
        asyncio.run(session.clear_session())
    st.write(asyncio.run(session.get_items()))
