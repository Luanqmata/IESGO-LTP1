import random
import time

def jogo_adivinha():
    numero_aleatorio = random.randint(0,10)
    return numero_aleatorio

num1 = jogo_adivinha()
contador = 0

while True:
    numero_escolhido = input("Digite sair para sair.\nDigite o numero do jogo adivinha: '0 a 10'. ")
    
    if numero_escolhido == 'sair':
        exit()
    num2 = int(numero_escolhido)
    if num1 == num2:
        print(f"parabens você acertou.\nE você tentou {contador} vezes.")
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
