def multiplyItSelf(inputted):
    result = []
    for element in inputted:
        if element != ",": result.append(int(element) * int(element))
    return result
