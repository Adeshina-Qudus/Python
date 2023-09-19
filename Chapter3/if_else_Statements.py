print("ENTER TWO INTEGERS, AND I WILL TELL YOU ,"
      "THE RELATIONSHIP THEY SATISFY.")
first_number = int(input("ENTER FIRST INTEGER : "))
second_number = int(input("ENTER SECOND INTEGER : "))
if first_number == second_number:
    print(first_number, "is equal to ", second_number)
else:
    print(first_number, "is not equal to ", second_number)
if first_number < second_number:
    print(first_number, "is less than ", second_number)
else:
    print(first_number, "is greater than ", second_number)
if first_number <= second_number:
    print(first_number, "is less or equal to ", second_number)
else:
    print(first_number, "is greater or equal to ", second_number)

