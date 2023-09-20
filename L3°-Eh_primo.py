def numero_primo_for():
    numero = int(input('digite um numero: '))
    for i in range(1):
        if numero <= 1:
            print('o numero deve ser maior do que 0 e 1, logo ele não é primo.')
            break
        if numero % 5 == 0:
            print(f'este numero {numero} é divisivel por 5, logo ele nao é primo')
            break
        if numero % 3 == 0:
            print(f'este numero {numero} é divisivel por 3, logo ele nao é primo')
            break
        if numero % 2 == 0:
            print(f'este numero {numero} é divisivel por 2, logo ele nao é primo')
            break
        else:
            print('o numero é primo.')
            exit()
numero_primo_for()

                                                                                                                                        """                        NO WHILE
                                                                                                                                        def numero_primo():
                                                                                                                                            numero = int(input('Digite um numero: '))
                                                                                                                                            while True:
                                                                                                                                                if numero % 2 == 0:
                                                                                                                                                    print('\no numero é divisivel por 2 portanto.')
                                                                                                                                                    print('o numero nao é primo.')
                                                                                                                                                    break
                                                                                                                                                if numero % 3 ==0:
                                                                                                                                                    print('\no numero é divisivel por 3 portanto.')
                                                                                                                                                    print('o numero nao é primo.')
                                                                                                                                                    break
                                                                                                                                                if numero % 5 ==0:
                                                                                                                                                    print('\no numero é divisivel por 5 portanto.')
                                                                                                                                                    print('o numero nao é primo.')
                                                                                                                                                    break
                                                                                                                                                else:
                                                                                                                                                    print('o numero é primo.')
                                                                                                                                        """
