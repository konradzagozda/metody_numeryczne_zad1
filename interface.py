def get_params_from_user():
    params = {}

    params['func'] = int(input(
        '''
        Wybierz funkcję:
        1. x^2 - 3 / x = -1.7, x = 1.7
        2. sin(x) / x = 0 +- pi
        3. 3^x - 2 / x = 0.63
        4. 3^x * sin(x) / x = 0, x = 0.63
        5. (x^2 - 3) * sin(x) / x = -3,14, x = 0 ... 
        >>>'''))

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

    return params
