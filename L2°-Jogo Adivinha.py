import random
import time

def jogo_adivinha():
    numero_aleatorio = random.randint(0,10)
    return numero_aleatorio
num1 = jogo_adivinha()

while True:
    numero_escolhido = int(input("Digite o numero do jogo adivinha: '0 a 10'. "))
    num2 = numero_escolhido
    if num1 == num2:
        print(f"parabens você acertou.")
        break
    elif num1>num2:
        print("Numero do maquina é MAIOR.")
        time.sleep(0.5)
        print('..')
        time.sleep(0.5)
        print('...')
    elif num1<num2:
        print('Numero da maquina é MENOR.')
        time.sleep(0.5)
        print('..')
        time.sleep(0.5)
        print('...')
