from tkinter import *
from tkinter import messagebox

from Graph import Graph
import math


window = Tk()

graph = Graph(window, width=510, function=lambda x: math.sin(1 / x),
              derivative=lambda x: math.cos(1 / x) * 1 / (x * x), graphX=-3.00, graphY=3, scale=0.01)


def draw_function():
    try:
        from StringToLambda import string_to_lambda
        from Derivative import string_to_derivative
        graph.change_function(string_to_lambda(f_entry.get()), string_to_derivative(f_entry.get()))
    except ValueError:
        messagebox.showinfo("Error", "Function f(x) = "+f_entry.get()+" is not valid")


controlFrame = Frame(window, width=300, bg="green")

title_label = Label(controlFrame, text="Graph drawer")
title_label.pack(fill="x")

function = Frame(controlFrame, width=300, bg="green")
f_label = Label(function, text="f(x) = ")
f_label.pack(side=LEFT)
f_entry = Entry(function)
f_entry.pack(side=LEFT)
function.pack(fill="x")

f_button = Button(controlFrame, text="Draw",  command=draw_function)
f_button.pack()

graph.pack(side=LEFT, fill="both", expand=True)
controlFrame.pack(side=RIGHT, fill="y")

graph.print()

window.mainloop()
