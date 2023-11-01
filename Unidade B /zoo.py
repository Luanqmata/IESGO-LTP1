"""

Desafio:

Adicione um atributo habitat à classe Animal (por exemplo, "Savana", "Tundra", "Floresta Tropical"). Modifique o método descricao para incluir essa informação.
Na classe Zoologico, adicione um método buscar_por_especie(self, especie) que retorna uma lista de animais dessa espécie específica.
Implemente a possibilidade de listar todos os animais em um habitat específico.
Dicas:

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
            print('\n...Realizando REMOÇÃO...')
            time.sleep(0.2)
            print('.')
            time.sleep(0.2)
            print('..')
            time.sleep(0.2)
            print('...')
            time.sleep(0.2)
            self.lista_animais_nome.remove(nome)
            print(f'\t...O Animal {nome}, será removido Do Zoologico com Sucesso!...\n\n\n\n\n')
        else:
            print('\n\t...processando...\n')
            time.sleep(0.9)
            print('\tERROR.')
            print('\t...O animal Não se Encontra no Zoologico...\n\n\n\n\n')  
              
    def listar_animais(self):
        print('\n\t\t...Opção 3: LISTAR REGISTROS...\n')
        time.sleep(0.4)
        print('\n\t\t...Listar Animais em Tempo real no Zoo Logic... = 1 \n')
        time.sleep(0.2)
        print('\n\t\t...Listar Animais que já Foram registrado no Sistema do Zoo Logic... = 2\n')
        
        print(f'\tNo momento Existem {len(self.lista_animais_nome)} Habitates Sendo Ocupados.\t Total de Registros Do Zoo Logic: {len(self.lista_animais)}')
        
        escolha = int(input('\n\nDigite o Numero Correspondente A lista Que você queira Imprimir: '))
        if escolha == 1:
            print('\nAnimais em TEMPO REAL no ZOOLOGIC:')
            print('\n\t\t',self.lista_animais_nome,'\n\n\n\n\n')
        elif escolha ==2:
            print('\nTodos Animais Que já passaram Pelo O ZOO LOGIC:')
            print('\n\t\t',self.lista_animais,'\n\n\n\n\n')
    
    #def listar_animais_em_habitat(self, habitat):
      #  print(f'\nAnimais no habitat {habitat}:')
       # animais_no_habitat = [animal for animal in self.lista_animais if animal.habitat == habitat]
      #  for animal in animais_no_habitat:
      #      print(f'{animal.nome.title()} ({animal.especie})')
      #  print('\n\n\n\n\n')

        
        
zoo = Zoo() 
time.sleep(0.2)    
print('\n\t@@@@@@@@@@@@@@@@@@@@@@@@@ BEM-VINDO AO ZoO LoGIc @@@@@@@@@@@@@@@@@@@@@@@@@')
while True:
    time.sleep(1)
    print("\nMenu Numerico de opções:\n")
    print('\t1. Registro de um novo Animal no Zoologic.')
    print('\t2. Mandar o Animal de uma DESSA pra MELHOR. "excluir" ')
    print('\t3. Listar.')

    user_escolha = int(input('\n-------------------------------------\nDigite o número da opção desejada: '))
    
    if user_escolha == 1:
        print('\n\t\t...Opção 1: Registro de Animal...\n')
        nome_animal = input('Digite o nome do animal: ')
        time.sleep(0.2)
        idade_animal = int(input('Digite a idade do animal: '))
        time.sleep(0.2)
        especie_animal = input('Digite a espécie do animal: ')
        time.sleep(0.2)
        dieta_animal = input('Digite o tipo de dieta deste animal: ')
        time.sleep(0.2)
        habitat = input('Qual o tipo de habitat que esse animal vive? ')
        habitat_animal = habitat.lower()
        time.sleep(0.2)
        nome_animal_min = nome_animal.lower()
        
        zoo.adicionar_animal(nome_animal_min)
        
        zoo.registro_animal(nome_animal_min, especie_animal, idade_animal, dieta_animal, habitat_animal)
        
        animal_info = Animal(nome_animal_min, especie_animal, idade_animal, dieta_animal, habitat_animal)
        
        print(animal_info) # MSG DA __STR__
        
        #print('\nExitem ',len(zoo.lista_animais_nome),'Animais, Registrados No ZoOlogico.')        
        
    elif user_escolha == 2:
        print('\n\t\t...Opção 2: Remover Animal Do zoologico...\n')
        nome = input('\nDigite o Nome do Animal para exclui-lo: ')
        nome_min = nome.lower()
        zoo.remover_animal(nome_min)
    
    elif user_escolha ==3:
        zoo.listar_animais()
    
  #  elif user_escolha == 4:
    #    habitat = input('Digite o habitat para listar os animais: ')
    #    zoo.listar_animais_em_habitat(habitat.lower())
    
    else:
        print('Opção inválida. Digite Os Números Disponiveis.')
