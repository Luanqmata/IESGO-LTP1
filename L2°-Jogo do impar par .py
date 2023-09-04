import random
import time

import random
import time
opcoes_do_jogo =['impar','par'] 

def jogo_impar_par():
    selecao_computador = random.randint(0,10)
    print('o conputador selecionou um numero entre 0 e 10.')
    time.sleep(1)
    print('o conputador selecionou um numero entre 0 e 10.')
    time.sleep(1)
    print('Sorteado ,agora tente adivinhar.')
    
    
    acertou = False
    palpites = 0
    while not acertou:
        palpites_jogador = input("Ímpar ou par? ").lower()  
        if palpites_jogador in opcoes_do_jogo:
            palpites_computador = selecao_computador % 2 == 0  
            if (palpites_jogador == 'par' and palpites_computador) or (palpites_jogador == 'impar' and not palpites_computador):
                print('Você acertou!')
                acertou = True
            else:
                print('Você errou. Tente novamente.')
                palpites += 1
        else:
            print('Escolha entre "ímpar" ou "par".')

    print(f'Você acertou em {palpites + 1} tentativas.')
      
def jogo_impar_par_humanos():
    print('digite um numero entre.')
    time.sleep(1)
    selecao_user1 = int(input("'0 e 10' digite: "))
    
    acertou = False
    palpites = 0
    while not acertou:
        palpites_user2 = input('Impar ou Par.').lower()
        if palpites_user2 in opcoes_do_jogo:
            palpite_computado = selecao_user1 % 2 ==0
            if(palpites_user2 == 'par' and palpite_computado) or (palpites_user2 == 'impar' and not palpite_computado):
                print('Você Acertou!')
                acertou = True
            else:
                print('Você errou. tente novamente.')
                palpites += 1 
        else:
            print('Você Errou . Escolha entre "ímpar" ou "par".')
        
    print(f'Você acertou em {palpites+1} tentativas.')
            
    
condicao_dos_menus = int(input('escolha entre jogar com o computador Digite = 1 \n jogar contra amigo Digite = 2 : '))

if condicao_dos_menus == 1:
    jogo_impar_par()
elif condicao_dos_menus == 2:
    jogo_impar_par_humanos()
else:
    print('digite entre 1 e 2.')
    
