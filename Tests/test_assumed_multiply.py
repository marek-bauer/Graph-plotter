from unittest import TestCase


class TestAssumed_multiply(TestCase):
    def test_assumed_multiply(self):
        from StringPreparation import assumed_multiply
        x = assumed_multiply("2x")
        self.assertTrue(x == "2*x")
