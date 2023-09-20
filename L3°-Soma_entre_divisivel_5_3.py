# Escreva um programa que solicita ao usuário inserir um número inteiro positivo N° e o programa retorna a soma de todos os números inteiros positivos 
# entre 1 e N° que são divisíveis por 3 ou 5.
import time

lista = []
lista_div_3 = []
lista_div_5 = []

def Soma_numeros():
    numero = int(input('\n\ndigite numero parar saber a soma total , e a soma dos numeros divisiveis por 5 e 3: '))
    for i in range(1,numero+1):
        if i % 3 == 0:
            lista_div_3.append(i)
        if i % 5 == 0:
            lista_div_5.append(i)
        lista.append(i)
        
    soma = sum(lista)
    time.sleep(0.5)
    print('\nA soma entre 1 e ',numero,'é:',soma,"\n")
    time.sleep(0.5)
    print('A soma de todos os numero Divisiveis por 3 desta lista é :',sum(lista_div_3),"\n")
    time.sleep(0.5)
    print('A soma de todos os numero Divisiveis por 5 desta lista é :',sum(lista_div_5),"\n")

Soma_numeros()
