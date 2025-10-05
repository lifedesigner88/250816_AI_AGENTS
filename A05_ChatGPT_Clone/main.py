import dotenv, asyncio, base64

dotenv.load_dotenv()

import streamlit as st
from agents import Agent, Runner, SQLiteSession, WebSearchTool, FileSearchTool

from openai import OpenAI

client = OpenAI()
VECTOR_STORE_ID = "vs_68e202a7b2bc8191a4d0fa63720c4a8c"

if "agent" not in st.session_state:
    st.session_state["agent"] = Agent(
        name="Chat GPT Clone",
        instructions="""
        You are a helpful assistant.
        
        You have access to the following tools:
            - Web Search Tool: User this when the user asks a questions that isn't in your training data. 
            Use this tool when the users asks about current or future events,
            when you think you don't know the answer, try searching for it in the web first
            - File Search Tool: Use this tool when the user asks a question about facts related to themselves. 
            or when they ask questions about specific files.

        """,
        tools=[
            WebSearchTool(),
            FileSearchTool(
                vector_store_ids=[VECTOR_STORE_ID],
                max_num_results=3,
            ),
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
                    content = message["content"]
                    if isinstance(content, str):
                        st.write(content)
                    elif isinstance(content, list):
                        for part in content:
                            if "image_url" in part:
                                st.image(part["image_url"])
                else:
                    if message["type"] == "message":
                        st.write(message["content"][0]["text"].replace("$", "\$"))
        if "type" in message:
            if message["type"] == "web_search_call":
                with st.chat_message("ai"):
                    st.write("🔎 Searched the Web")
            elif message["type"] == "file_search_call":
                with st.chat_message("ai"):
                    st.write("📂 Searched Your files")


asyncio.run(paint_histroy())


def update_status(status_container, event):
    status_messages = {
        "response.web_search_call.completed": (
            "✅ Web search completed.",
            "complete"
        ),
        "response.web_search_call.in_progress": (
            "🔍 Starting web search...",
            "running",
        ),
        "response.web_search_call.searching": (
            "🔍 Web search in progress...",
            "running",
        ),
        "response.file_search_call.completed": (
            "✅ File search completed.",
            "complete",
        ),
        "response.file_search_call.in_progress": (
            "🗂️ Starting file search...",
            "running",
        ),
        "response.file_search_call.searching": (
            "🗂️ File search in progress...",
            "running",
        ),
        "response.completed": (" ", "complete"),
    }

    if event in status_messages:
        label, state = status_messages[event]
        status_container.update(label=label, state=state)


async def run_agent(message):
    with st.chat_message("ai"):
        status_container = st.status("⏳", expanded=False)

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
                update_status(status_container, event.data.type)
                if event.data.type == "response.output_text.delta":
                    response += event.data.delta
                    text_placeholder.write(response.replace("$", "\$"))


prompt = st.chat_input(
    "Write a message for your assistant",
    accept_file=True,
    file_type=["txt", "jpg", "jpeg", "gif", "png"],
)

if prompt:
    for file in prompt.files:
        if file.type.startswith("text/"):
            with st.chat_message("ai"):
                with st.status("⌛ Uploading file...") as status:
                    uploaded_file = client.files.create(
                        file=(file.name, file.getvalue()),
                        purpose="user_data"
                    )
                    status.update(label="⌛ Attaching file...")
                    client.vector_stores.files.create(
                        vector_store_id=VECTOR_STORE_ID,
                        file_id=uploaded_file.id,
                    )
                    status.update(label="✅ File uploaded", state="complete")
        elif file.type.startswith("image/"):
            with st.status("⌛ Uploading image ... ") as status:
                file_bytes = file.getvalue()
                base64_data = base64.b64encode(file_bytes).decode("utf-8")
                data_url = f"data:{file.type};base64,{base64_data}"
                asyncio.run(
                    session.add_items(
                        [{
                            "role": "user",
                            "content": [{
                                "type": "input_image",
                                "detail": "auto",
                                "image_url": data_url,
                            }]
                        }]
                    )
                )
                status.update(label="✅ Image uploaded", state="complete")
            with st.chat_message("human"):
                st.image(data_url)

    if prompt.text:
        with st.chat_message("human"):
            st.write(prompt.text)
        asyncio.run(run_agent(prompt.text))

with st.sidebar:
    reset = st.button("Reset Memory")
    if reset:
        asyncio.run(session.clear_session())
    st.write(asyncio.run(session.get_items()))
