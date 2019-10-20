from unittest import TestCase
from StringToLambda import unary_operation_split


class TestUnaryOperationSplit(TestCase):
    def test_basic(self):
        op, left, right = unary_operation_split("32")
        self.assertTrue(op == "number" and left == "32" and right == "")
        op, left, right = unary_operation_split("log (3) 2")
        self.assertTrue(op == "log" and left == "(3)" and right == "2")
        op, left, right = unary_operation_split("ln e")
        self.assertTrue(op == "ln" and left == "e" and right == "")

    def test_trigonometry(self):
        op, left, right = unary_operation_split("cos32")
        self.assertTrue(op == "cos" and left == "32" and right == "")
        op, left, right = unary_operation_split("sin(cos43)")
        self.assertTrue(op == "sin" and left == "(cos43)" and right == "")
        op, left, right = unary_operation_split("tg(43)")
        self.assertTrue(op == "tg" and left == "43" and right == "")
        op, left, right = unary_operation_split("arcsin(sin30)")
        self.assertTrue(op == "arcsin" and left == "(sin30)" and right == "")
        op, left, right = unary_operation_split("arccos(((5)))")
        self.assertTrue(op == "arccos" and left == "(((5)))" and right == "")
        op, left, right = unary_operation_split("arctg0")
        self.assertTrue(op == "arctg" and left == "0" and right == "")
