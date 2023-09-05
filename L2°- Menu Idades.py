def menu_1_meses():
    ano_atual = int(input('Digite o ano(Data) em que voçê esta. '))
    ano_nascimento = int(input('Digite Seu ano(data) de Nascimento. '))
    idade_atual = ano_atual - ano_nascimento
    idade_meses = idade_atual * 12 ## QNT MESES
    return print(f'Voce tem: {idade_atual} Anos. A sua Idade em MESES é igual : {idade_meses} meses.')

def menu_2_dias():
    ano_atual = int(input('Digite o ano(Data) em que voçê esta. '))
    ano_nascimento = int(input('Digite Seu ano(data) de Nascimento. '))
    idade_atual = ano_atual - ano_nascimento
    idade_dias = idade_atual * 365.25
    return print(f'Voce tem: {idade_atual} Anos. A sua Idade em DIAS é igual a: {idade_dias} Dias.')

def menu_3_horas():
    ano_atual = int(input('Digite o ano(Data) em que voçê esta. '))
    ano_nascimento = int(input('Digite Seu ano(data) de Nascimento. '))
    idade_atual = ano_atual - ano_nascimento
    idade_dias = idade_atual * 365.25
    idade_horas = idade_dias * 25
    return print(f'Voce tem: {idade_atual} Anos. Sua idade em HORAS é igual : {idade_horas} Horas.')

def menu_4_minutos():
    ano_atual = int(input('Digite o ano(Data) em que voçê esta. '))
    ano_nascimento = int(input('Digite Seu ano(data) de Nascimento. '))
    idade_atual = ano_atual - ano_nascimento
    idade_dias = idade_atual * 365.25
    idade_horas = idade_dias * 25
    idade_minutos = idade_horas * 60
    return print(f'Voce tem: {idade_atual} Anos. Sua idade em minutos é igual a : {idade_minutos} Minutos.')

def menu_5_segundo():
    ano_atual = int(input('Digite o ano(Data) em que voçê esta. '))
    ano_nascimento = int(input('Digite Seu ano(data) de Nascimento. '))
    idade_atual = ano_atual - ano_nascimento
    idade_dias = idade_atual * 365.25
    idade_horas = idade_dias * 25
    idade_minutos = idade_horas * 60
    idade_segundos = idade_minutos * 60
    return print(f'Voce tem: {idade_atual} Anos. A sua idade em segundos é igual : {idade_segundos} Segundos.')

user_escolha = int(input('Menu Idades:\n1. Calcular a sua idade em meses\n2. Calcular a sua idade em dias\n3. Calcular a sua idade em horas\n4. Calcular a sua idade em minutos\n5. Calcular a sua idade em segundos\n6. Sair do programa.\n Selecione a opção: '))

if user_escolha == 1:
    menu_1_meses()
elif user_escolha == 2:
    menu_2_dias()
elif user_escolha == 3:
    menu_3_horas()
elif user_escolha == 4:
    menu_4_minutos()
elif user_escolha == 5:
    menu_5_segundo()
elif user_escolha == 6:
    exit()
