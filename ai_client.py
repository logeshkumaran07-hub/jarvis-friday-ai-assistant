"""Small provider adapters for OpenAI and Gemini."""
from config import OPENAI_API_KEY, GEMINI_API_KEY, OPENAI_MODEL, GEMINI_MODEL

def ask_openai(prompt: str, history: list[dict[str, str]]) -> str:
    if not OPENAI_API_KEY:
        return "FRIDAY needs OPENAI_API_KEY. Add it to your .env file and restart."
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        messages = [{"role": "system", "content": "You are FRIDAY, a helpful, concise voice assistant. Be clear and safety-conscious."}]
        messages.extend(history[-10:])
        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(model=OPENAI_MODEL, messages=messages, temperature=0.6)
        return (response.choices[0].message.content or "").strip() or "I could not generate a response."
    except Exception as exc:
        return f"FRIDAY encountered an API error: {exc}"

def ask_gemini(prompt: str, history: list[dict[str, str]]) -> str:
    if not GEMINI_API_KEY:
        return "JARVIS needs GEMINI_API_KEY. Add it to your .env file and restart."
    try:
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        transcript = "\n".join(f'{item["role"].capitalize()}: {item["content"]}' for item in history[-10:])
        full_prompt = ("You are JARVIS, a helpful, polished voice assistant. Be concise, clear, and safety-conscious.\n"
                       f"{transcript}\nUser: {prompt}\nJARVIS:")
        response = client.models.generate_content(model=GEMINI_MODEL, contents=full_prompt)
        return (response.text or "").strip() or "I could not generate a response."
    except Exception as exc:
        return f"JARVIS encountered an API error: {exc}"
