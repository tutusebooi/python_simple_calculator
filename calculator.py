import tkinter as tk

def add_to_calculator(symbol):
    current_text = text_box.get("1.0", tk.END).strip()
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, current_text + str(symbol))
    if symbol == "-":
        return minus_all()
    elif symbol =="+":
        return add_to_calculator()
    elif symbol == "*":
        return multiply_all()
    elif symbol == "/":
        return devide_all()
    else:
        print("Invalid operation")


def clear_calculator():
    text_box.delete("1.0", tk.END)

def evaluate_calculator():
    expression = text_box.get("1.0", tk.END).strip()
    try:
        result = eval(expression)
        clear_calculator()
        text_box.insert(tk.END, str(result))
    except Exception as e:
        clear_calculator()
        text_box.insert(tk.END, "Error")

def user_interface():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Simple Calculator")

    global text_box
    text_box = tk.Text(root, height=2, font=("bold", 16))
    text_box.pack(padx=10, pady=10)

    # Creating the buttons for numbers 0-9
    button_frame = tk.Frame(root)
    button_frame.pack()

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
    ]

    for (text, row, col) in buttons:
        tk.Button(button_frame, text=text, width=5, height=2, command=lambda t=text: add_to_calculator(t)).grid(row=row, column=col)

    # Operator buttons
    operators = [
        ('+', 1, 3), ('-', 2, 3),
        ('*', 3, 3), ('/', 4, 3)
    ]

    for (symbol, row, col) in operators:
        tk.Button(button_frame, text=symbol, width=5, height=2, command=lambda s=symbol: add_to_calculator(s)).grid(row=row, column=col)

    # Equal and Clear buttons
    tk.Button(button_frame, text='=', width=5, height=2, command=evaluate_calculator).grid(row=4, column=2)
    tk.Button(button_frame, text='C', width=5, height=2, command=clear_calculator).grid(row=4, column=0)

    root.mainloop()

user_interface()
