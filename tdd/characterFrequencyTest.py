import unittest

from assignment import characterFrequency


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = "semicolon.africa"
        result = {'s': 1, "e": 1, "m": 1, "i ": 2, "c": 2, "o": 2, "l": 1, "n": 1, ".": 1, "a": 2, "f": 1, "r": 1}
        self.assertDictEqual(result, characterFrequency.countChar(input))  # add assertion here


if __name__ == '__main__':
    unittest.main()
