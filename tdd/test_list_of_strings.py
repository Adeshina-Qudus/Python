from unittest import TestCase
from List_function import list_of_strings


class Test(TestCase):
    def test_remove_multiple_empty_strings(self):
        list_strings = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        self.assertEqual(['ABC', 'xyz', 'abc', 'XYZ'], list_of_strings.remove_multiple_empty_strings(list_strings))
