from unittest import TestCase


class TestBracketCloserPos(TestCase):
    def test_bracket_closer_pos(self):
        from StringToLambda import bracket_closer_pos
        self.assertTrue(bracket_closer_pos("()", 0) == 1)
        self.assertTrue(bracket_closer_pos("(())", 0) == 3)
        self.assertTrue(bracket_closer_pos("(())", 1) == 2)
        self.assertTrue(bracket_closer_pos("((aaa))", 1) == 5)
        self.assertTrue(bracket_closer_pos("((aaa)()())", 6) == 7)
        try:
            bracket_closer_pos("(((adsa)())", 0)
        except ValueError:
            pass
