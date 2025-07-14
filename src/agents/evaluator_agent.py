"""Agent that evaluates completeness of answers."""

from crewai import Agent

EVALUATOR_SYSTEM_PROMPT = (
    "Evaluate the conversation and snippets. "
    "Return JSON { score: 0-1, missing: ['field1', ...], draft: '...' }."
)

class EvaluatorAgent(Agent):
    def __init__(self, model: str):
        super().__init__(
            name="Evaluator",
            system_prompt=EVALUATOR_SYSTEM_PROMPT,
            model=model,
        )
