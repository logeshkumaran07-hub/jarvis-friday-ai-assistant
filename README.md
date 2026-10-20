# JARVIS + FRIDAY AI Assistant

A Windows desktop voice assistant with two selectable AI personas:

- **JARVIS** — Google Gemini
- **FRIDAY** — OpenAI

## Features

- Tkinter desktop chat UI and command-line fallback.
- Select JARVIS or FRIDAY.
- Typed prompts and one-shot microphone input.
- Optional spoken responses through the default audio device.
- Session conversation history.
- Quick-launch buttons and allow-listed commands for Notepad, Calculator, Paint, and Explorer.
- API keys loaded from a local `.env` file.

## Setup on Windows

1. Install Python 3.11 or newer.
2. Clone this repository and open PowerShell in the folder.
3. Create a virtual environment and install dependencies:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Create your local environment file:
   ```powershell
   Copy-Item .env.example .env
   notepad .env
   ```
5. Add the API key(s) you use to `.env`.
6. Start the desktop UI:
   ```powershell
   python desktop_ui.py
   ```
   Or double-click `run_gui.bat`.

For the original terminal interface, run `python main.py`.

## API keys

- `GEMINI_API_KEY`: Google AI Studio key for JARVIS.
- `OPENAI_API_KEY`: OpenAI API key for FRIDAY.

API usage may incur charges. A ChatGPT subscription and OpenAI API billing are separate.

## App launching

Use the UI quick-launch buttons, or type commands such as `/open notepad`, `/open calculator`, `/open paint`, or `/open explorer`. Launching is restricted to a fixed allow-list and uses `shell=False`; arbitrary shell commands are not accepted.

## Safety and privacy

- Prompts are sent to the selected AI provider.
- Microphone input is captured only after pressing **Voice input**. This stage does not continuously listen for a wake word.
- Never commit real API keys, passwords, or personal information. The real `.env` file is ignored by Git.
- The app does not execute arbitrary AI-generated system commands.

## Project structure

```text
jarvis-friday-ai-assistant/
├── main.py
├── desktop_ui.py
├── app_launcher.py
├── jarvis.py
├── friday.py
├── ai_client.py
├── voice_input.py
├── voice_output.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── run_gui.bat
└── docs/
    ├── architecture.md
    └── desktop-ui.md
```

This is an evolving starter project. API access, microphone permissions, audio drivers, and Python package compatibility can vary by computer.
