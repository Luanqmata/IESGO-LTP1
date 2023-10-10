def calculo_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura aqui: "))
    conta = peso/(altura * altura)
    imc = '{:.2f}'.format(conta)
    
    if float(imc) <= 16:
        return print('magreza grave', 'Seu imc é:',imc)
    elif 16 < float(imc) <= 17:
        return print('magreza moderada','Seu imc é:', imc)
    elif 17 < float(imc) <= 18.5:
        return print('magreza leve', 'Seu imc é:',imc)
    elif 18.5 < float(imc) <= 25:
        return print('saudável', 'Seu imc é:',imc)
    elif 25 < float(imc) <= 30:
        return print('sobrepeso', 'Seu imc é:',imc)
    elif 30 < float(imc) <= 35:
        return print('obesidade grau 1','Seu imc é:', imc)
    elif 35 < float(imc) <= 40:
        return print('obesidade grau 2', 'Seu imc é:',imc)
    elif float(imc) >= 40:
        return print('obesidade grau 3','Seu imc é:', imc)
    else:
        return 'IMC fora das faixa'

print(f'{calculo_imc()}')
