def ifElementOccurs(numbers, element):
    for count in numbers:
        if count == element:
            return True
        else:
            return False

print(ifElementOccurs([7,3,8,3],17))