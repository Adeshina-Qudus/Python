user_input = int(input("ENTER INTEGER BETWEEN 0 AND 1000: "))
first_number = user_input // 100
second_number = user_input // 10 % 10
third_number = user_input % 10
sum = first_number + second_number + third_number
print("THE SUM OF DIGIT IS : ", sum)
