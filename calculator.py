# simple calculator GUI
import tkinter as tk
from opertations import *

def add_to_calculator(symbol):
    pass


def clear_calculator():
    pass


def user_input( num1,num2):
    num1 = int(input())
    num2 = int(input())
    return num1, num2


def user_interfase():
    root= tk.Tk()

    root.geometry("500x500")

    label = tk.Label(root, text="Calculator",font=("Bold", 15))
    label.pack()
    text_box = tk.Text(root, height=2,font=("bold",16))
    text_box.pack(padx=10)

    button = tk.Button(root,text="ENTER", font=("Bold", 18))
    button.pack()
    #tk.CENTER()


    root.mainloop()
user_interfase()


