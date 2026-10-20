# Desktop UI (Stage 2)

Run `python desktop_ui.py` or double-click `run_gui.bat` on Windows.

## Included
- Tkinter desktop chat window.
- Selectable JARVIS (Gemini) / FRIDAY (OpenAI) persona.
- Text input and one-shot microphone input.
- Optional spoken responses.
- Quick-launch buttons for Notepad, Calculator, Paint, and Explorer.
- `/open notepad`, `/open calculator`, `/open paint`, and `/open explorer` commands.

## Safety
The microphone is only accessed when the user presses **Voice input**. There is no continuous recording or wake-word listener in this stage. Application launching uses a fixed allow-list and `shell=False`; arbitrary shell commands are not accepted.

## Known limitation
The UI calls the configured cloud AI APIs, so the relevant API key and internet access are required. Speech recognition and audio dependencies depend on the local Windows setup.
