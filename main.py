import tkinter as tk
import threading
import pyttsx3
import speech_recognition as sr
from cmd_assistant import cmd

# I have created this instance for resetting the screen and self running again
class TerminalUI(tk.Frame):
    def set_desired_voice(self):
        desired_voice = "Microsoft Zira Desktop - English (United States)"
        voices = self.engine.getProperty('voices')
        for idx, voice in enumerate(voices):
            if desired_voice in voice.name:
                self.engine.setProperty('voice', voices[idx].id)
                break

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH)
        self.create_widgets()

        self.engine = pyttsx3.init()
        self.set_desired_voice()

        self.r = sr.Recognizer()
        self.wake_up_phrase = "hi"      # say this to start the assistant

    def create_widgets(self):
        self.output_text = tk.Text(self, height=20, width=50, font=("Courier New", 12))
        self.output_text.pack(pady=10)

        self.status_label = tk.Label(self, text="Ready", font=("Arial", 12), fg="black")
        self.status_label.pack(pady=10)

    def listen_for_wake_up(self):
        # self.engine.say("Hi, I'm Project Pika. Say the wake-up phrase to activate me.")
        # self.engine.runAndWait()

        while True:
            with sr.Microphone() as source:
                audio = self.r.listen(source, phrase_time_limit=5)
            try:
                text = self.r.recognize_google(audio)
                if self.wake_up_phrase in text.lower():
                    self.engine.say("How can I help you?")
                    self.engine.runAndWait()
                    self.process_speech()
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                self.output_text.insert(tk.END, f"⚠️ Error: {e}\n")
                self.output_text.see(tk.END)

    def reset_app(self):
        self.status_label.config(text="Resetting...")
        self.update_idletasks()
        self.output_text.delete(1.0, tk.END)
        self.master.after(1000, lambda: self.status_label.config(text="Ready"))

    def process_speech(self):
        while True:
            with sr.Microphone() as source:
                audio = self.r.listen(source, phrase_time_limit=5)
            try:
                text = self.r.recognize_google(audio)
                if "reset" in text.lower():
                    self.reset_app()
                    continue

                self.status_label.config(text="Processing command...")
                self.output_text.insert(tk.END, f"📢 You said: {text}\n")
                self.output_text.see(tk.END)
                response = cmd(text)

                self.output_text.insert(tk.END, f"🤖 Pika: {response}\n")
                self.output_text.see(tk.END)

                self.engine.say(response)
                self.engine.runAndWait()

                self.status_label.config(text="Listening...")
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                self.output_text.insert(tk.END, f"⚠️ Error: {e}\n")
                self.output_text.see(tk.END)

root = tk.Tk()
root.title("Project Pika")
root.configure(bg="#F5F5F5")

app = TerminalUI(master=root)

window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

wake_up_thread = threading.Thread(target=app.listen_for_wake_up)
wake_up_thread.start()

app.mainloop()