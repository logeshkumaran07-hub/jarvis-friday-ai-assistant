"""FRIDAY persona powered by OpenAI."""
from ai_client import ask_openai

def respond(prompt: str, history: list[dict[str, str]]) -> str:
    return ask_openai(prompt, history)
