import sys
from enum import Enum
import built_in_functions

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f'{self.__x}, {self.__y}'

# return miejsce zerowe ( zalozmy ze jest jedno )
# metoda nie zawsze zbieżna
def szukaj_miejsc_zerowych_metoda_siecznych(a, b, stop, stop_param, f):
    p = [Point(a, f(a)), Point(b, f(b))]  # punkty
    if p[0].get_y() * p[1].get_y() >= 0:    #
        return None

    def next_step(a, b):
        f_a_res = f(a)  # to sie powtarza wiec liczmy tylko raz...
        var = a - f_a_res / (f(b) - f_a_res) * (b - a)  # przyblizenie miejsca zerowego
        if f(var) * f_a_res < 0:  # nie moze byc 0 bo zakladamy ze jest jedno miejsce zerowe
            b = var
        else:
            a = var
        p.append(Point(var, f(var)))
        return a, b

    if stop == 'eps':
        errA = sys.maxsize
        errB = sys.maxsize
        while errA > stop_param and errB > stop_param:
            a, b = next_step(a,b)
            errA = abs(a - b)
            errB = abs(p[len(p)-1].get_y())
    elif stop == 'iter':
        for i in range(stop_param):
            a, b = next_step(a,b)

    return p


# todo
def styczna(a, b, stop, stop_param, f):
    pass
