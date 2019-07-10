from unittest import TestCase


class TestOperationSplit(TestCase):
    def test_operation_split(self):
        from StringToLambda import operation_split
        op, left, right = operation_split("32")
        self.assertTrue(op == "" and left == "32" and right == "")
        op, left, right = operation_split("-x")
        self.assertTrue(op == "-" and left == "0" and right == "x")
        op, left, right = operation_split("log 3 2")
        self.assertTrue(op == "log" and left == "3" and right == "2")
        op, left, right = operation_split("(ln e)")
        self.assertTrue(op == "ln" and left == "e" and right == "")
        op, left, right = operation_split("2+2*2")
        self.assertTrue(op == "+" and left == "2" and right == "2*2")
        op, left, right = operation_split("2^2+1")
        self.assertTrue(op == "+" and left == "2^2" and right == "1")
        op, left, right = operation_split("(3+1)*(2+1)")
        self.assertTrue(op == "*" and left == "(3+1)" and right == "(2+1)")
        op, left, right = operation_split("3^(2*x)")
        self.assertTrue(op == "^" and left == "3" and right == "(2*x)")
