def multiplyItSelf(inputted):
    result = []
    for count in inputted:
        if count != ",":
            result.append(int(count)*int(count))
    return result

