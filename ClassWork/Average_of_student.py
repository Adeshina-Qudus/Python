number = 0
total = 0
userInput = int(input("ENTER A SCORE : "))
while userInput != -2:
    total += userInput
    number += 1
    userInput = int(input("ENTER A SCORE : "))
average = total / number
print(" ")
print("TOTAL SCORE IS : ", total)
print(" ")
print("TOTAL AVERAGE IS : ", average)