def sum_nested_list(numbers):
    sum_of_element = 0
    for index in numbers:
        for num in index:
            sum_of_element += num

    return sum_of_element


print(sum_nested_list([[2, 4, 5, 6], [2, 3, 5, 6]]))


def sum_list(numbers):
    total = 0
    for value in numbers:
        total += sum(value)
    return total


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))


# def sum_list_numbers(numbersList):
#     listOne, *listTwo = numbersList
#     result = sum(listOne) + sum(listTwo)
#     return result
#
# 
# print(sum_list_numbers([[2, 4, 5, 6], [2, 3, 5, 6]]))
