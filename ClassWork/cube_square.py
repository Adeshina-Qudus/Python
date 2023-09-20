print("number    Square     cube")
for number in range(1, 11):
    square_number = number * number
    cube_number = number * square_number

    print(f"{number} \t\t  {square_number}  \t\t   {cube_number}")

print("number   square       cube")
number = 1
while number <= 10:
    square_number = number * number
    cube_number = square_number * number
    print(f"{number}    \t   {square_number}     \t    {cube_number}")
    number = number + 1