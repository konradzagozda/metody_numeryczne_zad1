def horner(wielomian, n, x):
    result = wielomian[0]

    for i in range(1, n):
        result = result * x + wielomian[i]

    return result

#todo
def styczna():
    pass

#todo
def sieczna():
    pass