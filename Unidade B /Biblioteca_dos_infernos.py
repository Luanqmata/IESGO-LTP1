import time
class Cozinha:
    def __init__(self,nome_pessoa, hamburger, bebida):
        self.nome_pessoa = nome_pessoa
        self.hamburger = hamburger
        self.bebida = bebida
    
    def __str__(self):
        return f"\nO pedido de:{self.nome_pessoa}, {self.hamburger} e {self.bebida}.\n\n"
        time.sleep(0.5)
    
class Pedidos:
    def __init__(self):
        self.lista_pedidos = []
        self.lista_pagamentos_pendentes = [] 
    
    def registrar_pedido(self, pedido):
        valor_comida = Cardapio.hamburgeris_precos[pedido.hamburger]#Chamo a clas Cardapio. Onde esta armazenado os valores do sanduiches
        valor_bebida = Cardapio.bebidas_precos[pedido.bebida]
        valor_final = valor_comida+valor_bebida 
        print(f'\n\nO cliente {pedido.nome_pessoa} deve pagar o ')
        print(f'Valor de: R${valor_final}.\n')
        print('----------Pedido Registrado----------')
        self.lista_pagamentos_pendentes.append(pedido.nome_pessoa)
        self.lista_pagamentos_pendentes.append(valor_final)
        self.lista_pedidos.append(pedido.nome_pessoa)               # GUARDO ELAS NAS LISTAS 
        
    
    def deletar_pedido(self,nome,valor):
        if nome in self.lista_pagamentos_pendentes and valor in self.lista_pagamentos_pendentes:
            self.lista_pagamentos_pendentes.remove(nome)
            self.lista_pagamentos_pendentes.remove(valor)
            self.lista_pedidos.remove(nome)
            print('O Pedido Foi cancelado Com Sucesso!')
            print(self.lista_pagamentos_pendentes)
        else:
            print('Nao existe ninguem com esse nome.')   
            
    def __str__(self):
        return f"Total de pedidos: {len(self.lista_pedidos)}"
    
class Cardapio:
    hamburgeris = [
        "Cachorro Quente",
        "X-Salada",
        "X-Burger",
        "X-Bancon",
        "X-Tudão",
        "Add Batata",
        "Batata",
        "Adicional Batata"
    ]
    
    hamburgeris_precos = {
        "Cachorro Quente": 6,
        "X-Salada": 12,
        "X-Burger": 10,
        "X-Bancon": 16,
        "X-Tudão": 23,
        "Add Batata": 4,
        "Batata": 4,
        "Adicional Batata": 4
    }
    
    bebidas = [
        "Coca-Cola",
        "Tampico",
        "Guaraná",
        "Wisky",
        "Cerveja",
        "Fanta",
        "Açaí"
    ]
    
    bebidas_precos = {
        "Coca-Cola": 4,
        "Tampico": 9,
        "Guaraná": 5,
        "Wisky": 49,
        "Cerveja": 10,
        "Fanta": 7,
        "Açaí": 10
    }
    

pedido = Pedidos()
print("-----------BEM_VINDO_A_AMBURGUERIA-------------")
while True:
    print("--------------------------------------------------")
    print('Registrar Pedido = Digite 1.')
    print('Ver Qnt° de pedidos = Digite 2.')
    print('Finalizar Pedido = Digite 3.')
    print('Excluir Pedido = Digite 4.')
    user_escolha = int(input('\nEscolha: '))

    if user_escolha == 1:
        nome_cliente = input('Digite seu nome: ')
        sanduiche_escolha = int(input('Digite o número do Sanduíche: '))# PEGA O NUMERO Q O USUARIO ESCOLHEU DE ACORDO COM O CARDAPIO
        bebida_escolha = int(input("Digite o número de escolha da bebida: "))
        lanche = Cardapio.hamburgeris[sanduiche_escolha - 1] # puxa a CLass CARDAPIO. uso a lista de dentro da Clas cardapio (hamburgeris[e o input numero -1(por que a contagem inica em 0)])
        bebida = Cardapio.bebidas[bebida_escolha - 1]
        pedido_info = Cozinha(nome_cliente, lanche, bebida)# chamo a Class Cozinha(onde parametros são obrigatorios) e preencho com os input
        pedido.registrar_pedido(pedido_info) # chamo a Class pedido() linha 72 e a função dentro dela para ser reproduzida com o parametro pra ser armazenado
        print(pedido_info)# printo a mensagem __str__ da classe cozinha 

    elif user_escolha == 2:
        print(pedido) # printo a mensagem __str__ da classe pedido
        print(pedido.lista_pedidos)
        
    elif user_escolha == 3:
        print(pedido.lista_pagamentos_pendentes)
        
    elif user_escolha == 4 :
        nome_cliente = input('Digite seu nome: ')
        valor_pago = int(input('Digite o Valor que foi Pago: '))
        pedido.deletar_pedido(nome_cliente,valor_pago)
        print(pedido)

    elif user_escolha == 5:
        print(cozinha())
