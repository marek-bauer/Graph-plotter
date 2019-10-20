from StringToLambda import *

derivatives = {
    "ln": lambda x: 1 / x,
    # "abs": lambda a, b: abs(a),
    "sin": lambda x: -math.cos(x),
    "cos": lambda x: math.sin(x),
    "tg": lambda x: 1 / math.cos(x) ** 2,
    "ctg": lambda x: -1 / math.sin(x) ** 2,
    "arcsin": lambda x: 1 / (1 - x ** 2) ** 1 / 2,
    "arccos": lambda x: -1 / (1 - x ** 2) ** 1 / 2,
    "arctg": lambda x: 1 / 1 + x ** 2,
}


def string_to_derivative(string: str):
    from StringPreparation import prepare
    s = prepare(string)
    r, t = anc_string_to_derivative(s)
    return r


def anc_string_to_derivative(string: str):
    if string == "":
        return lambda x: 0, True
    op, left, right = operation_split(string)
    if op == "number":
        return lambda x: 0, True
    if op == "x":
        return lambda x: 1, True
    d_f, d_f_is_const = anc_string_to_derivative(left)
    d_g, d_g_is_const = anc_string_to_derivative(left)
    if op == "+":
        if d_f_is_const:
            if d_g_is_const:
                t = d_f(0) + d_g(0)
                return lambda x: t, True
            else:
                t = d_f(0)
                if t != 0:
                    return lambda x: t + d_g(0), False
                else:
                    return lambda x: d_g(0), False
        if d_g_is_const:
            t = d_g(0)
            if t != 0:
                return lambda x: t + d_f(0), False
            else:
                return lambda x: d_f(0), False
        else:
            return lambda x: d_f(x) + d_g(x), False
    if op == "-":
        if d_f_is_const:
            if d_g_is_const:
                t = d_f(0) - d_g(0)
                return lambda x: t, True
            else:
                t = d_f(0)
                return lambda x: t - d_g(0), False
        if d_g_is_const:
            t = d_g(0)
            return lambda x: t - d_f(0), False
        else:
            return lambda x: d_f(x) - d_g(x), False
    f, f_is_const = anc_string_to_lambda(left)
    g, g_is_const = anc_string_to_lambda(right)
    if op == "*":
        if f_is_const:
            if g_is_const:
                return lambda x: 0, True
            else:
                t = f(0)
                if t != 0:
                    return lambda x: t * d_g(x), d_g_is_const
                else:
                    return lambda x: 0, True
        else:
            if g_is_const:
                t = g(0)
                if t != 0:
                    return lambda x: t * d_f(x), d_f_is_const
                else:
                    return lambda x: 0, True
            else:
                return lambda x: d_f(x) * g(x) + f(x) * d_g(x), False
    if op == "/":
        return lambda x: (d_f(x) * g(x) - f(x) * d_g(x)) / g(x) ** 2, f_is_const and g_is_const
    if op == "^":
        if f_is_const:
            if g_is_const:
                return lambda x: 0, True
            else:
                t = f(0)
                l = math.log(t)
                return lambda x: l * t ** g(x) * d_g(x), False
        else:
            if g_is_const:
                t = g(0)
                return lambda x: t * f(x) ** (t - 1), False
            else:
                return lambda x: (f(x) ** g(x)) * (d_g(x) * math.log(f(x)) + g(x) * d_f(x) / f(x)), False

    if op == "log":
        return lambda x: d_g(x) / (g(x) * math.log(f(x))) - math.log(g(x)) * d_f(x) / (
                (math.log(f(x))) ** 2 * f(x)), f_is_const and g_is_const
    if op == "abs":
        return lambda x: d_f(x) if f(x) >= 0 else -d_f(x), f_is_const
    if f_is_const is False:
        der = derivatives.get(op)
        d_f, d_f_is_const = anc_string_to_derivative(left)
        if d_f_is_const is False:
            return lambda x: der(f(x)) * d_f(x), False
        else:
            temp = d_f(0)
            return lambda x: der(f(x)) * temp, False
    else:
        return lambda x: 0, True
