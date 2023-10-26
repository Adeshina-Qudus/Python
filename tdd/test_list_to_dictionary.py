from unittest import TestCase
from assignment import list_to_dictionary


class Test(TestCase):
    def test_list_to_dictionary(self):
        sample_input = ["apple", "banana", "coconut", "corn"]
        self.assertEqual({'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'},
                         list_to_dictionary.list_to_dictionary(sample_input))
