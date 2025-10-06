from pydantic_ai import Agent, RunContext
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

roulette_agent = Agent(  
    model=model,
    # deps_type will hold the winning roulette number and be in integer
    deps_type=int,
    # output type is a boolean. True if the customer has won, False if the customer has lost.
    # You can change output type is a string. 'winner' if the customer has won, 'loser' if the customer has lost.
    output_type=bool,
    # system prompt is the instructions for the agent to use the roulette_wheel function.
    system_prompt=(
        'Use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),
)
# this decorator registers the roulette_wheel function as a tool that the LLM can call.
@roulette_agent.tool
# ctx: RunContext[int]: The RunContext is automatically passed to all tools. RunContext is a class that contains the dependencies and the output of the agent. Because we set deps_type=int on the agent, we can access the winning number using ctx.deps.
# RunContext in the OpenAI Agents SDK and Pydantic AI is a crucial component for managing state and dependencies within an agent's execution.
# ctx: RunContext[int]: This provides context for the current run, specifically holding a deps (dependencies) value, which is the winning number.
# square: int: The square is the number that the customer has bet on.
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:  
    # The function simply checks if the square the user bet on is equal to the winning number stored in ctx.deps. It returns 'winner' or 'loser' as a string.
    return 'winner' if square == ctx.deps else 'loser'
# Run the agent
success_number = 18
# we pass the winning number to the agent using the deps parameter.
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.output)  
#> True

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.output)
#> False