import random

userInput = int(input("ENTER A NUMBER BETWEEN 1 TO 10 : "))
number = random.randint(1, 10)
print(number)
if userInput == number:
    print("CORRECT!!!!!!!")
else:
    while userInput != number:
        userInput = int(input("ENTER A NUMBER BETWEEN 1 TO 10 : "))
        number = random.randint(1, 10)
        print(number)
        if userInput == number:
            print("CORRECT!!!!!!!")
