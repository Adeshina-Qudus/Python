from unittest import TestCase
from dictionary import two_lists_to_dictionary


class Test(TestCase):
    def test_two_list_to_dictionary(self):
        first_list = ['a', 'b', 'c']
        second_list = [1, 2, 3]
        self.assertEqual({'a': 1, 'b': 2, 'c': 3},
                         two_lists_to_dictionary.two_list_to_dictionary(first_list, second_list))
