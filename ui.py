import tkinter as tk
import subprocess

def on_click(event):
    # Replace "path_to_python_interpreter" with the path to your Python interpreter
    python_interpreter_path = "python"

    # Replace "path_to_script" with the path to the Python script you want to run
    script_path = "main.py"

    # Run the script using the Python interpreter
    subprocess.Popen([python_interpreter_path, script_path])

root = tk.Tk()

# Load the GIF
gif_path = "gif1.gif"  # Replace with your GIF file path
gif = tk.PhotoImage(file=gif_path)

# Create a label to display the GIF
label = tk.Label(root, image=gif)
label.pack()

# Bind click event to the label
label.bind("<Button-1>", on_click)

root.mainloop()
