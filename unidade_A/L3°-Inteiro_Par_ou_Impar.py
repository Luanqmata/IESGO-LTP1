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
"""                                    PAR IMPAR NO FOR LOOP
def par_impar1():
    numero = int(input('Digite um numero: '))
    for i in range(1):
        if numero % 2 == 0:
            print( 'par')
        if numero % 2 != 0:
            print('numero impar.')
            
par_impar1()  
"""
