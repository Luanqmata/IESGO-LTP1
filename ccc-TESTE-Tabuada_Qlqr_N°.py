"""
def contagem():
    começo = int(input('Digite o começo da contagem.'))
    final = int(input('Digite o final da contagem.'))
    for i in range(começo, final):
        print(i)
contagem()
"""
import time
def tabuada(numero_escolhido):
    print('\n@@@@@@@@@@@@ Gerador de tabuada. @@@@@@@@@@@@@@\n')
    for multiplicador in range(1, 11):
        calculo = numero_escolhido * multiplicador
        time.sleep(1)
        print(f'{numero_escolhido} x {multiplicador} = {calculo}')

numero_da_tabuada_user = int(input('Digite o numero para o computador fazer a tabuada dele: '))
tabuada(numero_da_tabuada_user)
