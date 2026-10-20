"""Safe, allow-listed Windows app launcher. Never executes arbitrary user-supplied commands."""
import os
import subprocess

# Extend this dictionary only with known, trusted executable paths or Windows app aliases.
SUPPORTED_APPS = ("notepad", "calculator", "paint", "explorer")

APP_COMMANDS = {
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
    "paint": ["mspaint.exe"],
    "explorer": ["explorer.exe"],
}

def launch_app(name: str) -> str:
    key = name.strip().lower()
    if key not in APP_COMMANDS:
        options = ", ".join(SUPPORTED_APPS)
        raise ValueError(f"App not allowed. Choose one of: {options}.")
    try:
        subprocess.Popen(APP_COMMANDS[key], shell=False, close_fds=True)
        return f"Opened {key}."
    except OSError as exc:
        return f"Could not open {key}: {exc}. This launcher is intended for Windows."
