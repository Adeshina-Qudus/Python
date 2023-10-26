from unittest import TestCase
from List_function import frequency_of_given_element


class Test(TestCase):
    def test_frequency_element(self):
        given_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7, ]
        given_value = 2
        self.assertEqual({1, 2, 5}, frequency_of_given_element.frequency_element(given_list, given_value))
