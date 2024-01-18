def tuple_reverse(numbers):
    reverse = 0
    for count in numbers:
        for number in count:
            if count == number:
                reverse = count[::-1]
                return reverse


# def nested_tuple(numbers):
#     total = 0
#     for count in numbers:
#         if count == numbers[0][1] and count == numbers[1][2]:
#     return None