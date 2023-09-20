count = 0
add = 0
average = 0
for even in range(0, 51, 2):
    print(even, end=" ")
    add += even
    count = count + 1
    average = add / count
print()
print("SUM OF EVEN NUMBERS IS ", add)
print("AVERAGE IS ", average)

