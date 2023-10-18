
class Pedidos:
    def __init__(self,nome_pessoa, hamburger, bebida):
        self.lista_pedidos = []
        self.nome_pessoa = nome_pessoa
        self.hamburger = hamburger
        self.bebida = bebida
        
        
    def __str__(self):
        return f"\nO pedido de:{self.nome_pessoa}, {self.hamburger} e {self.bebida}. Total de pedidos: {len(self.lista_pedidos)}\n"


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
    
print('Hamburgueria.')

user_escolha = int(input('Comer aqui: 1, ou delivery: 2\nEscolha: '))

if user_escolha == 1:
    nome = input('digite seu nome: ')
    sanduiche_escolha = int(input('Digite o número do Sanduíche: '))
    bebida_escolha = int(input("Digite o número de escolha da bebida: "))
    lanche = Cardapio.hamburgeris[sanduiche_escolha - 1]
    bebida = Cardapio.bebidas[bebida_escolha - 1]
    pedido = Pedidos(nome,lanche,bebida)
    print(pedido)
