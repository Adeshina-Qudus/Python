import unittest
from Class_Task import addIngToAString


class MyTestCase(unittest.TestCase):
    def test_thatAStringEndWithIngAddLy(self):
        sample_input = "sting"
        self.assertEqual("stingly", addIngToAString.endWithIngAddLy(sample_input))


if __name__ == '__main__':
    unittest.main()
