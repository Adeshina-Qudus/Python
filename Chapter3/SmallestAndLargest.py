count = 0
largest = 0
smallest = 0
average = 0
for loop in range(1, 5):
    userInput = int(input("ENTER AN INTEGER : "))
    smallest = userInput
    largest = userInput
    count = count + 1
    if userInput < smallest:
        smallest = userInput
    else:
        largest = userInput
print(smallest)
print(largest)



