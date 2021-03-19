import math
import built_in_functions
import numpy as np
import matplotlib.pyplot as plt

from util import szukaj_miejsc_zerowych_metoda_siecznych
from interface import get_params_from_user
from built_in_functions import *

# 1. niech uzytkownik wybierze funkcje (  wielomian, trygonometryczną, wykładniczą i ich złożenia. )
# 2. uzytkownik wybiera przedzial a - b poszukiwania miejsca zerowego
# 3. uzytkownik wybiera kryterium stopu ( dokladnosc lub liczba iteracji ) i podaje paramter ( epsilon lub liczba iteracji )
# 4. obydwie metody szukają miejsc zerowych
# 5. wyświetla wyniki
#   5.1 wyświetla współrzędne miejsc zerowych
#   5.2 rysowanie wykresu danej funkcji

while True:
    params = get_params_from_user()
    print(params)

    points_sieczne = szukaj_miejsc_zerowych_metoda_siecznych(params['a'], params['b'], params['stop'], params['stop-param'], params['func'])
    print(f"znalezione miejsce zerowe: {points_sieczne[len(points_sieczne) -1]}")
    print(f"liczba iteracji: {len(points_sieczne) - 2}")

    ##############################
    #todo:
    # miejsce na wywolanie metody
    ################################


    X = []
    Y = []
    step = 0.1
    a = params['a']
    b = params['b']
    while a < b:
        X.append(a)
        Y.append(params['func'](a))
        a += step

    X = np.array(X)
    Y = np.array(Y)

    plt.scatter(X, Y)
    X_sieczne = np.array([x.get_x() for x in points_sieczne])
    Y_sieczne = np.array([x.get_y() for x in points_sieczne])

    plt.scatter(X_sieczne, Y_sieczne, color="red")
    plt.show()

    ##############################
    #todo:
    # miejsce na dodanie punktow do wykresu ( opcjonalnie )
    ################################


