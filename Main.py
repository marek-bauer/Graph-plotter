from tkinter import *
from Graph import Graph
import math

window = Tk()

graph = Graph(window, width=300, height=300, function=lambda x: math.cos(3.14*x), derivative=lambda x: math.sin(3.14*x))
controlFrame = Frame(window)

graph.pack(side=LEFT)
controlFrame.pack(side=RIGHT)

graph.print()
window.mainloop()
