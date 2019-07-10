from unittest import TestCase


class TestAbs_replace(TestCase):
    def test_abs_replace(self):
        from StringPreparation import abs_replace
        x = abs_replace("|x|")
        self.assertTrue(x == "abs(x)")
        x = abs_replace("||x|+|x||")
        self.assertTrue(x == "abs(abs(x)+abs(x))")
