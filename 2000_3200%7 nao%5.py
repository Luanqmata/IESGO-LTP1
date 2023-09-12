## Exercício 5 - Escreva um programa que encontra quais números são divisíveis por 7 e não são múltiplos de 5, entre 2000 e 3200 (inclusive). Imprima o seu resultado no console em uma única linha separada por vírgulas.
import time
def contador_2000a_3200():
    contador = 2000
    contador_7= -16
    contador_5= -92
    while contador <= 3200:
        if contador % 7 == 0:
            print('Divisiveis por 7: ',contador) ## SE NAO QUISER MOSTRAR A TABELA É SO APAGAR ESTA LINHA DE CODIGO 
            contador_7 +=1
        if contador % 5 !=0:
            print('não são multiplos de 5.', contador) ## E ESSA TAMBEM QUE O RESULTADO SERA DADO EM UMA SÓ LINHA.
            contador_5 +=1
        contador += 1
    print('\n\nCalculando Quantos Divisiveis por 7 e não por 5.')
    time.sleep(2)
    print('Calculando Quantos Divisiveis por 7 e não por 5..')
    time.sleep(2)
    print('Calculando Quantos Divisiveis por 7 e não por 5...')
    time.sleep(1)
    print('\n\nexiste:',contador_7,'Números DIVISIVEIS por 7. E existe:',contador_5,'NÃO DIVISIVEIS por 5.\n')

contador_2000a_3200()