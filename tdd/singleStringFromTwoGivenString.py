import unittest

from Class_Task import singleStringFromTwoGivenString


class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputtedStringOne = "abc"
        inputtedStringTwo = "xyz"
        self.assertEqual("xyc abz", singleStringFromTwoGivenString.swap(inputtedStringOne,
                                                                        inputtedStringTwo))  # add assertion here
