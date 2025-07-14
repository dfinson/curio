"""Agent that judges snippet relevance."""

from typing import List

from crewai import Agent

RELEVANCE_SYSTEM_PROMPT = (
    "Judge whether each snippet is relevant to the question. "
    "Return only the relevant snippets as JSON list."
)

class RelevanceJudgeAgent(Agent):
    def __init__(self, model: str):
        super().__init__(
            name="RelevanceJudge",
            system_prompt=RELEVANCE_SYSTEM_PROMPT,
            model=model,
        )
