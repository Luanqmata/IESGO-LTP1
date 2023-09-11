def calcula_raiz():
    raiz_asercalculada = int(input('Digite o valor para descobrir a √: '))
    
    if raiz_asercalculada >= 0 :
        raiz_quadrada = raiz_asercalculada ** 0.5
        if raiz_quadrada % 1 == 0:
            print(f'O valor escolhido foi: {raiz_asercalculada}.\n E a √ é = {int(raiz_quadrada)}')
        else:
            print('O numero deve ser um inteiro.')
    else:
        print('O numero deve ser positivo.')
        
calcula_raiz()
