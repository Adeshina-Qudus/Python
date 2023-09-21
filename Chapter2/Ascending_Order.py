first_number = float(input("ENTER A DECIMAL NUMBER : "))
second_number = float(input("ENTER A DECIMAL NUMBER : "))
third_number = float(input("ENTER A DECIMAL NUMBER : "))

if first_number <= second_number and first_number <= third_number:
    smallest = first_number
    if second_number <= third_number:
        middle = second_number
        largest = third_number
    else:
        middle = third_number
        largest = second_number

elif second_number <= first_number and second_number <= third_number:
    smallest = second_number
    if first_number <= third_number:
        middle = first_number
        largest = third_number
    else:
        middle = third_number
        largest = first_number
else:
    smallest = third_number
    if first_number <= second_number:
        middle = first_number
        largest = second_number
    else:
        middle = second_number
        largest = first_number

print()
print(f"{smallest} , IS THE SMALLEST NUMBER ")
print(f"{middle} , IS THE MIDDLE NUMBER")
print(f"{largest} , IS THE BIGGEST NUMBER")

#use one print statement
