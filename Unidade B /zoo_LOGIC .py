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
        print(f'\n\tNo momento Existem {len(self.lista_animais_nome)} Habitates Sendo Ocupados.\t Total de Registros Do Zoo Logic: {len(self.lista_animais)}')
        
        print('\n\t\t...Opção 3: LISTAR REGISTROS...\n')
        time.sleep(0.4)
        print('\n\t\t...Listar Animais em Tempo real no Zoo Logic... DIGITE = 1 \n')
        time.sleep(0.2)
        print('\n\t\t...Listar Animais que já Foram registrado no Sistema do Zoo Logic... DIGITE= 2\n')
        
        
        escolha = int(input('\n\nDigite o Numero Correspondente A lista Que você queira Imprimir: '))
        if escolha == 1:
            print('\nAnimais em TEMPO REAL no ZOOLOGIC:')
            print('\n\t\t',self.lista_animais_nome,'\n\n\n\n\n')
            
            if self.lista_animais_nome: # VERIFICAÇÃO SE EXISTE ALGUM ITEM NA LISTA 
                nome_mai = input('Digite o nome do animal,para Mais informações: ')
                nome = nome_mai.lower()
                for animal in self.lista_animais:
                    if nome in animal:
                        print('\n',animal)
                        print('\n\n\n\n\n')
            else:
                print('não existe nenhum animal na lista.')
        elif escolha ==2:
            print('\nTodos Animais Que já passaram Pelo O ZOO LOGIC:')
            print('\n\t\t',self.lista_animais,'\n\n\n\n\n')
    
    def listar_animais_em_habitat(self, habitat):
        print(f'\nAnimais no habitat {habitat}:')
        for animal in self.lista_animais:
            if animal[4] == habitat:
                print(animal)
            else:
                print('\n\t...não existem animais nesse Habitat...')
        print('\n\n\n\n\n')


zoo = Zoo() 
time.sleep(0.2)    
print('\n\t@@@@@@@@@@@@@@@@@@@@@@@@@ BEM-VINDO AO ZoO LoGIc @@@@@@@@@@@@@@@@@@@@@@@@@')
while True:
    time.sleep(1)
    print("\nMenu Numerico de opções:\n")
    print('\t1. Registro de um novo Animal no Zoologic.')
    print('\t2. Mandar o Animal de uma DESSA pra MELHOR. "excluir" ')
    print('\t3. Listar Animais Em tempo real , e animais registrado no sistema.')
    print('\t4.Prcurar animais por HABITAT.')
    
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
        print('\n\t\t',zoo.lista_animais_nome,'\n\n')
        if zoo.lista_animais_nome:
            nome = input('\nDigite o Nome do Animal para exclui-lo: ')
            nome_min = nome.lower()
            zoo.remover_animal(nome_min)
        else:
            print('...Não existem Animamis Para serem excluidos...\n\t       ...Registre um e tente novamente...')
            print('\n\n\n\n\n')
            
    elif user_escolha ==3:
        if zoo.lista_animais:
            zoo.listar_animais()
        else: 
            print('\n\t...Ainda não existe Nenhum animal registrado no Sistema...\n\t       ...Registre um e tente novamente...')
            print('\n\n\n\n\n')
            
    elif user_escolha == 4:             # falta fazer a logica de só printar os que estão ocupando o habitat em tempo real 
        if zoo.lista_animais_nome: # checka se tem algum animal em tempo real em algum habitat.
                #nome_maiusculo = input('     digite o nome do animal: ')
                #nome = nome_maiusculo.lower()
                #if nome in zoo.lista_animais_nome:
            print('\n\tAnimais em Habitats.',zoo.lista_animais_nome,'\n')
            habitat_mai = input('\n\n    Agora digite o HABITAT: ')
            habitat = habitat_mai.lower()
            zoo.listar_animais_em_habitat(habitat)
                #else:
                #print('\n\n\tO animal n se encontra nesse Habitat.')
        else:
            print('\n\t...Não existem Habitats Ocupados...\n\t       ...Registre um e tente novamente...')
    else:
        print('Opção inválida. Digite um numero dentre as opçoes do MENU.')
