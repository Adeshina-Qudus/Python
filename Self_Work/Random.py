import random
numbers = int(input())
number2 = int(input())
count = 0
while count < number2:
    print(count, random.randint(numbers, number2))
    count += 1
