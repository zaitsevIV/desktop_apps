import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as file:
        text = file.read()
        txt_edit.insert(tk.END, text)
    root.title(f"Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as file:
        text = txt_edit.get("1.0", tk.END)
        file.write(text)
    root.title(f"Text Editor - {filepath}")


def open_button(operation):
    return tk.Button(button_frame, width=12, height=1, text=operation, command=open_file)


def save_button(operation):
    return tk.Button(button_frame, width=12, height=1, text=operation, command=save_file)


def button_config(operation):
    return tk.Button(button_frame, width=12, height=1, text=operation, command=open_file)


root = tk.Tk()
root.title("notepad")
root.resizable(0, 0)

root.grid_columnconfigure(0, minsize=100, weight=1)
root.grid_columnconfigure(1, minsize=1000, weight=1)

root.grid_rowconfigure(0, minsize=600, weight=1)

txt_edit = tk.Text(root)
button_frame = tk.Frame(root)

button_frame.grid(row=0, column=0, sticky="nsew")
txt_edit.grid(row=0, column=1, sticky="nsew")


open_button("open file").grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
save_button("save file").grid(row=1, column=0, sticky="nsew", padx=3, pady=3)

if __name__ == "__main__":
    root.mainloop()
