from unittest import TestCase
from Class_Task import unique_sequence_even_numbers


class Test(TestCase):
    def test_unique_even_numbers(self):
        numbers = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
        result = [2, 4, 6, 8, 10, 12, 14]
        self.assertEqual(unique_sequence_even_numbers.unique_even_numbers(numbers),result)
