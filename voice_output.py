"""Local text-to-speech output."""
def speak(text: str) -> None:
    print(f"Assistant: {text}\n")
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 178)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as exc:
        print(f"(Text-to-speech unavailable: {exc})")
