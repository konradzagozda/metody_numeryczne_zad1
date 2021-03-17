import math


def horner(wielomian, n, x):
    result = wielomian[0]

    for i in range(1, n):
        result = result * x + wielomian[i]

    return result

#todo
# x^2 - 3
def wielomian(x):
    pass

def sinus(x):
    return math.sin(x)

# 3^x - 2
def wykladnicza(x):
    pass

# 3^x * sin(x)
def zlozenie_wykladnicza_sinus(x):
    pass

# (x^2 - 3) * sin(x)
def zlozenie_wielomian_sinus(x):
    pass