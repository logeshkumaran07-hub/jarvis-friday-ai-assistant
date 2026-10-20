"""Tkinter desktop UI for JARVIS + FRIDAY. Runs API calls off the UI thread."""
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import jarvis
import friday
from voice_input import listen
from voice_output import speak
from app_launcher import launch_app, SUPPORTED_APPS

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS + FRIDAY")
        self.root.geometry("860x650")
        self.root.minsize(680, 500)
        self.history = []
        self.busy = False
        self.speak_enabled = tk.BooleanVar(value=True)
        self.persona = tk.StringVar(value="JARVIS")
        self._build()
        self._append("System", "Ready. Choose JARVIS or FRIDAY, type a message, or use Voice Input.")

    def _build(self):
        top = ttk.Frame(self.root, padding=12)
        top.pack(fill="x")
        ttk.Label(top, text="JARVIS + FRIDAY", font=("Segoe UI", 18, "bold")).pack(side="left")
        ttk.Label(top, text="Assistant:").pack(side="left", padx=(22, 6))
        selector = ttk.Combobox(top, textvariable=self.persona, values=("JARVIS", "FRIDAY"), state="readonly", width=12)
        selector.pack(side="left")
        ttk.Checkbutton(top, text="Speak responses", variable=self.speak_enabled).pack(side="right")

        self.chat = tk.Text(self.root, wrap="word", state="disabled", font=("Segoe UI", 10), padx=12, pady=12)
        self.chat.pack(fill="both", expand=True, padx=12, pady=(0, 10))

        actions = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        actions.pack(fill="x")
        self.entry = ttk.Entry(actions)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda _event: self.send_text())
        self.send_btn = ttk.Button(actions, text="Send", command=self.send_text)
        self.send_btn.pack(side="left", padx=(8, 0))
        self.voice_btn = ttk.Button(actions, text="Voice input", command=self.voice_input)
        self.voice_btn.pack(side="left", padx=(8, 0))

        bottom = ttk.Frame(self.root, padding=(12, 0, 12, 12))
        bottom.pack(fill="x")
        ttk.Label(bottom, text="Quick launch (allow-listed apps only):").pack(side="left")
        for app in SUPPORTED_APPS:
            ttk.Button(bottom, text=app.title(), command=lambda name=app: self.open_app(name)).pack(side="left", padx=4)
        ttk.Button(bottom, text="Clear chat", command=self.clear_chat).pack(side="right")

    def _append(self, who, text):
        self.chat.configure(state="normal")
        self.chat.insert("end", f"{who}: {text}\n\n")
        self.chat.see("end")
        self.chat.configure(state="disabled")

    def _set_busy(self, busy):
        self.busy = busy
        state = "disabled" if busy else "normal"
        self.send_btn.configure(state=state)
        self.voice_btn.configure(state=state)

    def send_text(self):
        if self.busy:
            return
        prompt = self.entry.get().strip()
        if not prompt:
            return
        self.entry.delete(0, "end")
        self._submit(prompt)

    def voice_input(self):
        if self.busy:
            return
        self._set_busy(True)
        self._append("System", "Listening once. Your microphone is not continuously monitored.")
        def work():
            prompt = listen()
            self.root.after(0, lambda: self._voice_done(prompt))
        threading.Thread(target=work, daemon=True).start()

    def _voice_done(self, prompt):
        self._set_busy(False)
        if prompt:
            self._submit(prompt)
        else:
            self._append("System", "No speech recognized. You can type a message instead.")

    def _submit(self, prompt):
        if self.busy:
            return
        self._append("You", prompt)
        if prompt.lower().startswith("/open "):
            app = prompt[6:].strip().lower()
            try:
                result = launch_app(app)
            except ValueError as exc:
                result = str(exc)
            self._append("System", result)
            return
        self._set_busy(True)
        responder = jarvis.respond if self.persona.get() == "JARVIS" else friday.respond
        name = self.persona.get()
        history_snapshot = list(self.history)
        def work():
            answer = responder(prompt, history_snapshot)
            self.root.after(0, lambda: self._response_done(name, prompt, answer))
        threading.Thread(target=work, daemon=True).start()

    def _response_done(self, name, prompt, answer):
        self._set_busy(False)
        self._append(name, answer)
        self.history.extend([{"role": "user", "content": prompt}, {"role": "assistant", "content": answer}])
        self.history = self.history[-20:]
        if self.speak_enabled.get():
            threading.Thread(target=speak, args=(answer,), daemon=True).start()

    def open_app(self, app):
        try:
            message = launch_app(app)
        except ValueError as exc:
            message = str(exc)
        self._append("System", message)

    def clear_chat(self):
        self.history.clear()
        self.chat.configure(state="normal")
        self.chat.delete("1.0", "end")
        self.chat.configure(state="disabled")
        self._append("System", "Conversation history cleared.")

def main():
    root = tk.Tk()
    try:
        ttk.Style().theme_use("vista")
    except tk.TclError:
        pass
    AssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
