
from dotenv import load_dotenv
from fastapi import FastAPI
from openai import AsyncOpenAI
from pydantic import BaseModel
from starlette.responses import StreamingResponse

load_dotenv()

from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You help users with their questions.")
# result = Runner.run_sync(agent, "Why is it called Budapest")
# print(result.final_output)

app = FastAPI()

client = AsyncOpenAI()

class CreateConversationResponse(BaseModel):
    conversation_id: str


@app.get("/conversations")
async def create_conversation() -> CreateConversationResponse:
    conversation = await client.conversations.create()
    return CreateConversationResponse(conversation_id=conversation.id)


class CreateMessageInput(BaseModel):
    questions: str


class CreateMessageOutput(BaseModel):
    answer: str


@app.post("/conversations/{conversation_id}/message")
async def create_message(
        conversation_id: str,
        message_input: CreateMessageInput
) -> CreateMessageOutput:
    answer = await Runner.run(
        starting_agent=agent,
        input=message_input.questions,
        conversation_id=conversation_id
    )
    return CreateMessageOutput(answer=answer.final_output)


@app.post("/conversations/{conversation_id}/message-stream")
async def create_message_stream(
        conversation_id: str,
        message_input: CreateMessageInput
) -> StreamingResponse:
    async def event_generator():
        events = Runner.run_streamed(
            starting_agent=agent,
            input=message_input.questions,
            conversation_id=conversation_id
        )
        async for event in events.stream_events():
            if event.type == "raw_response_event" and event.data.type == "response.output_text.delta":
                yield event.data.delta

    return StreamingResponse(event_generator(), media_type="text/plain")

@app.post("/conversations/{conversation_id}/message-stream-all")
async def create_message_stream_all(
        conversation_id: str,
        message_input: CreateMessageInput
) -> StreamingResponse:
    async def event_generator():
        events = Runner.run_streamed(
            starting_agent=agent,
            input=message_input.questions,
            conversation_id=conversation_id
        )
        async for event in events.stream_events():
            if event.type == "raw_response_event":
                yield f"{event.data.to_json()}\n"

    return StreamingResponse(event_generator(), media_type="text/plain")

# curl -N -X POST "http://127.0.0.1:8000/conversations/conv_68fae2e342b48196bdbe6514fb6a5da60807b4afcd30161d/message-stream" \
#      -H "Content-Type: application/json" \
#      -d '{"questions": "let me know about korea stock"}'