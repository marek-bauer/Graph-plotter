from unittest import TestCase


class TestCharacteristicValues(TestCase):
    def test_characteristic_values(self):
        from Graph import characteristic_values
        x = characteristic_values(0.001, 10.0001, 4)
        assert (x == [2, 4, 6, 8])
        x = characteristic_values(3.14, 3.15, 3)
        x = characteristic_values(100, 1000, 9)
        pass
