def two_list_to_dictionary(first_list: list, second_list: list):
    return dict(zip(first_list, second_list))


print(two_list_to_dictionary(['a', 'b', 'c'], [1, 2, 3]))
