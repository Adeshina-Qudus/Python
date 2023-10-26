from unittest import TestCase
from Class_Task import list


class GroupTest(TestCase):
    def test_That_A_list_Can_be_created_with_numbers(self):
        my_list = list.list_created()
        self.assertEqual(my_list, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_the_odd_numbers_in_the_list(self):
        my_list = list.odd_numbers_in_list()
        self.assertEqual(my_list, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_that_all_item_in_list_can_double(self):
        my_list = list.double_item_in_list()
        self.assertEqual(my_list, [2, 6, 10, 14, 18, 22, 26, 30, 34, 38])

    def test_that_item_can_change(self):
        my_list = list.changeElement()
        self.assertEqual(my_list, [2, 6, 10, 14, 0, 0, 0, 0, 34, 38])

    def test_function_can_concatenate_two_list(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e' , 'rers']
        list3 = ['we', 'are' , 'the' , 'xplorers']
        self.assertEqual(list.concatenate(list1,list2,),list3)
