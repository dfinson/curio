"""Simple web search utility."""

from typing import List
import httpx
import os

SEARCH_API_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"

async def web_search(query: str, max_calls: int = 3) -> List[str]:
    api_key = os.getenv("SEARCH_API_KEY")
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": str(max_calls)}
    async with httpx.AsyncClient() as client:
        resp = await client.get(SEARCH_API_ENDPOINT, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        return [item.get('snippet', '') for item in data.get('webPages', {}).get('value', [])]
