from typing import Tuple


def addNumbers(*numbers):
    """
    enter the numbers you want to sum up
    after each number put coma [ , ]
    [user don"t be stupid!!!!!!!!]
    :param numbers you want to add together :
    :return the sum of the numbers :
    """
    total = 0
    for count in numbers:
        total += count
    return total


# print(addNumbers(5555))

def subtractNumber(firstNumber, seccondNumber):
    """ enter the numbers you want to subtract
    after each number put coma [ , ]
    [user don"t be stupid!!!!!!!!]

    :param numbers you want to subtract :
    :return the result of the subtraction:
    """
    subtract = firstNumber - seccondNumber
    if firstNumber < seccondNumber:
        return subtract
    return subtract


# print(subtractNumber(3, 1))


def maximum(*numbers):
    maxi = 0
    for count in numbers:
        if count > maxi:
            maxi = count
    return maxi

