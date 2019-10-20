from unittest import TestCase

from Tests.test_string_to_lambda import fn_comp


class TestStringToDerivative(TestCase):
    def test_string_to_derivative(self):
        from Derivative import string_to_derivative
        d = string_to_derivative("x")
        assert fn_comp(d, lambda x: 1)
        d = string_to_derivative("x^4")
        x = d(0)
        x = d(1)
        assert fn_comp(d, lambda x: 4*x**3)
