from unittest import TestCase
from List_function import difference_between_smallest_and_largest


class Test(TestCase):
    def test_difference_smallest_largest(self):
        numbers = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(70, difference_between_smallest_and_largest.difference_smallest_largest(numbers))
