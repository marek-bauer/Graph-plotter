from unittest import TestCase

import math


def same_res(f, g, x):
    try:
        a = f(x)
    except:
        try:
            b = g(x)
        except:
            return True
        else:
            return a == b
    else:
        try:
            b = g(x)
        except:
            return False
        else:
            return a == b


def fn_comp(f, g):
    for i in range(1, 1000):

        if not same_res(f, g, i) or not same_res(f, g, 1.0 / i):
            return False
    return True


class TestString_to_lambda(TestCase):
    def test_simple_test(self):
        from StringToLambda import string_to_lambda
        f = string_to_lambda("x")
        self.assertTrue(fn_comp(f, lambda x: x))
        f = string_to_lambda("x^2")
        self.assertTrue(fn_comp(f, lambda x: x * x))
        f = string_to_lambda("sinx")
        self.assertTrue(fn_comp(f, lambda x: math.sin(x)))
        f = string_to_lambda("2^(x+1)")
        self.assertTrue(fn_comp(f, lambda x: math.pow(2, x + 1)))
        f = string_to_lambda("2 + 2x")
        self.assertTrue(fn_comp(f, lambda x: 2 + 2 * x))
        f = string_to_lambda("log x     3")
        self.assertTrue(fn_comp(f, lambda x: math.log(3, x)))
        f = string_to_lambda("|x+|-x||")
        self.assertTrue(fn_comp(f, lambda x: abs(x + abs(-x))))
        f = string_to_lambda("log (3x) 4")
        self.assertTrue(fn_comp(f, lambda x: math.log(4, 3 * x)))
        f = string_to_lambda("(2x)^(x+8)")
        self.assertTrue(fn_comp(f, lambda x: math.pow(2 * x, x + 8)))
