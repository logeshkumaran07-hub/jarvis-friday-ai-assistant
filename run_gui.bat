@echo off
cd /d "%~dp0"
py desktop_ui.py
if errorlevel 1 pause
