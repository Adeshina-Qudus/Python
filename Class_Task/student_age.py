def student_age_function():
    student_age = {"dike": 33,
                   "ope": 25,
                   "melody": 20,
                   "precious": 27
                   }
    for index, value in student_age.items():
        name = input("enter your name ").lower()
        if name in index:
            return f"Hi,{name}, you are {value} years old"
        elif name is not index:
            print("your name is not in the dictionary ")
            age = input("enter your age ")
            student_age.update({name: age})
            print(f"Hi,{name}, you are {age} years old")
            return student_age



print(student_age_function())
