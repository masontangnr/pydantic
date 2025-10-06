from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider
import os
from dotenv import load_dotenv

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
# this will work with a function that reads each line and display it
# run sync function is useful when you want to see it line by line
result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)

