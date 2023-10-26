from unittest import TestCase
from python_Task import array


class Test(TestCase):
    def test_biggest_odd(self):
        number = '23569'
        numbers = array.biggest_odd(number)
        self.assertEqual(numbers, "9")
