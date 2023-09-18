count = 1
number = 1
while count <= 3000:
    number *= 6
    count += 6
    if number >= 3000:
        break
    print(number, end=" ")
