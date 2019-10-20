import time
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


def function_range(fn, der, x1, x2) -> (int, int):
    try:
        der = safe_function(der)
        precision = x2 - x1
        y = fn(x1)
        f_min = y
        f_max = y
        while x1 < x2:
            d = der(x1)
            if d is not None and d != 0.0:
                mov = max(abs(2 * precision / d), precision / 10)
            else:
                mov = precision / 10
            for i in range(20):
                if f_min - 2 * precision <= fn(x1 + mov) <= f_max + 2 * precision:
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


def characteristic_values(min, max, number_of_values):
    if number_of_values < 1:
        return []
    t = max - min
    step = t / number_of_values
    r = math.floor(math.log10(t)) - math.ceil(math.log10(number_of_values))
    step = (math.ceil(step * 10 ** -r) / 10 ** -r)
    min = round(min / step + 1) * step
    results = []
    for i in range(number_of_values):
        results.append(round((min + step * i) * 10 ** -r) / 10 ** -r)
    return results


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
            self.graphX = -4
        if "graphY" in kw:
            self.graphY = kw.get("graphY")
            kw.pop("graphY")
        else:
            self.graphY = 4
        if "scale" in kw:
            self.scale = kw.get("scale")
            kw.pop("scale")
        else:
            self.scale = 0.02
        # painting
        self.is_printing = False
        Widget.__init__(self, master, 'canvas', cnf, kw)
        self.print()
        # bindings
        self.bind("<Configure>", lambda e: self.print())
        self.x_mouse_prev_pos = 0
        self.y_mouse_prev_pos = 0
        self.bind("<ButtonPress-1>", self.button_pressed)
        self.bind("<B1-Motion>", self.reposition)
        self.bind("<MouseWheel>", self.mouse_wheel)

    def change_function(self, fn, der=None):
        self.function = fn
        if der is None:
            self.derivative = lambda x: (fn(x) - fn(x+0.00000001))/0.00000001
        else:
            self.derivative = der
        self.print()

    def button_pressed(self, e):
        self.x_mouse_prev_pos = e.x
        self.y_mouse_prev_pos = e.y

    def reposition(self, e):
        self.graphX += (self.x_mouse_prev_pos - e.x) * self.scale
        self.graphY += (e.y - self.y_mouse_prev_pos) * self.scale
        self.x_mouse_prev_pos = e.x
        self.y_mouse_prev_pos = e.y
        self.print()

    def mouse_wheel(self, e):
        prev_scale = self.scale
        self.scale *= 0.8 ** (e.delta / 120)
        scale_diff = prev_scale - self.scale
        self.graphX += scale_diff * (e.x - 2)
        self.graphY -= scale_diff * (e.y - 2)
        self.print()

    def print(self):
        if self.is_printing is False:
            self.is_printing = True
            prev = self.find_all()
            self.update()
            w = self.winfo_width()
            h = self.winfo_height()
            self.create_rectangle(2, 2, w - 3, h - 3)
            for i in range(w):
                min, max = function_range(self.function, self.derivative, self.graphX + i * self.scale,
                                          self.graphX + (i + 1) * self.scale)
                if min is not None and max is not None:
                    if max - min > self.scale:
                        self.create_line(i, (self.graphY - min) / self.scale, i,
                                         (self.graphY - max) / self.scale, fill="blue")
                    else:
                        self.create_line(i, (self.graphY - min) / self.scale, i,
                                         (self.graphY - min) / self.scale + 1, fill="blue")
            self.draw_axis()
            for i in prev:
                self.delete(i)
            self.is_printing = False

    def draw_axis(self):
        w = self.winfo_width()
        h = self.winfo_height()
        x_ax_position = min(max(self.graphY / self.scale, 2), h - 4)
        y_ax_position = min(max(self.graphX / -self.scale, 2), w - 4)
        # X ax
        self.create_line(0, x_ax_position, w, x_ax_position)
        num = characteristic_values(self.graphX, self.graphX + w * self.scale, int(w / 40))
        if len(num) >= 2:
            num = characteristic_values(self.graphX, self.graphX + w * self.scale,
                                        int(w / ((len(str(num[2]))) * 6 + 20)))
        for n in num:
            if n != 0.0 and (n - self.graphX) / self.scale + 25 < w:
                self.create_line((n - self.graphX) / self.scale, x_ax_position - 4, (n - self.graphX) / self.scale,
                                 x_ax_position + 3)
                if h - x_ax_position > 30:
                    self.create_text((n - self.graphX) / self.scale, x_ax_position + 10, text=n,
                                     font=("Courier", 10))
                else:
                    self.create_text((n - self.graphX) / self.scale, x_ax_position - 10, text=n,
                                     font=("Courier", 10))
        # Y ax
        self.create_line(y_ax_position, 0, y_ax_position, h)
        num = characteristic_values(self.graphY + h * -self.scale, self.graphY, int(h / 40))
        for n in num:
            if n != 0.0 and (self.graphY - n) / self.scale - 15 > 0:
                self.create_line(y_ax_position - 3, (self.graphY - n) / self.scale, y_ax_position + 4,
                                 (self.graphY - n) / self.scale)
                if y_ax_position > 50:
                    self.create_text(y_ax_position - 4 - (len(str(n))) * 4, (self.graphY - n) / self.scale - 1, text=n,
                                     font=("Courier", 10))
                else:
                    self.create_text(y_ax_position + 4 + (len(str(n))) * 4, (self.graphY - n) / self.scale - 1, text=n,
                                     font=("Courier", 10))
        pass
