number = int(input("ENTER A NUMBER OR PRESS [-1] TO QUITE : "))
smallest = number
largest = number


while number != -1:

   if number < smallest:
         smallest = number

   if number > largest:
          largest = number

   number = int(input("ENTER A NUMBER OR PRESS [-1] TO QUITE : "))



print("THE SMALLEST NUMBER YOU ENTERED IS : ", smallest)
print("THE LARGEST NUMBER YOU ENTERED IS : ", largest)


