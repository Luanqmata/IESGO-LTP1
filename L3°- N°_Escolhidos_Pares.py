import time
def _pares_entre():
    print('Pares entre numeros Escolhidos.\n')
    inicio = float(input("digite o valor do incio da contagem: ")) # para um melhor fuincionamneto do programa sempre começe com 0 ou pares.
    final = float(input('digite o valor final para parar a contagem.'))
    contador = inicio
    contador2 = 1
    while contador <= final:
        time.sleep(0.5)
        print('\n...\n')
        contador += 2
        if contador % 2 == 0:
            print('Entre os numeros escolhidos possuem:', contador2, 'Numeros pares.')
            print(contador)
            contador2 += 1
        else:
            print('\n\n>>>>>>>>>>>>>>>>Dica: Começe com 0 (Valor 1) ou NUMEROS PARES para A realização da contagem...<<<<<<<<<<<<<<<<\n')
            break
        
_pares_entre()
