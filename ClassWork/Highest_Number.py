first_userInput = int(input("enter first number "))
second_userInput = int(input("enter second number "))
third_userInput = int(input("enter third number "))

if first_userInput > second_userInput and first_userInput > third_userInput:
    print(first_userInput, "is the highest number ")

elif second_userInput > first_userInput and second_userInput > third_userInput:
    print(second_userInput, "is the highest number")

else:
    print(third_userInput, "is the highest number")
