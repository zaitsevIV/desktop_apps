import tkinter as tk
from tkinter import *
from tkinter import messagebox


def press_key(event):
    value = calcul.get()
    if value[-1].isdigit() is False and value[-1] not in "+-*/":
        if "+" in value or "-" in value or "/" in value or "*" in value:
            calcul.delete(0, tk.END)
            calcul.insert(0, value[:-1])
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "-+/*":
        add_operation(event.char)
    elif event.char == "\r":
        calculate()


def add_digit(number):
    value = calcul.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calcul.delete(0, tk.END)
    calcul.insert(0, value + number)


def add_operation(operation):
    value = calcul.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    elif "+" in value or "-" in value or "/" in value or "*" in value:
        calculate()
        value = calcul.get()
    calcul.delete(0, tk.END)
    calcul.insert(0, value + operation)


def calculate():
    value = calcul.get()
    if value[-1] in "+-/*":
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calcul.delete(0, tk.END)
    try:
        calcul.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Error!", "Try again!")
        calcul.insert(0, "0")
    except ZeroDivisionError:
        messagebox.showinfo("Error!", "Dividing by zero is not allowed!")
        calcul.insert(0, "0")


def clear():
    calcul.delete(0, tk.END)
    calcul.insert(0, "0")


def delete_char():
    value = calcul.get()
    if len(value) == 1:
        value = "0" + value
    calcul.delete(0, tk.END)
    calcul.insert(0, value[:-1])


def make_float():
    value = calcul.get()
    if value[-1] in "+-/*":
        value += "0"
    float_value = value[:-1] + str(float(value[-1]))
    calcul.delete(0, tk.END)
    calcul.insert(0, float_value[:-1])


def degree():
    value = calcul.get()
    if value[-1] in "+-/*":
        value = value[:-1]
    elif "+" in value or "-" in value or "/" in value or "*" in value:
        try:
            pass
        except ValueError:
            pass
    value += "**2"
    calcul.delete(0, tk.END)
    calcul.insert(0, eval(value))


def find_sqrt():
    value = calcul.get()
    if value[-1] in "+-/*":
        value = value[:-1]
    elif "+" in value or "-" in value or "/" in value or "*" in value:
        try:
            pass
        except ValueError:
            pass
    value += "**0.5"
    calcul.delete(0, tk.END)
    calcul.insert(0, eval(value))


def button_config(digit):
    return tk.Button(text=digit, bg="#a5a5a5", command=lambda: add_digit(digit))


def calculate_button(operation):
    return tk.Button(text=operation, bg="#ff9f0a", command=calculate)


def operation_button(operation):
    return tk.Button(text=operation, bg="#ff9f0a", command=lambda: add_operation(operation))


def clear_button(operation):
    return tk.Button(text=operation, bg="white", command=clear)


def dlt_char_button(operation):
    return tk.Button(text=operation, bg="white", command=delete_char)


def float_button(operation):
    return tk.Button(text=operation, bg="#ff9f0a", command=make_float)


def degree_button(operation):
    return tk.Button(text=operation, bg="#ff9f0a", command=degree)


def sqrt_button(operation):
    return tk.Button(text=operation, bg="#ff9f0a", command=find_sqrt)


root = Tk()
root.title("calculator")
root.geometry(f"240x330+100+200")
root["bg"] = "black"

root.bind('<Key>', press_key)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.grid_rowconfigure(5, minsize=60)

calcul = tk.Entry(root, justify=tk.RIGHT, font=('Verdana', 15), width=15)
calcul.insert(0, "0")
calcul.grid(row=0, column=0, columnspan=4, sticky="we")

button_config("7").grid(row=2, column=0, sticky="wesn", padx=1, pady=1)
button_config("4").grid(row=3, column=0, sticky="wesn", padx=1, pady=1)
button_config("1").grid(row=4, column=0, sticky="wesn", padx=1, pady=1)

button_config("8").grid(row=2, column=1, sticky="wesn", padx=1, pady=1)
button_config("5").grid(row=3, column=1, sticky="wesn", padx=1, pady=1)
button_config("2").grid(row=4, column=1, sticky="wesn", padx=1, pady=1)

button_config("9").grid(row=2, column=2, sticky="wesn", padx=1, pady=1)
button_config("6").grid(row=3, column=2, sticky="wesn", padx=1, pady=1)
button_config("3").grid(row=4, column=2, sticky="wesn", padx=1, pady=1)

button_config("0").grid(row=5, column=1, sticky="wesn", padx=1, pady=1)

operation_button("/").grid(row=1, column=3, sticky="wesn", padx=1, pady=1)
operation_button("*").grid(row=2, column=3, sticky="wesn", padx=1, pady=1)
operation_button("-").grid(row=3, column=3, sticky="wesn", padx=1, pady=1)
operation_button("+").grid(row=4, column=3, sticky="wesn", padx=1, pady=1)

calculate_button("=").grid(row=5, column=3, sticky="wesn", padx=1, pady=1)
clear_button("C").grid(row=5, column=0, sticky="wesn", padx=1, pady=1)
dlt_char_button("<--").grid(row=5, column=2, sticky="wesn", padx=1, pady=1)
float_button(".").grid(row=1, column=0, sticky="wesn", padx=1, pady=1)
degree_button("^2").grid(row=1, column=1, sticky="wesn", padx=1, pady=1)
sqrt_button("sqrt").grid(row=1, column=2, sticky="wesn", padx=1, pady=1)

if __name__ == "__main__":
    root.mainloop()
