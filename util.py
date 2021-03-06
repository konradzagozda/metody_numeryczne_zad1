def horner(wielomian, n, x):
    result = wielomian[0]

    for i in range(1, n):
        result = result * x + wielomian[i]

    return result


# zaimplementowac wybor funkcji np switchem
def wybierz_funkcje(x, choice):
    pass


#
def styczna(a, b, eps, choice, variantchoice, iter):
    pass