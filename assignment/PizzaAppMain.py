from assignment import PizzaApp
totalBox = 0
totalSlices = 0
haveLeft = 0
price = 0
print("""
          ***********************************************
          *      WHAT SIZE OF PIZZA YOU WANT TO GET ?   *
          *      FOR BIG SIZE [ENTER : LARGE]           *
          *      FOR MEDIUM SIZE [ENTER : MEDIUM]       *
          *      FOR SMALL SIZE [ENTER : SMALL]         *
          ***********************************************
                """)
userInput = input().upper()
while (userInput != "LARGE") and (userInput != "MEDIUM") and (userInput != "SMALL"):
        print("ENTER A VALID SIZE OF PIZZA )> ")
        userInput = input().upper()
print("HOW MANY HUNGRY PEOPLE ")
hungry = input()
print("HOW MANY SEMI-HUNGRY PEOPLE ")
semiHungry = input()
print("HOW MANY CLASSIC PEOPLE ")
classic = input()
if userInput == "LARGE":
        totalSlices = PizzaApp.totalSlices(hungry, semiHungry, classic)
        totalBox = PizzaApp.recommendLargestSize(hungry, semiHungry, classic)
        haveLeft = PizzaApp.largePizzaSlicesLeft(totalSlices, totalBox)
        price = PizzaApp.largePizzaAmountRecommended(totalBox)
        print("total slices " + totalSlices)
        print("have left " + haveLeft)
        print("total box " + totalBox)
        print("price " + price)
if userInput == "MEDIUM":
        totalSlices = PizzaApp.totalSlices(hungry, semiHungry, classic)
        totalBox = PizzaApp.recommendMediumSize(hungry, semiHungry, classic)
        haveLeft = PizzaApp.mediumPizzaSlicesLeft(totalSlices, totalBox)
        price = PizzaApp.mediumPizzaAmountRecommended(totalBox)
        print("total slices " + totalSlices)
        print("have left " + haveLeft)
        print("total box " + totalBox)
        print("price " + price)
if userInput == "SMALL":
        totalSlices = PizzaApp.totalSlices(hungry, semiHungry, classic)
        totalBox = PizzaApp.recommendSmallSize(hungry, semiHungry, classic)
        haveLeft = PizzaApp.smallPizzaSlicesLeft(totalSlices, totalBox)
        price = PizzaApp.smallPizzaAmountRecommended(totalBox)
        print("total slices " + totalSlices)
        print("total box " + totalBox)
        print("price " + price)


