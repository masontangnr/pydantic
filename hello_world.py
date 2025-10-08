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
    'meta-llama/llama-3.2-1b-instruct',
    provider=OpenRouterProvider(api_key=api_key),
)

# Define your agent
agent = Agent(
    model=model,
    instructions='Be concise, reply with one sentence.',
)

# Run query
result = agent.run_sync('Where does "hello world" come from?')
print(result.output)