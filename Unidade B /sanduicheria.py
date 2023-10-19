
import time

class Cozinha:
    def __init__(self,nome_pessoa, hamburger, bebida):
        self.nome_pessoa = nome_pessoa
        self.hamburger = hamburger
        self.bebida = bebida

    def __str__(self):
        return f"\n\tO pedido de:{self.nome_pessoa}, {self.hamburger} e {self.bebida}.\n\n"
        time.sleep(0.5)

class Pedidos:
    def __init__(self):
        self.fila_espera = []
        self.lista_pagamentos_pendentes = [] 
        self.lista_pedidos = []
        
    def registrar_pedido(self, pedido):
        valor_comida = Cardapio.hamburgeris_precos[pedido.hamburger]#Chamo a clas Cardapio. Onde esta armazenado os valores do sanduiches
        valor_bebida = Cardapio.bebidas_precos[pedido.bebida]
        valor_final = valor_comida+valor_bebida 
        print('\n\n\n----------         Pedido Registrado        ----------\n')
        print(f'\n\tO cliente {pedido.nome_pessoa} deve pagar o ')
        print(f'\t\tValor de: R${valor_final}.\n')
        self.lista_pagamentos_pendentes.append(pedido.nome_pessoa)  #adiciono o pedido.nome_pessoa + o valor do pagamento na lsita de pagamentos pend...
        self.lista_pagamentos_pendentes.append(valor_final)
        self.fila_espera.append(pedido.nome_pessoa)               # guardo o nome da pessoa que esta armazenada na class cozinha,na fila da espera. 
        self.lista_pedidos.append(pedido.nome_pessoa)
        self.lista_pedidos.append(pedido.hamburger)
        self.lista_pedidos.append(pedido.bebida)
   
    def deletar_pedido(self,nome,valor,lanche,bebida):
        if nome in self.lista_pagamentos_pendentes and valor in self.lista_pagamentos_pendentes:
            self.lista_pagamentos_pendentes.remove(nome)
            self.lista_pagamentos_pendentes.remove(valor)
            self.lista_pedidos.remove(nome)
            self.fila_espera.remove(nome)
            if lanche in self.lista_pedidos and bebida in self.lista_pedidos:
                self.lista_pedidos.remove(lanche)
                self.lista_pedidos.remove(bebida)
                print('\nO Pedido Foi cancelado Com Sucesso!')
            else:
                print('\n\nError. Numero do pedido incorreto. Olhe o numero Antes do Nome do Sanduiche')
        else:
            print('\n\nError. Ou o Cliente não está cadastrado ou o valor que foi pago, foi digitado errado \n\n\t Tente Novamente!.')   
    
    def fechar_comanda(self):
            print('\n\t OPÇÃO FECHAR COMANDA \n\n')
            contagem_comandas = len(self.fila_espera)
            time.sleep(0.5)
            print(f'\n>>>>>>   Total De Pedidos Em Aberto: {len(self.fila_espera)}   <<<<<<')
            time.sleep(0.2)
            print('\n\nPagamentos a Serem Feitos: (Cliente,valor)\n')
            print(pedido.lista_pagamentos_pendentes)
            if contagem_comandas !=0:
                cliente = input('\nDigite seu Nome: ')
                print('\n Debito Ou Credito? \n ')
                time.sleep(0.2)
                valor =  int(input('Digite o Valor a Pagar: '))
                if cliente in self.lista_pagamentos_pendentes and valor in self.lista_pagamentos_pendentes:
                    self.lista_pagamentos_pendentes.remove(cliente)
                    self.lista_pagamentos_pendentes.remove(valor)
                    self.fila_espera.remove(cliente)
                    self.lista_pedidos.append('<--PAGO.')
                    print('\nA sua Comanda Foi finalizada Com Sucesso.\n\n\t\t Obrigado Volte SEMPRE!\n')
                    print(f'Total De Pedidos Em Aberto: {len(self.fila_espera)}')
                else:
                    print('Nome Ou Valor Digitados Errados. Tente Novamente A Finalização.')
            else:
                time.sleep(1.5)
                print('\n\n\t NÃO A PEDIDOS A SEREM FINALIZADOS...\n')
                

                         
    def __str__(self):
        R = '\n\t\t OPÇÃO Exibir FILA De pedidos. \n'
        R += f"\t>>>>>>>>>>>>>>  Total de pedidos A serem Produzidos: {len(self.fila_espera)}  <<<<<<<<<<\n"
        R += '\n\nSe o Nome Da pessoa Estiver Na primeira Lista e na segunda significa que o pedido Dele ainda Esta em produção.\n'
        R += f'\n\t{self.lista_pagamentos_pendentes}\n'
        R += f'\t{self.lista_pedidos}\n'
        return R

    
class Cardapio:
    hamburgeris = [
        "1.Cachorro Quente",
        "2.X-Salada",
        "3.X-Burger",
        "4.X-Bancon",
        "5.X-Tudão",
        "6.Add Batata",
        "7.Batata",
        "8.Adicional Batata"
    ]
    
    hamburgeris_precos = {
        "1.Cachorro Quente": 6,
        "2.X-Salada": 12,
        "3.X-Burger": 10,
        "4.X-Bancon": 16,
        "5.X-Tudão": 23,
        "6.Add Batata": 4,
        "7.Batata": 4,
        "8.Adicional Batata": 4
    }
    
    bebidas = [
        "1.Coca-Cola",
        "2.Tampico",
        "3.Guaraná",
        "4.Wisky",
        "5.Cerveja",
        "6.Fanta",
        "7.Açaí"
    ]
    
    bebidas_precos = {
        "1.Coca-Cola": 4,
        "2.Tampico": 9,
        "3.Guaraná": 5,
        "4.Wisky": 49,
        "5.Cerveja": 10,
        "6.Fanta": 7,
        "7.Açaí": 10
    }
    

pedido = Pedidos()
print("\n\n---------- -          BEM_VINDO_Au_LaricaSSa           - -----------")
while True:
    print("\n----------------------- LaricaSSa - MENU ------------------------------\n")
    print('\n\tRegistrar Pedido = Digite 1.')
    print('\tFinalizar Pedido = Digite 2.')
    print('\tExibir Lista de Pedidos Do Dia = Digite 3.')
    print('\tVer FILA de pedidos = Digite 4.')
    print('\tModificar Pedido = Digite 5.')
    print('\tExcluir Pedido = Digite 6.')
    
    
    user_escolha = int(input('\n\nEscolha do menu: '))

    if user_escolha == 1:
        print('\n\t----------------       Cardapio       ---------------')
        print('\n\t\tLanches\t\t\t     Bebidas')
        print('\t"1.Cachorro Quente": 6\t\t"1.Coca-Cola": 4')
        print('\t"2.X-Salada": 12\t\t"2.Tampico": 9')
        print('\t"3.X-Burger": 10\t\t"3.Guaraná": 5')
        print('\t"4.X-Bancon": 16\t\t"4.Wisky": 49')
        print('\t"5.X-Tudão": 23\t\t\t"5.Cerveja": 10')
        print('\t"6.Add Batata": 4\t\t"6.Fanta": 7')
        print('\t\t\t\t\t"7.Açaí": 10')
        
        #----------------------------------------------------------------
        
        print('\n\n\tPreencha Os Dados Para Prosseguir com seu Pedido! :D.\n')
        nome = input('\nDigite seu nome: ')
        nome_cliente = nome.lower()
        sanduiche_escolha = int(input('Digite o número do Sanduíche: '))# PEGA O NUMERO Q O USUARIO ESCOLHEU DE ACORDO COM O CARDAPIO
        bebida_escolha = int(input("Digite o número de escolha da bebida: "))
        lanche = Cardapio.hamburgeris[sanduiche_escolha - 1] # puxa a CLass CARDAPIO. uso a lista de dentro da Clas cardapio (hamburgeris[e o input numero -1(por que a contagem inica em 0)])
        bebida = Cardapio.bebidas[bebida_escolha - 1]
        pedido_info = Cozinha(nome_cliente, lanche, bebida)# chamo a Class Cozinha(onde parametros são obrigatorios) e preencho com os input
        pedido.registrar_pedido(pedido_info) # chamo a Class pedido() linha 72 e a função dentro dela para ser reproduzida com o parametro pra ser armazenado
        print(pedido_info)# printo a mensagem __str__ da classe cozinha 

    elif user_escolha == 2:
        pedido.fechar_comanda()
        
    elif user_escolha == 3:
        print(f'\n\n\n\n\nHoje tivemos Esses Pedido(s):\n')
        print(pedido.lista_pedidos)  
   
    elif user_escolha == 4 :
        print(pedido) # printo a mensagem __str__ da classe pedido
        
    elif user_escolha == 5:
            
            contagem = len(pedido.lista_pagamentos_pendentes)/2
            
            if contagem != 0: 
                
                print('\nSe vc deseja Trocar O sanduiche. Escreva "Sanduiche".\n\nSe vc deseja trocar A bebida. Escreva "Bebida".')   
                
                resposta = input('\nResponda aqui: ')
                resposta_m = resposta.lower()
                
                if resposta_m == 'sanduiche':
                    
                    print('\n\t----------------       Cardapio       ---------------')
                    print('\n\t\tLanches')
                    print('\t"1.Cachorro Quente"')
                    print('\t"2.X-Salada"')
                    print('\t"3.X-Burger"')
                    print('\t"4.X-Bancon"')
                    print('\t"5.X-Tudão"')
                    print('\t"6.Add Batata"')
                    
                    print('\n\nLista de pedidos :',pedido.lista_pedidos)
                    
                    sanduiche_atual = int(input('\n\n\nDigite o numero do sanduiche Atual: '))
                    encontrar_sanduiche = Cardapio.hamburgeris[sanduiche_atual - 1]
                    del_sanduiche = pedido.lista_pedidos.remove(encontrar_sanduiche)
                    
                    sanduiche_troca = int(input('\nAgora digite o numero do sanduiche que queira trocar: '))
                    encontrar_sanduiche_novo = Cardapio.hamburgeris[sanduiche_troca - 1]
                    add_sanduiche = pedido.lista_pedidos.append(encontrar_sanduiche_novo)
                    
                    print('\n\n\n A troca ocorreu com Sucesso E vc ainda Ganhou uma promoção RARA!')
                    print('\n \t VOCÊ NÃO PAGA O VALOR DA TROCA.')
                    
                elif resposta_m == 'bebida':
                    print('\n\t----------------       Cardapio       ---------------')
                    print('\n\tBebidas')
                    print('\t"1.Coca-Cola"')
                    print('\t"2.Tampico"')
                    print('\t"3.Guaraná"')
                    print('\t"4.Wisky"')
                    print('\t""5.Cerveja"')
                    print('\t"6.Fanta"')
                    print('\t"7.Açaí"')
                    
                    print('\n\nLista de pedidos :',pedido.lista_pedidos)
                    
                    bebida_atual = int(input('\n\nDigite o numero do bebida Atual: '))
                    encontrar_bebida = Cardapio.bebidas[bebida_atual - 1]
                    del_bebida = pedido.lista_pedidos.remove(encontrar_bebida)
                    
                    bebida_nova = int(input('\n\nDigite o numero do bebida Atual: '))
                    encontrar_bebida_nova = Cardapio.bebidas[bebida_nova - 1]
                    add_bebida = pedido.lista_pedidos.append(encontrar_bebida_nova)
                    
                    print('\n A troca ocorreu com Sucesso E vc ainda Ganhou uma promoção RARA!')
                    print('\n \t VOCÊ NÃO PAGA O VALOR DA TROCA.')
                    
                else:
                    print('\nVocê Digitou algo de errado.')
            else:
                time.sleep(1)
                print('\n\n NÃO EXISTE PEDIDOS A SEREM MODIFICADOS...\n')   
                
    elif user_escolha == 6:
        print('\n\n\n\n OPÇÃO Excluir Pedido \n\n')
        contagem = len(pedido.lista_pagamentos_pendentes)/2
        if  contagem != 0:
            print(pedido.lista_pedidos)
            print(pedido.lista_pagamentos_pendentes,'\n')
            nome = input('Digite seu nome: ')
            nome_cliente = nome.lower()
            valor_pago = int(input('Digite o Valor que foi Pago: '))
            numero_sanduiche = int(input('digite o Numero do Sanduiche: '))
            numero_bebida = int(input('digite o Numero do Bebida: '))
            lanche = Cardapio.hamburgeris[numero_sanduiche - 1]
            bebida = Cardapio.bebidas[numero_bebida - 1]
            pedido.deletar_pedido(nome_cliente,valor_pago,lanche,bebida)
        else:
            print('\t NÃO HÁ PEDIDOS A SEREM CANCELADOS...\n\n')
