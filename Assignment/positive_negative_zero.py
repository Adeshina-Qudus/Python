number = int(input("ENTER A NUMBER 0R [-2] TO QUIT : "))
positive_number = number
negative_number = number
zero_number = number
count = 0

while number != -2:

    number = int(input("ENTER A NUMBER 0R [-2] TO QUIT : "))

    if number > 0:
        positive_number = number
    if number < 0:
        negative_number = number
    if number == 0:
        zero_number = number

print("THE NUMBER OF POSITIVE NUMBERS ENTERED IS : ", positive_number)
print("THE NUMBER OF NEGATIVE NUMBERS ENTERED IS : ", negative_number)
print("THE NUMBER OF ZERO NUMBERS ENTERED IS : ", zero_number)
