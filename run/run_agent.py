from pydantic_ai import Agent, AgentRunResultEvent, AgentStreamEvent
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

result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.output)
#> The capital of Italy is Rome.


async def main():
    result = await agent.run('What is the capital of France?')
    print(result.output)
    #> The capital of France is Paris.

    async with agent.run_stream('What is the capital of the UK?') as response:
        async for text in response.stream_text():
            print(text)
            #> The capital of
            #> The capital of the UK is
            #> The capital of the UK is London.

    events: list[AgentStreamEvent | AgentRunResultEvent] = []
    async for event in agent.run_stream_events('What is the capital of Mexico?'):
        events.append(event)
    print(events)
    """
    [
        PartStartEvent(index=0, part=TextPart(content='The capital of ')),
        FinalResultEvent(tool_name=None, tool_call_id=None),
        PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='Mexico is Mexico ')),
        PartDeltaEvent(index=0, delta=TextPartDelta(content_delta='City.')),
        AgentRunResultEvent(
            result=AgentRunResult(output='The capital of Mexico is Mexico City.')
        ),
    ]
    """

if __name__ == "__main__":
    asyncio.run(main())