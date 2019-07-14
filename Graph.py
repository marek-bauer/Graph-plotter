from tkinter import *

import math


def safe_value(f, x):
    try:
        return f(x)
    except:
        return None


def safe_function(f):
    return lambda x: safe_value(f, x)


def value_to_range(x, min, max):
    if x < min:
        return x, max
    elif x > max:
        return min, x
    else:
        return min, max


def function_range(fn, der, x1, x2):
    try:
        der = safe_function(der)
        precision = x2 - x1
        y = fn(x1)
        f_min = y
        f_max = y
        while x1 < x2:
            d = der(x1)
            if d is not None and d != 0.0:
                mov = abs(precision / d)
            else:
                mov = precision / 10
            for i in range(10):
                if y - precision <= fn(x1 + mov) <= y + precision:
                    y = fn(x1 + mov)
                    x1 += mov
                    f_min, f_max = value_to_range(y, f_min, f_max)
                    break
                else:
                    mov /= 2
            else:
                return f_min, f_max
        return f_min, f_max
    except:
        return None, None


class Graph(Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        if "function" in kw:
            self.function = kw.get("function")
            kw.pop("function")
        else:
            self.function = lambda x: x
        if "derivative" in kw:
            self.derivative = kw.get("derivative")
            kw.pop("derivative")
        else:
            self.derivative = lambda x: (self.function(x) - self.function(x + 0.0000001)) / 0.0000001
        if "graphX" in kw:
            self.graphX = kw.get("graphX")
            kw.pop("graphX")
        else:
            self.graphX = 0
        if "graphY" in kw:
            self.graphY = kw.get("graphY")
            kw.pop("graphY")
        else:
            self.graphY = 5
        if "scale" in kw:
            self.scale = kw.get("scale")
            kw.pop("scale")
        else:
            self.scale = 0.02
        Widget.__init__(self, master, 'canvas', cnf, kw)

    def print(self):
        self.create_line(5, 5, 6, 6, fill="green")
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        self.create_rectangle(2, 2, w - 3, h - 3)
        for i in range(w):
            min, max = function_range(self.function, self.derivative, self.graphX + i * self.scale,
                                      self.graphX + (i + 1) * self.scale)
            if min is not None and max is not None:
                self.create_line(i, (self.graphY - min) / self.scale, i,
                                 (self.graphY - max) / self.scale, fill="blue")
