from unittest import TestCase


def fn_comp(f, g):
    for i in range(1, 1000):
        if f(i) != g(i) or f(1.0/i) != g(1.0/i):
            return False
    return True


class TestString_to_lambda(TestCase):
    def test_simple_test(self):
        from StringToLambda import string_to_lambda
        f = string_to_lambda("x");
        self.assertTrue(fn_comp(f, lambda x: x))
        f = string_to_lambda("x^2");
        x = f(1)
        y = f(2)
        self.assertTrue(fn_comp(f, lambda x: x*x))
