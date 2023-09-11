import time
def volume_esfera(raio):
    print('\nprocessando...')
    pi = 3.141516 #FAZENDO SEM BIBLIOTECA .MATH
    formula = (( 4/3 ) * pi) * raio **3
    formula_arredondada = "{:.2f}".format(formula)
    time.sleep(1)
    return print(f'O volume da esfera é igual a: {formula_arredondada} Litros..\n')

print('             Calcula Volume Esfera.            \n')
raio = float(input('Digite o tamanho do Raio da circuferencia: '))
volume_esfera(raio)
