"""Main orchestration loop for Curio."""

from typing import List

from crewai import Crew

from .agents.interviewer_agent import InterviewerAgent
from .agents.search_decider_agent import SearchDeciderAgent
from .agents.web_fetcher_agent import WebFetcherAgent
from .agents.relevance_judge_agent import RelevanceJudgeAgent
from .agents.evaluator_agent import EvaluatorAgent
from .agents.synthesizer_agent import SynthesizerAgent
from .agents.compiler_agent import CompilerAgent


class CurioOrchestrator:
    """Ties all agents together in a loop."""

    def __init__(self, crew: Crew, max_turns: int = 10) -> None:
        self.crew = crew
        self.max_turns = max_turns

    async def run(self, user_goal: str) -> str:
        """Run interview until output compiled."""
        for _ in range(self.max_turns):
            result = await self.crew.run_once({'goal': user_goal})
            if result.get('compiled_output'):
                return result['compiled_output']
        return ""
