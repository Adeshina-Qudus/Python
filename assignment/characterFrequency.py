def countChar(inputString):
    dictionary = {}
    counter = 0
    for value in inputString:
        for values in inputString:
            if value == values:
                counter += 1
        dictionary.update({value: counter})
        counter = 0
    return dictionary


print(countChar("semicolon.africa"))
