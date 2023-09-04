import random
import time
opcao_resposta = ['sim','não']

def gerador_sim_nao():
    while True:
        frase = input("digite A pergunta. e 'sair' para parar. ")
        if frase.lower() == "sair":
            return exit()
    
        sim_nao = random.choice(opcao_resposta)
        time.sleep(0.5)
        print('Pensando na Resposta.')
        time.sleep(0.5)
        print('Pensando na Resposta..')
        time.sleep(0.5)    
        print('Pensando na Resposta...')
        print(f"Resposta: {sim_nao}")
print(gerador_sim_nao())
    
