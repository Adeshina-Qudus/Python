import random
from string import ascii_lowercase, ascii_letters, punctuation, ascii_uppercase


def cardLength(digit):
    if len(digit) < 13 or len(digit) > 16:
        return 0
    return len(digit)


def visaCardFirstDigit(digit):
    for count in digit:
        return count[1]


# print(visaCardFirstDigit("4235678876432"))

array = []

for count in range(2):
    for count in range(3):
        array.append(2)

print(array)