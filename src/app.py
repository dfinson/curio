"""FastAPI backend for Curio."""

import asyncio
import os
from fastapi import FastAPI, WebSocket
from crewai import Crew, Task

from .agents import (
    InterviewerAgent,
    SearchDeciderAgent,
    WebFetcherAgent,
    RelevanceJudgeAgent,
    EvaluatorAgent,
    SynthesizerAgent,
    CompilerAgent,
)
from .config_loader import load_env
from .orchestrator import CurioOrchestrator

load_env()

app = FastAPI(title="Curio")

INTERVIEWER_MODEL = os.getenv("INTERVIEWER_MODEL", "gpt-4")
GENERIC_MODEL = os.getenv("GENERIC_MODEL", "gpt-3.5-turbo")
MAX_SEARCH_CALLS = int(os.getenv("MAX_SEARCH_CALLS", "3"))
SCORE_THRESHOLD = float(os.getenv("SCORE_THRESHOLD", "0.8"))

interviewer = InterviewerAgent(model=INTERVIEWER_MODEL)
search_decider = SearchDeciderAgent(model=GENERIC_MODEL)
fetcher = WebFetcherAgent(model=GENERIC_MODEL, max_calls=MAX_SEARCH_CALLS)
judge = RelevanceJudgeAgent(model=GENERIC_MODEL)
evaluator = EvaluatorAgent(model=GENERIC_MODEL)
synthesizer = SynthesizerAgent(model=GENERIC_MODEL)
compiler = CompilerAgent(model=GENERIC_MODEL)

# Register tasks
crew = Crew(
    agents=[
        interviewer,
        search_decider,
        fetcher,
        judge,
        evaluator,
        synthesizer,
        compiler,
    ],
    tasks=[
        Task(name="ask_question", agent=interviewer),
        Task(name="decide_search", agent=search_decider, depends_on=["ask_question"]),
        Task(name="perform_search", agent=fetcher, condition="need_search == 'yes'", depends_on=["decide_search"]),
        Task(name="judge_relevance", agent=judge, depends_on=["perform_search"]),
        Task(name="evaluate", agent=evaluator, depends_on=["judge_relevance"]),
        Task(name="synthesize", agent=synthesizer, depends_on=["judge_relevance"]),
        Task(name="compile_output", agent=compiler, depends_on=["evaluate"], condition=f"score >= {SCORE_THRESHOLD}"),
    ],
)

orchestrator = CurioOrchestrator(crew)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    goal = await websocket.receive_text()
    result = await orchestrator.run(goal)
    await websocket.send_text(result)
    await websocket.close()

