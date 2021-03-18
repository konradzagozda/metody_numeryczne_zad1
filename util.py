import sys

#return miejsce zerowe ( zalozmy ze jest jedno )
def szukaj_miejsc_zerowych_metoda_cieciw(a,b, stop, stop_param, f):
    init_a, init_b = a, b

    def next_step(a, b):
        f_a_res = f(a)  # to sie powtarza wiec liczmy tylko raz...
        var = a - f_a_res / (f(b) - f_a_res) * (b - a)  # przyblizenie miejsca zerowego
        if f(var) * f_a_res < 0:  # nie moze byc 0 bo zakladamy ze jest jedno miejsce zerowe
            b = var
        else:
            a = var
        return a, b


    if stop == 'eps':
        err = sys.maxsize
        while err > stop_param:
            a, b = next_step(a, b)
            print(a,b)
            err = abs(a - b)
        return a if init_a < a < init_b else None
    elif stop == 'iter':
        i = 0
        while i < stop_param:
            a, b = next_step(a, b)
            i += 1
        return a if init_a < a < init_b else None



#todo
def styczna(a,b, stop, stop_param, f):
    pass







