import math

from util import szukaj_miejsc_zerowych_metoda_cieciw
from interface import get_params_from_user
from built_in_functions import *

# 1. niech uzytkownik wybierze funkcje (  wielomian, trygonometryczną, wykładniczą i ich złożenia. )
# 2. uzytkownik wybiera przedzial a - b poszukiwania miejsca zerowego
# 3. uzytkownik wybiera kryterium stopu ( dokladnosc lub liczba iteracji ) i podaje paramter ( epsilon lub liczba iteracji )
# 4. obydwie metody szukają miejsc zerowych
# 5. wyświetla wyniki
#   5.1 wyświetla współrzędne miejsc zerowych
#   5.2 rysowanie wykresu danej funkcji

# params = get_params_from_user()
# print(params)

print(szukaj_miejsc_zerowych_metoda_cieciw(1,4,'eps', 0.01, math.sin))
