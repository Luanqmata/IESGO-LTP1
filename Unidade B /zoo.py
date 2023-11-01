"""

Contexto:
Você foi encarregado de desenvolver um sistema para gerenciar os animais de um zoológico. O zoológico tem vários tipos de animais, e eles precisam de uma forma organizada de acompanhar informações básicas sobre esses animais, como espécie, dieta, idade e habitat.

Requisitos:

Crie uma classe Zoologico que tenha os seguintes atributos:

animais (uma lista para armazenar instâncias da classe Animal)
A classe Zoologico deve ter os seguintes métodos:

adicionar_animal(self, animal): para adicionar um novo animal ao zoológico.
remover_animal(self, nome): para remover um animal do zoológico usando seu nome.
listar_animais(self): para listar todos os animais no zoológico e suas informações.
Desafio:

Adicione um atributo habitat à classe Animal (por exemplo, "Savana", "Tundra", "Floresta Tropical"). Modifique o método descricao para incluir essa informação.
Na classe Zoologico, adicione um método buscar_por_especie(self, especie) que retorna uma lista de animais dessa espécie específica.
Implemente a possibilidade de listar todos os animais em um habitat específico.
Dicas:

Ao adicionar ou remover animais da lista em Zoologico, lembre-se de usar os métodos da lista, como append ou remove.
Ao listar os animais, use um loop para iterar sobre todos os animais e chamar o método descricao de cada animal.
"""
class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def __str__(self):
        return f'{self.nome} é um {self.especie}, ele tem {self.idade} anos. Ele é {self.dieta} e seu habitat é {self.habitat}.'
class Zoo: 
    def __init__(self):
        self.lista_animais_nome = []
        self.lista_animais = []

    def adicionar_animal_caracters(self, nome, especie, idade, dieta, habitat):
        dados_jutnos = nome, especie, idade, dieta, habitat 
        self.lista_animais.append(dados_jutnos)
    
    def adicionar_animal(self,nome):
        
    
    # def remover_animal(self, nome):      
      #  if nome in self.lista_animais:
       #     self.lista_animais.remove(nome)
        #    print('Foi removido com sucesso.')
       # else:
       #     print('O animal Não foi removido ')    
    #def listar_animais(self):    
zoo = Zoo()     
        
while True:
    print('Opções:')
    print('1. Registrar um animal')
    print('2. EXCLUIR')

    user_escolha = int(input('Digite o número da opção desejada: '))
    
    if user_escolha == 1:
        print('Opção 1: Registro de Animal')
        nome_animal = input('Digite o nome do animal: ')
        idade_animal = int(input('Digite a idade do animal: '))
        especie_animal = input('Digite a espécie do animal: ')
        dieta_animal = input('Digite o tipo de dieta deste animal: ')
        habitat_animal = input('Qual o tipo de habitat que esse animal vive? ')

        zoo.adicionar_animal(nome_animal)
        
        zoo.adicionar_animal_caracters(nome_animal, especie_animal, idade_animal, dieta_animal, habitat_animal)
        
        animal_info = Animal(nome_animal, especie_animal, idade_animal, dieta_animal, habitat_animal)
        print(animal_info)
        
        print('\nExitem ',len(zoo.lista_animais),'Animais, Registrados No ZoOlogico.')        
        
    elif user_escolha == 2:
        nome = input('Digite o Nome do Animal para exclui-lo: ')
        zoo.remover_animal(nome)
    
    elif user_escolha ==3:
        print(zoo.lista_animais)
    else:
        print('Opção inválida. Digite 1 para registrar um animal ou 2 para sair.')
