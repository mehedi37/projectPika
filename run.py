import tkinter as tk
import threading
import sys

class TerminalUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH)
        self.create_widgets()

        self.process = None

    def create_widgets(self):
        self.output_text = tk.Text(self, height=20, width=50, font=("Courier New", 12))
        self.output_text.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_execution, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_execution, font=("Arial", 14), bg="#F44336", fg="white", state=tk.DISABLED)
        self.stop_button.pack(side="left", padx=10)

        self.status_label = tk.Label(self, text="Ready", font=("Arial", 12), fg="black")
        self.status_label.pack(pady=10)

    def start_execution(self):
        if self.process is None or self.process.poll() is not None:
            self.status_label.config(text="Executing main.py...")
        try:
            exec(open("main.py").read())
        except Exception as e:
            self.output_text.insert(tk.END, f"An error occurred: {e}\n", "error")
            self.output_text.see(tk.END)

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)


    def stop_execution(self):
        self.status_label.config(text="Execution stopped")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

# Create the Tkinter window
root = tk.Tk()

root.title("Project Pika")

# Set a custom window background color
root.configure(bg="#F5F5F5")

# Create an instance of the TerminalUI class
app = TerminalUI(master=root)

# Set window dimensions and center it on the screen
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Start the Tkinter event loop
app.mainloop()
