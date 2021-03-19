from built_in_functions import Functions


def get_params_from_user():
    params = {}

    func_number = input(
        '''
        Wybierz funkcję:
        1. x^2 - 3 / x = -1.7, x = 1.7
        2. sin(x) / x = 0 +- pi
        3. 3^x - 2 / x = 0.63
        4. 3^x * sin(x) / x = 0, x = 0.63
        5. (x^2 - 3) * sin(x) / x = -3,14, x = 0 ... 
        >>>''')

    if func_number == '1':
        params['func'] = Functions.WIELOMIAN
    elif func_number == '2':
        params['func'] = Functions.SINUS
    elif func_number == '3':
        params['func'] = Functions.WYKLADNICZA
    elif func_number == '4':
        params['func'] = Functions.WYKL_SIN
    elif func_number == '5':
        params['func'] = Functions.WIEL_SIN
    else:
        params['func'] = Functions.SINUS


    print("pamietaj by punkty początkowe mialy inne znaki!")

    params['a'] = float(input(
        '''
        Podaj mniejszą liczbę z przedziału: >>>'''
    ))

    params['b'] = float(input(
        '''
        Podaj większą liczbę z przedziału: >>>'''
    ))

    params['stop'] = input(
        '''
        Wybierz czy kryterium stopu jest epsilon czy liczba iteracji: ( eps / iter )
        >>>'''
    ).lower()

    if (params['stop'] == 'eps'):
        params['stop-param'] = float(input('''
            Podaj epsilon >>>'''))
    elif (params['stop'] == 'iter'):
        params['stop-param'] = int(input('''
            Podaj liczbe iteracji >>>'''))
    print()

    return params
