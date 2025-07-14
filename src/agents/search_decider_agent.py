"""Agent that decides whether a web search is needed."""

import json
from crewai import Agent

SEARCH_DECIDER_SYSTEM_PROMPT = (
    "Decide if the latest answer requires a web search. "
    "Respond with JSON { need_search: 'yes'|'no', query: '...' }."
)

class SearchDeciderAgent(Agent):
    def __init__(self, model: str):
        super().__init__(
            name="SearchDecider",
            system_prompt=SEARCH_DECIDER_SYSTEM_PROMPT,
            model=model,
        )
