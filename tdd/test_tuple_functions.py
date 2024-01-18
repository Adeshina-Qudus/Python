from unittest import TestCase

from assignment.tuple_task import tuple_functions


class tupleFunction(TestCase):
    def test_that_tuple_can_reverse(self):
        numbers_tuple = tuple_functions.tuple_reverse((10, 20, 30, 40, 50), )
        self.assertEqual(numbers_tuple, (50, 40, 30, 20, 10), )

    def test_return_a_nested_tuple(self):
        numbers_tuple = tuple_functions.nested_tuple(("Orange", [10, 20, 30], (5, 15, 25)))
        self.assertEqual(numbers_tuple, ((0, 20), (1, 25)))
