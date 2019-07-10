import re

# Finds end of selected bracket in string
import math


def bracket_closer_pos(data, pos):
    counter = 1
    pos += 1
    for c in data[pos:]:
        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1
        if counter == 0:
            return pos
        else:
            pos += 1
    raise ValueError("String is incorrect")


def string_to_lambda(string):
    from StringPreparation import prepare
    s = prepare(string)
    return anc_string_to_lambda(s)


def anc_string_to_lambda(string):
    if string == "":
        return lambda x: 0
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: math.pow(a, b),
        "log": lambda a, b: math.log(b, a),
        "ln": lambda a, b: math.log(a),
        "abs": lambda a, b: abs(a),
        "sin": lambda a, b: math.sin(a),
        "cos": lambda a, b: math.cos(a),
        "tg": lambda a, b: math.tan(a),
        "ctg": lambda a, b: 1 / math.tan(a),
        "arcsin": lambda a, b: math.asin(a),
        "arccos": lambda a, b: math.acos(a),
        "arctg": lambda a, b: math.atan(a),
    }
    op, left, right = operation_split(string)
    if op == "number":
        return lambda x: float(left)
    if op == "x":
        return lambda x: x
    return lambda x: operations.get(op)(string_to_lambda(left)(x), string_to_lambda(right)(x))


# Ancillary function for unary functions
def unary_operation_split(data):
    if data[0] == '(' and bracket_closer_pos(data, 0) == len(data) - 1:
        return unary_operation_split(data[1:-1])
    if '0' <= data[0] <= '9':
        return "number", data, ""
    if data[0] == 'x':
        return "x", data, ""
    unary_operators = ["abs", "sin", "cos", "tg", "ctg", "arcsin", "arccos", "arctg", "ln"]
    for op in unary_operators:
        if re.search("^" + op, data):
            return op, data[len(op):].strip(), ""
    if re.search("^log", data):
        temp = data.split(" ")
        return "log", temp[1], temp[2]


# Splits string of operation to (operator, left_argument, right,argument)
def operation_split(data):
    if data[0] == '(' and bracket_closer_pos(data, 0) == len(data) - 1:
        return operation_split(data[1:-1])
    if data[0] == "-":
        return "-", "0", data[1:]
    binary_operators = ["+", "-", "*", "/", "^", ""]
    op = ""
    pos = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            i = bracket_closer_pos(data, i)
        if data[i] in binary_operators:
            if binary_operators.index(data[i]) < binary_operators.index(op):
                op = data[i]
                pos = i
        i += 1
    if op == "":
        return unary_operation_split(data)
    else:
        return op, data[:pos], data[pos + 1:]
