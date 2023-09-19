five_digit = int(input("ENTER FIVE DIGIT INTEGERS : "))
first_digit = five_digit // 10000 % 1000
second_digit = five_digit // 1000 % 100
third_digit = five_digit // 100 % 10
fourth_digit = five_digit // 10 % 10
fifth_digit = five_digit % 10

if first_digit == fifth_digit:
    print(five_digit, "IS A PALINDROME ")
else:
    print(five_digit, "IS NOT A PALINDROME ")