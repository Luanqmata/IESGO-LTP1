# Exercício 6 - Escreva um aplicativo que solicita ao usuário inserir um número e retorna o seu fatorial.
def fatorial(numero):
    resultado = 1
    for i in range(1,numero+1): ## O LOOPING VAO DO 1 ',' ATE O NUMERO ESCOLHO 'NUMERO' CADA VEZ ACRESENTANDO '+1' 
        resultado *= i ## aqui é o comando que Você da para o loop se vc qr ,multi,somar,dividir.   
    return resultado

input_user = int(input('Digite o numero q queira saber o fatorial.'))
resultado_final = fatorial(input_user)

print(f'O fatorial do numero {input_user}\nÉ igual a {resultado_final}')

## EM WHILE
"""
def fatorial(numero):
    contador = 1
    resultado = 1
    while contador <= numero:
        resultado *= contador
        contador +=1
    return resultado
        

input_user = int(input("Digite o numero para descobrir o fatorial: "))
incrementacao = fatorial(input_user)

print(f'O fatorial do numero: {input_user} é igual a: {incrementacao}')
