def list_created():
    myList = []
    for number in range(1, 21):
        myList.append(number)
    return myList


def odd_numbers_in_list():
    odd_num = []
    odd_list = list_created()
    for element in odd_list:
        if element % 2 != 0:
            odd_num.append(element)
    return odd_num


def double_item_in_list():
    doubleElementList = []
    double_Element = odd_numbers_in_list()
    for element in double_Element:
        doubleElementList.append(element * 2)
    return doubleElementList


print(double_item_in_list())


def changeElement():
    change = []
    change_element = double_item_in_list()
    for element in change_element:
        element[4:7] = 0
        change.append(element)
    return change


print(changeElement())


def concatenate(list1, list2):
    return list1 + list2 zip list1
    return None