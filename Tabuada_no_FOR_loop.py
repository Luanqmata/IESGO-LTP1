"""                                 
                                                            ## CONTAGEM DO '1 AO 10'
def contagem():
    começo = int(input('Digite o começo da contagem.'))
    final = int(input('Digite o final da contagem.'))
    for i in range(começo, final):                     ##  {  E PARA FAZER A CONTAGEM DESCRESCENTE= for i in range(final,começo,-1):}
        print(i)
contagem()
"""
## _______________________________________________________________________________________________________
import time 
                                                          
                                                         ##TABUADA DE QUALQR NUMERO.
                                     
def tabuada():
    print('\n@@@@@@@@@@@@ Gerador de tabuada. @@@@@@@@@@@@@@\n')
    numero_escolhido = int(input('Digite o numero para o computador fazer a tabuada dele: '))
    print('\n')
    for multiplicador in range(1, 11):
        calculo = numero_escolhido * multiplicador
        time.sleep(1)
        print(f'{numero_escolhido} x {multiplicador} = {calculo}')

## __________________________________________________________________________________________________________

                                                            ## TABUADA DO 1 AO 10 
def tabuada_1_10():
    print('\n@@@@@@@@@@@@@ TABUADA DO 1 ao 10. @@@@@@@@@@@@@\n')
    for multiplo in range(1,11):
        time.sleep(0.5)
        print(f'\nTABUADA DO {multiplo} : \n')
        for expoente in range(1,11):
            conta = multiplo * expoente
            print(f"    {multiplo} x {expoente} = {conta}")
    
user_dado_menu = int(input('Digite entre 1 e 2 para a alternação de Menus.\n Menu 1 Gerador de tabuada n° especifico.\n Menu 2 Tabuada do 1 ao 10 : '))
if user_dado_menu == 1:
    tabuada()
elif user_dado_menu == 2:
    tabuada_1_10()
