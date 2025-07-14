"""Agent that synthesizes paragraphs from snippets and Q-A."""

from crewai import Agent

SYNTHESIZER_SYSTEM_PROMPT = (
    "Write one coherent paragraph incorporating all provided snippets and context."
)

class SynthesizerAgent(Agent):
    def __init__(self, model: str):
        super().__init__(
            name="Synthesizer",
            system_prompt=SYNTHESIZER_SYSTEM_PROMPT,
            model=model,
        )
