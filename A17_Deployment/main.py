from dotenv import load_dotenv
from fastapi import FastAPI
from openai import AsyncOpenAI
from pydantic import BaseModel

load_dotenv()

from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You help users with their questions.")
# result = Runner.run_sync(agent, "Why is it called Budapest")
# print(result.final_output)

app = FastAPI()

client = AsyncOpenAI()


class CreateConversationResponse(BaseModel):
    conversation_id: str

@app.post("/conversations")
async def create_conversation() -> CreateConversationResponse:
    conversation = await client.conversations.create()
    return CreateConversationResponse(conversation_id=conversation.id)

@app.get("/conversations/{conversation_id}/message")
async def create_message(conversation_id: str):
    print(conversation_id)
    pass