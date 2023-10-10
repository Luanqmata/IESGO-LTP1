import random
import time
def jokenpo():
    opcoes_do_jogo = ['pedra', 'papel', 'tesoura']
    selecao_do_computador = random.choice(opcoes_do_jogo)
    selecao_do_usuario = opcoes_do_jogo[int(input('Escolha entre pedra, papel ou tesoura: \n 1. pedra \n 2. papel \n 3. tesoura \n'))-1]
    print(f'O computador escolheu {selecao_do_computador}.')
    print(f'O usuário escolheu {selecao_do_usuario}.')

    if selecao_do_usuario == selecao_do_computador:
        print('Empate!')
    elif selecao_do_usuario == 'pedra' and selecao_do_computador == 'tesoura':
        print('Você ganhou!')
    elif selecao_do_usuario == 'papel' and selecao_do_computador == 'pedra':
        print('Você ganhou!')
    elif selecao_do_usuario == 'tesoura' and selecao_do_computador == 'papel':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    input('Pressione ENTER para jogar novamente...')
    jokenpo()

def jokenpo_humano():
    print('____________________________________\nBEM VINDO AO Jogo Jokenpo. 2 Players\n iniciando...')
    time.sleep(2)
    minusculo1 = input('P1- Pedra,Papel,Tesoura: ')
    minusculo2 = input('P2- Pedra,Papel,Tesoura: ')
    jogador1 = minusculo1.lower()
    jogador2 = minusculo2.lower()
    time.sleep(1)
    if jogador1 == jogador2:
        print('Empate!')
    elif jogador1 == 'pedra' and jogador2 == 'tesoura':
        print('Jogador 1 GANHOU!!!!')
    elif jogador1 == 'papel' and jogador2 == 'pedra':
        print('jogador 1 Ganhou')
    elif jogador1 == 'tesoura' and jogador2 == 'papel':
        print('Jogador 1 GANHOU!!!!')
    else:
        print('JOGADOR 2 DOUTRINOU.')
    input('___________________________________________\nAperte ENTER para Jogar Novamente...')
    jokenpo_humano()

escolha_menu_user = int(input(' Menu = 1 = Jokenpo contra Maquina\nMenu = 2 = Jokenpo contra Humano.\nDigite O numero do menu: '))

if escolha_menu_user == 1:
    jokenpo()
elif escolha_menu_user == 2:
    jokenpo_humano()
else:
    print('Digite entre 1 e 2.')
