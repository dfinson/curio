"""Agent that performs web searches."""

from typing import List

from crewai import Agent

from ..tools.web_search import web_search

WEB_FETCHER_SYSTEM_PROMPT = (
    "Perform the provided search query and return raw snippets as JSON list."
)

class WebFetcherAgent(Agent):
    def __init__(self, model: str, max_calls: int = 3):
        super().__init__(
            name="WebFetcher",
            system_prompt=WEB_FETCHER_SYSTEM_PROMPT,
            model=model,
        )
        self.max_calls = max_calls

    async def fetch(self, query: str) -> List[str]:
        return await web_search(query, self.max_calls)
