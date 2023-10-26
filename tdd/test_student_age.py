from unittest import TestCase
from Class_Task import student_age


class Test(TestCase):
    def test_student_age_function(self):
        self.assertTrue(student_age.student_age_function())
