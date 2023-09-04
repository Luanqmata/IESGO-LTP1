def contador_palavras():
    frase = input('digite uma frase:')
    separador_palavra = frase.split()
    contador_palavra = len(separador_palavra)
    frase_sem_espaco = ''.join(separador_palavra)
    return f"A sua frase possui {contador_palavra} Palavras. \n A frase selecionada foi: {frase.title()}\n frase sem espaço : {frase_sem_espaco}."
resultado = contador_palavras()
print(resultado)
