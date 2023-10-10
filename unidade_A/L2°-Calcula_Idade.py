ano_atual = 2023
signosstr = ['aquario','peixes','aries','touro','gemeos','cancer','leao','virgem','libra','escorpiao','sagitario','capricornio']

def questao_um():
    ano= int(input("em qual ano você nasceu? "))
    mes= int(input("qual o mes em que você nasceu? ")) 
    idade = ano_atual - ano
    signosint = (mes -1) 
    resultado = signosstr[signosint]
    return print(f"Idade é: {idade} \n Signo é: {resultado}")

resultado = questao_um()
print(resultado)
