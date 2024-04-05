import unittest
from Class_Task import returnList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = "2,3,5"
        self.assertEqual([4, 9, 25], returnList.multiplyItSelf(input))
