def soma_numeros():
    lista =[]
    numero_user =int(input('Digite um valor: '))+1
    contador = 1
    while contador < numero_user:
        if contador % 1==0:
            lista.append(contador)
        contador +=1
    soma_lista = sum(lista)
    print('\nA soma dos valores entre 0 e ',numero_user-1,'é igual a:',soma_lista,'\n')

soma_numeros()
