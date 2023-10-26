import unittest
from unittest import TestCase

def triple_numbers(numbers_list):
    num_list = []
    for loop in numbers_list:
        num_list.append(loop ** 3)
    return num_list


class MyTestCase(TestCase):
    def test_Triple_numbers_in_list(self):
        numbers = triple_numbers([3, 7, 2, 6, 5])
        self.assertEqual(numbers, [27, 343, 8, 216,125])  # add assertion here


if __name__ == '__main__':
    unittest.main()
