even = 0
odd = 0
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        even = even+1
    else:
        odd = odd+1
num = "[1,2,3,4,5,6,7,8,9]"
print(f"Sample numbers : numbers =  {num} ","\n" "Expected Output :", "\n",f"Number of even numbers : {even}", "\n" f"Number of odd numbers : {odd}" )

