"""Agent that asks dynamic questions based on past interactions."""

from crewai import Agent

INTERVIEWER_SYSTEM_PROMPT = (
    "You are an expert interviewer guiding a conversation. "
    "Ask one concise question at a time to achieve the user's goal."
)

class InterviewerAgent(Agent):
    def __init__(self, model: str):
        super().__init__(
            name="Interviewer",
            system_prompt=INTERVIEWER_SYSTEM_PROMPT,
            model=model,
        )
