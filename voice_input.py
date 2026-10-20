"""Microphone input with a typed-input fallback."""
def listen(timeout: int = 6, phrase_time_limit: int = 18) -> str:
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening... speak now.")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.strip()
        except sr.UnknownValueError:
            print("I could not understand that audio.")
            return ""
        except sr.RequestError as exc:
            print(f"Speech recognition service error: {exc}")
            return ""
    except Exception as exc:
        print(f"Microphone unavailable ({exc}).")
        return ""
