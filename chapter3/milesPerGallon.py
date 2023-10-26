average = 0
overall_Average = 0
gallon_used = 0
count = 0
overAvg = 0
divide = 0
while gallon_used != -1:
    gallon_used = float(input("Enter the gallons used (-1 to end): "))
    miles_driven = float(input("Enter the miles driven: "))
    average = miles_driven / gallon_used
    print(average)
    overall_Average += average
    count += 1
divide = count / overall_Average
print(overall_Average)
print(count)
print(divide)
