import time

def fatorial_qualqr_numero():
    numero_user = int(input("digite o valor para saber o fatorial dele mesmo: "))
    contagem = numero_user

    limite = contagem
    while limite >= 1:
        calculo = limite * numero_user
        print(numero_user,'x', limite ,'=' ,calculo)
        time.sleep(1)
        print('Processando...')
        limite -= 1
    if numero_user < 0:
        print('  ERROR.\n >>>O numero deve ser POSITIVO.<<< \n positivo?')
    
print(fatorial_qualqr_numero())
