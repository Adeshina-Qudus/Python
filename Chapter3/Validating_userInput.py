passes = 0
failures = 0
student_counter = 1
while student_counter <= 10:
    result = int(input("ENTER RESULT (1=pass, 2=fail):"))
    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1
    else:
        print(" \t ENTER A CORRECT VALUE ")
        continue
    student_counter = student_counter + 1
print("PASSED", passes)
print("FAILURE", failures)
if passes > 8:
    print("BONUS TO THE INSTRUCTOR!!!")





