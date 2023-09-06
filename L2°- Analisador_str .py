def analisador_str():
    frase = input('digite a string: ')
    frase_separada = frase.split()
    frase1 = len(frase_separada)
    conta_caracter = frase.count('*')+frase.count('#')+frase.count('!')+frase.count('$')+frase.count('%')+frase.count('¨')+frase.count('&')+frase.count('?')
    conta_letra_maiuscula = frase.count('A')+frase.count('B')+frase.count('C')+frase.count('D')+frase.count('E')+frase.count('F')+frase.count('G')+frase.count('H')+frase.count('I')+frase.count('J')+frase.count('K')+frase.count('L')+frase.count('M')+frase.count('N')+frase.count('O')+frase.count('P')+frase.count('Q')+frase.count('R')+frase.count('S')+frase.count('T')+frase.count('U')+frase.count('V')+frase.count('W')+frase.count('X')+frase.count('Y')+frase.count('Z')
    conta_letra_minuscula = frase.count('a')+frase.count('b')+frase.count('c')+frase.count('d')+frase.count('e')+frase.count('f')+frase.count('g')+frase.count('h')+frase.count('i')+frase.count('j')+frase.count('k')+frase.count('l')+frase.count('m')+frase.count('n')+frase.count('o')+frase.count('p')+frase.count('q')+frase.count('r')+frase.count('s')+frase.count('t')+frase.count('u')+frase.count('v')+frase.count('w')+frase.count('x')+frase.count('y')+frase.count('z')
    print(f'A String possui {conta_caracter} caractes.\n A String possui: {conta_letra_maiuscula} Letras Maiusculas.\n A string possui: {conta_letra_minuscula} Letras minusculas.\nA String possui: {frase1} Palavras.')

print(analisador_str())
