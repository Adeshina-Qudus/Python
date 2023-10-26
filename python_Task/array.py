def list_odd(numbers):
    bigOdd = []
    odd = numbers[0]
    for count in numbers:
        bigOdd.append(count)
    return bigOdd


def biggest_odd(numbers):
    number = list_odd(numbers)
    largest: int = numbers[0]
    for count in number:
        if int(count) % 2 != 0:
            if count > largest:
                largest = count
    return largest


numbers = "23569"
highest = filter(lambda count: int(count) % 2 != 0 and count > numbers[3], numbers)
print(highest)

print(biggest_odd(numbers))
