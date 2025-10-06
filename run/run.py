from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider
import os
from dotenv import load_dotenv
import asyncio

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Define your model using OpenRouter's OpenAI-compatible API
model = OpenAIChatModel(
    'deepseek/deepseek-chat-v3.1:free',
    provider=OpenRouterProvider(api_key=api_key),
)
# Define your agent
agent = Agent(
    model=model,
)

async def main():
    # an async function which returns a RunResult containing a completed response.
    agent_run = await agent.run('What is the capital of France?')
    print(agent_run.output)

if __name__ == "__main__":
    asyncio.run(main())
