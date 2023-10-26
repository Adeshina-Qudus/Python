
def difference_smallest_largest(numbers : list):
    smallest = numbers[0]
    largest = 0
    for count in numbers:
        if count < smallest:
            smallest = count

        if count > largest:
            largest = count
    return largest - smallest

