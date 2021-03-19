import math

from enum import Enum

# wielomian to lista wspolczynnikow, n to liczba wyrazow wielomianu (stopien + 1), x to x
def horner(wielomian, n, x):
    result = wielomian[0]

    for i in range(1, n):
        result = result * x + wielomian[i]

    return result


# x^2 - 3
def wielomian(x):
    return horner([1, 0, -3], 3, x)


def sinus(x):
    return math.sin(x)


# 3^x - 2
def wykladnicza(x):
    return 3 ** x - 2


# 3^x * sin(x)
def zlozenie_wykladnicza_sinus(x):
    return wykladnicza(x) * sinus(x)


# (x^2 - 3) * sin(x)
def zlozenie_wielomian_sinus(x):
    return wielomian(x) * sinus(x)


class Functions(Enum):
    WIELOMIAN = wielomian
    SINUS = sinus
    WYKLADNICZA = wykladnicza
    WIEL_SIN = zlozenie_wielomian_sinus
    WYKL_SIN = zlozenie_wykladnicza_sinus
