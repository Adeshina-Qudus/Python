
def your_salary():
    result = 0
    secondResult = 0
    total = 0
    sub = 0
    teachers_name = input("Enter teacher name ")
    periods = int(input("Enter number of period taught in a month "))
    if periods <= 100:
        result += periods * 20
        total = result
    if periods > 100:
        sub += periods - 100
        result += 100 * 20
        secondResult += sub * 25
        total = result + secondResult
        print("Teacher : ", teachers_name)
        print("period : ", periods)
        print("Gross salary : ", total)
    return total



print(your_salary())