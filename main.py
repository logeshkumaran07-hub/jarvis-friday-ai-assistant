"""Command-line entry point for the JARVIS + FRIDAY assistant."""
import sys
import jarvis
import friday
from voice_input import listen
from voice_output import speak

def choose_persona():
    print("\n=== JARVIS + FRIDAY AI Assistant ===")
    print("1. JARVIS  — Gemini")
    print("2. FRIDAY  — ChatGPT / OpenAI")
    choice = input("Choose assistant [1/2]: ").strip()
    return ("JARVIS", jarvis.respond) if choice == "1" else ("FRIDAY", friday.respond)

def main() -> None:
    name, responder = choose_persona()
    history: list[dict[str, str]] = []
    print(f"\n{name} online. Type /help for commands.")
    while True:
        mode = input("\nPress Enter to speak, type a message, or enter /quit: ").strip()
        if mode.lower() in {"/quit", "/exit"}:
            print(f"{name}: Signing off.")
            break
        if mode.lower() == "/help":
            print("Commands: /help, /clear, /quit. Press Enter for microphone input.")
            continue
        if mode.lower() == "/clear":
            history.clear()
            print("Conversation history cleared.")
            continue
        prompt = mode if mode else listen()
        if not prompt:
            typed = input("Type your message (or press Enter to try again): ").strip()
            if not typed:
                continue
            prompt = typed
        if prompt.lower() in {"/quit", "/exit"}:
            break
        answer = responder(prompt, history)
        speak(answer)
        history.extend([{"role": "user", "content": prompt}, {"role": "assistant", "content": answer}])
        history = history[-20:]

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye.")
        sys.exit(0)
