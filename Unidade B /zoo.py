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
import time
class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def __str__(self):
        return f'    {self.nome.title()} é um {self.especie}, ele tem {self.idade} anos. Ele é {self.dieta} e seu habitat é {self.habitat}.\n\n\n\n\n'

class Zoo: 
    def __init__(self):
        self.lista_animais_nome = []
        self.lista_animais = []

    def registro_animal(self, nome, especie, idade, dieta, habitat):
        dados_jutnos = nome, especie, idade, dieta, habitat 
        self.lista_animais.append(dados_jutnos)
        # print(self.lista_animais)
    
    def adicionar_animal(self,nome):
        self.lista_animais_nome.append(nome)
        # print(self.lista_animais_nome)
        print('\n...Realizando Cadastro...')
        time.sleep(0.2)
        print('.')
        time.sleep(0.2)
        print('..')
        time.sleep(0.2)
        print('...')
        time.sleep(0.2)
        print(f'\n\t\t...REGISTRADO COM SUCESSO...')
        
    def remover_animal(self, nome):      
        if nome in self.lista_animais_nome:
            self.lista_animais_nome.remove(nome)
            print(f'O Animal {nome}, será removido Do Zoologico com Sucesso!')
        else:
            print('O animal Não se Encontra no Zoologico.')  
              
    #def listar_animais(self):
       
zoo = Zoo()     
print('\n\t@@@@@@@@@@@@@@@@@@@@@@@@@ BEM-VINDO AO ZoO LoGIc @@@@@@@@@@@@@@@@@@@@@@@@@')
while True:
    time.sleep(1)
    print("\nMenu Numerico de opções:\n")
    print('\t1. Registro de um novo Animal no Zoologic.')
    print('\t2. Mandar o Animal de uma DESSA pra MELHOR. "excluir" ')

    user_escolha = int(input('\n-------------------------------------\nDigite o número da opção desejada: '))
    
    if user_escolha == 1:
        print('\n\t\tOpção 1: Registro de Animal\n')
        nome_animal = input('Digite o nome do animal: ')
        time.sleep(0.2)
        idade_animal = int(input('Digite a idade do animal: '))
        time.sleep(0.2)
        especie_animal = input('Digite a espécie do animal: ')
        time.sleep(0.2)
        dieta_animal = input('Digite o tipo de dieta deste animal: ')
        time.sleep(0.2)
        habitat_animal = input('Qual o tipo de habitat que esse animal vive? ')
        time.sleep(0.2)
        nome_animal_min = nome_animal.lower()
        
        zoo.adicionar_animal(nome_animal_min)
        
        zoo.registro_animal(nome_animal_min, especie_animal, idade_animal, dieta_animal, habitat_animal)
        
        animal_info = Animal(nome_animal_min, especie_animal, idade_animal, dieta_animal, habitat_animal)
        
        print(animal_info) # MSG DA __STR__
        
        #print('\nExitem ',len(zoo.lista_animais_nome),'Animais, Registrados No ZoOlogico.')        
        
    elif user_escolha == 2:
        print('Opção 2: Remover Animal do ZOO.')
        nome = input('Digite o Nome do Animal para exclui-lo: ')
        nome_min = nome.lower()
        zoo.remover_animal(nome_min)
    
    elif user_escolha ==3:
        print(zoo.lista_animais)
        print(zoo.lista_animais_nome)
        
    else:
        print('Opção inválida. Digite 1 para registrar um animal ou 2 para sair.')
