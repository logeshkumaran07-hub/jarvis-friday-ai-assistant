# JARVIS + FRIDAY AI Assistant

A starter Windows desktop voice assistant with two selectable AI personas:

- **JARVIS** — Google Gemini
- **FRIDAY** — OpenAI ChatGPT

This starter includes local voice input/output, typed input fallback, provider configuration, and a simple command-line conversation loop. It does not yet execute operating-system commands or silently control the computer.

## Features

- Select JARVIS (Gemini) or FRIDAY (OpenAI).
- Microphone speech input with typed-text fallback.
- Spoken responses through the computer's default audio device.
- Conversation history within the active session.
- API keys read from a local `.env` file rather than hard-coded.

## Setup on Windows

1. Install Python 3.11 or newer.
2. Download or clone this repository.
3. Open PowerShell in the project folder:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and add your provider API keys.
5. Run:
   ```powershell
   python main.py
   ```

## API keys

- `GEMINI_API_KEY`: Google AI Studio key.
- `OPENAI_API_KEY`: OpenAI platform API key.

API usage may incur charges. A ChatGPT subscription and OpenAI API billing are separate.

## Safety and privacy

- Prompts are sent to the selected AI provider.
- Microphone speech recognition uses the configured speech recognition service.
- Never commit real API keys, passwords, or personal information.
- This starter intentionally does not run arbitrary shell commands.

## Planned structure

```text
jarvis-friday-ai-assistant/
├── main.py
├── jarvis.py
├── friday.py
├── ai_client.py
├── voice_input.py
├── voice_output.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── docs/architecture.md
```

This is a starter implementation; dependencies and microphone/audio settings can vary by machine.
