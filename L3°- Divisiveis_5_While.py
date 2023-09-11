import time

def divisiveis_5():
    print('numeros de 1 a 100 divisiveis por 5.')
    contador = 100
    print('\n Nao sei usar for \n') 
    while contador >= 10:
        conta = contador / 5
        print(contador, '/  5  =', conta)
        print('\nprocessando...\n')
        time.sleep(1) ## ISSO NAO É NESCESSARIO É SO PARA STYLE.
        contador -= 5
        
divisiveis_5()    
