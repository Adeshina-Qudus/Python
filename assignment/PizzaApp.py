class PizzaApp:
    largePizzaPrice = 5000
    mediumPizzaPrice = 3000
    smallPizzaPrice = 1200
    largeSlices = 10
    mediumSlices = 6
    smallSlices = 4
    hungryPerson = 4
    semiHungryPerson = 2
    classicPerson = 1


def totalSlices(hungry, semiHungry, classic):
    hungryTotal = hungry * PizzaApp.hungryPerson
    semiHungryTotal = semiHungry * PizzaApp.semiHungryPerson
    classicTotal = classic * PizzaApp.classicPerson
    return hungryTotal + semiHungryTotal + classicTotal


def recommendLargestSize(hungry, semiHungry, classic):
    totalSlice = totalSlices(hungry, semiHungry, classic)
    totalBox = totalSlice // PizzaApp.largeSlices
    if totalSlice % PizzaApp.largeSlices != 0:
        totalBox += 1
    return totalBox


def recommendMediumSize(hungry, semiHungry, classic):
    totalSlice = totalSlices(hungry, semiHungry, classic)
    totalBox = totalSlice // PizzaApp.mediumSlices
    if totalSlice % PizzaApp.mediumSlices != 0:
        totalBox += 1
    return totalBox


def recommendSmallSize(hungry, semiHungry, classic):
    totalSlice = totalSlices(hungry, semiHungry, classic)
    totalBox = totalSlice // PizzaApp.smallSlices
    if totalSlice % PizzaApp.smallSlices != 0:
        totalBox += 1
    return totalBox


def largePizzaSlicesLeft(Slices, totalBox):
    totalBoxSlice = totalBox * PizzaApp.largeSlices
    return totalBoxSlice - Slices


def mediumPizzaSlicesLeft(slices, totalBox):
    totalBoxSlice = totalBox * PizzaApp.mediumSlices
    return totalBoxSlice - slices


def smallPizzaSlicesLeft(allSlices, totalBox):
    totalBoxSlice = totalBox * PizzaApp.smallSlices
    return totalBoxSlice - allSlices


def largePizzaAmountRecommended(totalBox):
    return totalBox * PizzaApp.largePizzaPrice


def mediumPizzaAmountRecommended(totalBox):
    return totalBox * PizzaApp.mediumPizzaPrice


def smallPizzaAmountRecommended(totalBox):
    return totalBox * PizzaApp.smallPizzaPrice