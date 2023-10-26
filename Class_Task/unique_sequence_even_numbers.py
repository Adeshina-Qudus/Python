def unique_even_numbers(numbers):
    unique_element = []
    for number in set(numbers):
        if number % 2 == 0:
            unique_element.append(number)
    return unique_element


print(unique_even_numbers([1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]))
