from unittest import TestCase


def sum_numbers_forloop(numbers):
    result = 0
    for count in numbers:
        result += count
    return result


class TestSumForLoop(TestCase):
    def test_sum_numbers_forloop(self):
        numbers = sum_numbers_forloop([1, 4, 5, 20])
        self.assertEqual(numbers, 30)
        numbers = sum_numbers_forloop([56, 98, 100, 23])
        self.assertEqual(numbers, 277)


def sum_numbers_whileloop(numbers):
    total = 0
    count = 0

    while count < len(numbers):
        total += numbers[count]
        count += 1
    return total


class TestSumWhileLoop(TestCase):
    def test_sum_numbers_whileloop(self):
        numbers = sum_numbers_whileloop([1, 4, 5])
        self.assertEqual(numbers, 10)


def reverseList(reverselist):
    return reverselist[:: -1]


class TestReverseList(TestCase):
    def test_reverse_list(self):
        number = reverseList([1, 2, 3, 4, 5])
        self.assertEqual(number, [5, 4, 3, 2, 1])


def largest_element(element):
    largest = element[0]

    for count in element:
        if element[count] > largest:
            largest = element[count]
            count += 1

    return largest


class TestLargestElement(TestCase):
    def test_largest_element(self):
        numbers = largest_element([23, 67, 98, 1])
        self.assertEqual(numbers, [98])


def oddly_places(numbers):
    length = len(numbers)
    even = numbers[1:length:2]
    return even


class TestEvenPosition(TestCase):
    def test_odd_position_number(self):
        numbers = oddly_places([1, 3, 2, 5, 67, 34])
        self.assertEqual(numbers, [3, 5, 34, ])


def ifElementOccurs(numbers, element):
    if numbers == element:
        return True
    else:
        return False


class TestIfAnElementOccurs(TestCase):
    def testIfAnElementOccurs(self, element):
        element = 5
        numbers = ifElementOccurs([5, 87, 468, 98, 35], element)
        self.assertTrue(numbers, element)
