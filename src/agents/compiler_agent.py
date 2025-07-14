"""Agent that compiles final output when score threshold met."""

from crewai import Agent

COMPILER_SYSTEM_PROMPT = (
    "Merge all questions, answers, and snippets into final text."
)

class CompilerAgent(Agent):
    def __init__(self, model: str):
        super().__init__(
            name="Compiler",
            system_prompt=COMPILER_SYSTEM_PROMPT,
            model=model,
        )
