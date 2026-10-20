# Architecture

Microphone or typed text -> main.py -> persona selection -> JARVIS/Gemini or FRIDAY/OpenAI -> text response -> local text-to-speech.

This version intentionally does not execute arbitrary operating-system commands. Desktop automation should be added as a separate, permission-gated module with explicit user confirmation.
