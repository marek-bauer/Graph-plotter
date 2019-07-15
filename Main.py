from tkinter import *
from Graph import Graph
import math

window = Tk()

graph = Graph(window, width=400, height=400, function=lambda x: math.sin(1 / x),
              derivative=lambda x: math.cos(1 / x) * 1 / (x * x), graphX=10, graphY=10)
controlFrame = Frame(window)

graph.pack(side=LEFT)
controlFrame.pack(side=RIGHT)

graph.print()
window.mainloop()
