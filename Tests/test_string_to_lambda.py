from unittest import TestCase

import math


def fn_comp(f, g):
    for i in range(2, 1000):
        if f(i) != g(i) or f(1.0 / i) != g(1.0 / i):
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
        self.assertTrue(fn_comp(f, lambda x: abs(x+abs(-x))))