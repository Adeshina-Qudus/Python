names = [" ", "joy", "udeme", "ender"]
# print(names.index("joy"))
# print(any(names))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]


def my_index(li: list, n):
    idx = 0
    for count in range(len(li)):
        if li[count] == n:
            idx = count
        break
    return idx


# print(my_index(numbers, 3))
# print(sorted(numbers))


result = [count for count in range(6, 9) if count % 2 == 0]
print(result)
