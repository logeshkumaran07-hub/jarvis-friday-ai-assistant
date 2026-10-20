"""JARVIS persona powered by Google Gemini."""
from ai_client import ask_gemini

def respond(prompt: str, history: list[dict[str, str]]) -> str:
    return ask_gemini(prompt, history)
