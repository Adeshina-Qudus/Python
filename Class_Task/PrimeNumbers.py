def primenumbers(max):
    global isprime
    isprime[0] = False
    isprime[1] = False
    for number in range(2, max):
        isprime = True

    for n in range(2, max):
        if isprime[n] is True:
            for i in range(n ** 2, max, n):
                isprime[i] = False

    primeNumbers = []
    for p in range(2, max):
        if isprime[p] is True:
            primeNumbers.append(p)
            return primeNumbers


print(primenumbers(100))
