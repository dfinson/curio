"""Simple web search utility using Tavily's Python SDK."""

from typing import List
from tavily import AsyncTavilyClient


async def web_search(query: str, max_calls: int = 3) -> List[str]:
    """Query Tavily and return snippet texts."""
    async with AsyncTavilyClient() as client:
        data = await client.search(query, max_results=max_calls)
        return [item.get("content", "") for item in data.get("results", [])]
