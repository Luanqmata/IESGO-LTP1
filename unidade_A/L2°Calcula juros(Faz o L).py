def faz_o_eli():
    ##COBRA 15% e aplica no valor final esse valor 
    valor = float(input('Digite o valor da compra que O juros 15% será aplicado: '))
    juros = (valor*15)/100
    juros_aplicado = valor + juros
    return print(f'O valor com o juros Aplicado de 15% é igual a : {juros_aplicado}.\nE o Juros que foi cobrado do valor é de: {juros}.')

def user_faz_o_eli():
    valor = float(input('Digite o valor da compra: '))
    porcentagem = int(input('digite agora a % que sera cobrado.'))
    juros = (valor*porcentagem)/100
    juros_aplicado = valor + juros
    return print(f'O valor com o juros Aplicado de 15% é igual a : {juros_aplicado}.\nE o Juros que foi cobrado do valor é de: {juros}.')

user_escolha_menu = int(input("Bem vindo ao calculadora de Juros.\n Aperte 1 para Cobrar 15% de Imposto.\nAperte 2 para Cobra o Valor 'x' de imposto.\nDigite aqui: "))

if user_escolha_menu == 1:
    faz_o_eli()
elif user_escolha_menu ==2:
    user_faz_o_eli()
else:
    print('digite entre 1 e 2.')
