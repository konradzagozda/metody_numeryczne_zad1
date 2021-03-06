def get_params_from_user():
    params = {}

    params['func'] = int(input(
        '''
        Wybierz funkcję:
        1. 4x^5 + 3x^4 + 2x^3 + x^2 + 4x - 2
        2. sin(x)
        3. 3^x
        4. 3^x * sin(x)
        5. (4x^5 + 3x^4 + 2x^3 + x^2 + 4x - 2) * sin(x)
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
