"""##                                                    CONTADOR DO 1 AO 10 e virse-versa

                            ## DO 1 AO 10 
                            incio = 1
                            final = 10
                            while incio <= final:
                                print(incio)
                                incio +=1
                                
                                                                                        ## DO 10 AO 1 
                                                                                        inicio = 10
                                                                                        while inicio >=1:
                                                                                            print(inicio)
                                                                                            inicio -=1
                                                                                        """
##__________________________________________________________________________________________________________________

import time
def tabuada_while():
    numero_da_tabuada =int(input('\n\n digite o numero para realizar a tabuada: '))
    print('\n')
    i = 1
    while i <= 10:
        conta = i * numero_da_tabuada
        print(f'  {i} x {numero_da_tabuada} = {conta}')
        time.sleep(0.5)
        i +=1

##_____________________________________________________________________________________________________________________

def tabuada_1_10_while():
    print('\n@@@@@@@@@@@@ Tabuada do 1 ao 10 WHILE @@@@@@@@@@@@\n')
    a = 1
    while a <= 10:
        b = 1 # Reinicializa o contador b a cada iteração de a
        time.sleep(0.5)
        print(f'\nTABUADA DO {a}\n')
        while b <=10:
            conta =a*b
            print(f'{a} x {b} = {conta}')
            b+=1
        a +=1
            
menu_user_dado = int(input('Digite entre 1 e 2 para a alternação de Menus.\n Menu 1 Gerador de tabuada n° especifico.\n Menu 2 Tabuada do 1 ao 10 : '))
if menu_user_dado == 1:
    tabuada_while()
elif menu_user_dado ==2:
    tabuada_1_10_while()
