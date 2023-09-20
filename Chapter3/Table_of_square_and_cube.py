print("number   square       cube")
number = 0
while number <= 5:
    square_number = number * number
    cube_number = square_number * number
    print(f"{number:5}    \t{square_number:>3}    \t {cube_number:>3}")
    number = number + 1