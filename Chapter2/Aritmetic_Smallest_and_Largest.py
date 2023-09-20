user_Firstinput = int(input("ENTER A NUMBER:"))
user_Secondinput = int(input("ENTER A NUMBER:"))
user_Thirdinput = int(input("ENTER A NUMBER:"))

print("SUM OF THE THREE NUMBERS IS :", user_Firstinput+user_Secondinput+user_Thirdinput)
print("THE AVERAGE OF THE THREE NUMBERS IS :", user_Firstinput+user_Secondinput+user_Thirdinput / 3)
print("THE PRODUCT OF THE THREE NUMBERS IS :", user_Firstinput*user_Secondinput*user_Thirdinput)

if user_Firstinput < user_Secondinput and user_Firstinput < user_Thirdinput:
      print(user_Firstinput, " IS THE SMALLEST NUMBER")

elif user_Secondinput < user_Firstinput and user_Secondinput < user_Thirdinput:
      print(user_Secondinput, "IS THE SMALLEST NUMBER ")
else:
    print(user_Thirdinput, "IS THE SMALLEST NUMBER ")

if user_Firstinput > user_Secondinput and user_Firstinput > user_Thirdinput:
    print(user_Firstinput, " IS THE LARGEST NUMBER")

elif user_Secondinput > user_Firstinput and user_Secondinput > user_Thirdinput:
    print(user_Secondinput, "IS THE LARGEST NUMBER ")

else:
    print(user_Thirdinput, "IS THE LARGEST NUMBER ")

