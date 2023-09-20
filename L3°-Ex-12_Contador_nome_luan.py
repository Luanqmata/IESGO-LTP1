# Exercício 12 - Escreva um programa que contenha uma função com o seu nome que solicita ao usuário inserir um texto e retorna o número de letras que
# o texto contém que também compõem o seu nome.

def contador_caracters_dnv():
    meu_nome = str('luan')
    print(f"\n O nome selecionado foi '{meu_nome}'. \n")
    frase_input_user = input('digite uma frase: ')
    contador_de_l = frase_input_user.count('l')+frase_input_user.count('L')
    contador_de_u = frase_input_user.count('u')+frase_input_user.count('U')
    contador_de_a = frase_input_user.count('a')+frase_input_user.count('A')
    contador_de_n = frase_input_user.count('n')+frase_input_user.count('N')
    contagem_final_letras = contador_de_l+contador_de_u+contador_de_a+contador_de_n
    print(f'\n E a contagem das letras do nome: {meu_nome} na frase é de: {contagem_final_letras} \n')
    print(f'Tendo {contador_de_l} letra(s) L')
    print(f'Tendo {contador_de_u} letra(s) U')
    print(f'Tendo {contador_de_a} letra(s) A')
    print(f'Tendo {contador_de_n} letra(s) N')

contador_caracters_dnv()
