import string


def swapString(inputtedStringOne) -> string:
    result = ""
    for element in range(len(inputtedStringOne)):
        if element < 2:
            result += inputtedStringOne[element]
    return result


def gettingCharsApartFromTheFirstTwo(inputtedStringOne) -> string:
    result = ""
    for element in range(len(inputtedStringOne)):
        if element >= 2:
            result += inputtedStringOne[element]
    return result


def swap(inputtedStringOne, inputtedStringTwo):
    resultOne = swapString(inputtedStringOne)
    resultTwo = swapString(inputtedStringTwo)
    resultOne += gettingCharsApartFromTheFirstTwo(inputtedStringTwo)
    resultTwo += gettingCharsApartFromTheFirstTwo(inputtedStringOne)
    return resultTwo + " " + resultOne
