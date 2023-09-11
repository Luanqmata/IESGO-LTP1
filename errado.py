import random
import time

def jogo_adivinha():
    numero_aleatorio = random.randint(0,10)
    return numero_aleatorio

num1 = jogo_adivinha()
contador = 0

while True:
    numero_escolhido = int(input("Digite sair para sair.\nDigite o numero do jogo adivinha: '0 a 10'. "))
    num2 = numero_escolhido
    if num1 == num2:
        print(f"parabens você acertou.\nE você tentou{contador} vezes.")
        break
    elif num1>num2:
        print("Numero do maquina é MAIOR.")
        print('.')
        time.sleep(0.5)
        print('..')
        time.sleep(0.5)
        print('...')
        time.sleep(0.5)
        contador += 1
    elif num1<num2:
        print('Numero da maquina é MENOR.')
        print('.')
        time.sleep(0.5)
        print('..')
        time.sleep(0.5)
        print('...')
        time.sleep(0.5)
        contador += 1
    elif numero_escolhido == 'sair':
        break
