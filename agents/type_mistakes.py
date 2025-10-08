from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

@dataclass
class User:
    name: str


agent = Agent(
    'test',
    deps_type=User,  
    output_type=bool,
)


@agent.system_prompt
def add_user_name(ctx: RunContext[str]) -> str:  
    return f"The user's name is {ctx.deps}."
def foobar(x: bytes) -> None:
    pass
result = agent.run_sync('Does their name start with "A"?', deps=User('Anne'))
foobar(result.output)

# uv run mypy type_mistakes.py
# type_mistakes.py:18: error: Argument 1 to "system_prompt" of "Agent" has incompatible type "Callable[[RunContext[str]], str]"; expected "Callable[[RunContext[User]], str]"  [arg-type]
# type_mistakes.py:28: error: Argument 1 to "foobar" has incompatible type "bool"; expected "bytes"  [arg-type]
# Found 2 errors in 1 file (checked 1 source fi