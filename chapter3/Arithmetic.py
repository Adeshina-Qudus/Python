smallest = 0
largest = 0
total_sum = 0
average = 0
number = 0
for number in range(4):
    number += 1
    userInput = int(input("ENTER A NUMBER "))
    if number == 0:
        smallest = userInput
        largest = userInput
    else:
        if userInput < smallest:
            smallest = userInput
            total_sum += userInput
        if userInput > largest:
            largest = userInput
            total_sum += userInput
average = total_sum / number
print(total_sum)
print(average)
print(largest)
print(smallest)
