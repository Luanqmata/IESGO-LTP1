def par_impar():
    numero_dado = float(input('Digite um numero inteiro positivo.'))

    if numero_dado % 2 == 0:
        print('o numero escolhido é PAR.')
        if numero_dado % 2 != 0:
            print('o numero escolhido é IMPAR.')
        else: 
            print('O numero deve ser um positivo ')
    else: 
        print('o numero deve ser inteiro')

par_impar()
