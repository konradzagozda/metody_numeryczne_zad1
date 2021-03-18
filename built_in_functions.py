import math


# wielomian to tablica wspolczynnikow od a_0 do a_n
def horner(wielomian, n, x):
    result = wielomian[0]

    for i in range(1, n):
        result = result * x + wielomian[i]

    return result

# x^2 - 3
def wielomian(x):
    return horner([1,0,-3], 3, x)

def sinus(x):
    return math.sin(x)

# 3^x - 2
def wykladnicza(x):
    return 3**x - 2

# 3^x * sin(x)
def zlozenie_wykladnicza_sinus(x):
    return wykladnicza(x) * sinus(x)

# (x^2 - 3) * sin(x)
def zlozenie_wielomian_sinus(x):
    return wielomian(x) * sinus(x)