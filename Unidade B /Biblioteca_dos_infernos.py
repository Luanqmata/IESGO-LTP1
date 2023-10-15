import time

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponivel"
       ##self.biblioteca_livros = {}##
    
    def __str__(self): # FUNÇÃO PARA TIRAR A PROVA Q O TREM VEIO PARA O LOCAL CERTO 
        return(f"Titulo: {self.titulo} | Autor: {self.autor} | Status: {self.status}\n \n")#Contagem Livros: {len(self.biblioteca_livros)#
        time.sleep(0.5)
    
class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def __str__(self):
        return(f"Nome: {self.nome}. Quantidade de Livros emprestados {len(self.livros_emprestados)}\n")
        time.sleep(0.5)
    
class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def __str__(self):  ## FAZ A CONTAGEM DE QUANTOS MEMBROS EXISTE DENTRO DA BIBLIOTECA 
        return f"\nContagem de Membros da Biblioteca: {len(self.membros)}\n\nContagem de Livros Na Biblioteca {len(self.livros)}.\n"
        
    def add_livros(self, livro):
        titulo_livro = livro.titulo
        time.sleep(1)
        self.livros[titulo_livro] = livro
        print('\n\n_____________BIBLIOTECA_______________')
        print(f'\n\nO livro foi adicionado à Biblioteca:\n')
        time.sleep(1)
        
    def add_membro(self, membro):
        nome_membro = membro.nome
        time.sleep(0.5)
        self.membros[nome_membro] = membro #manda pro self.membros porém se o nome for igual ele nao acumula tem q colocar nme e sobrenome 
        print('\n\n_____________BIBLIOTECA_______________')
        print(f'\nO membro Foi adicionado com Sucesso!\n\n')
        time.sleep(1.5)
        
    def emprestar_livro(self, livro_escolhido, nome_membro):
        if livro_escolhido in self.livros and nome_membro in self.membros:# se o parametro estiver dentro da bibliteca self.livros
            emprestimo = self.livros.get(livro_escolhido) # busca o parametro passado dentro da biblioteca 
            membro = self.membros.get(nome_membro) # busca o parametro passado dentro da biblioteca
            if emprestimo.status == 'disponivel': # e o item buscado dentro da biblioteca estiver disponivel na leitura do self.status
                emprestimo.status = 'emprestado' # retorna q o status dele é 'emprestado' agora 
                membro.livros_emprestados.append(emprestimo)# adiciona dentro da classe com .membro , e dentro da lista da classe membro com .append , q é o titulo do livro 
                membro.livros_emprestados.append(membro) 
                print(f'\nO Membro: "{nome_membro}" , Pegou o livro: "{livro_escolhido}" Emprestado.\n\n')
            else:
                print(f'\nO livro "{emprestimo.titulo}" não está disponível.\n\n')# se o item nao estiver diponivel
        else:
            print(f'\nO livro "{livro_escolhido}" ou o "{nome_membro}" não existe nessa Biblioteca .\n\n') #retornara que o livro não esta na biblitoeca 
                    
"""                                         2°metodo 
                                                                                                                                                                                                            livro = self.livros.get(livro_escolhido) 
                                                                                                                                                                                                            membro = self.membros.get(nome_membro)
                                                                                                                                                                                                            
                                                                                                                                                                                                            if livro and membro:  # Verifique se tanto o livro quanto o membro existem
                                                                                                                                                                                                                if livro.status == 'disponivel':
                                                                                                                                                                                                                    livro.status = 'emprestado'
                                                                                                                                                                                                                    membro.livros_emprestados.append(livro)
                                                                                                                                                                                                                    print(f'\nO membro "{membro.nome}" pegou emprestado o livro "{livro.titulo}".\n')
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    print('O livro não está disponível para empréstimo.\n')
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                print('Membro ou livro não registrados. Certifique-se de fazer o registro antes.\n')
"""

 
def main():
    biblioteca = Biblioteca()

    while True:
        print('\n\n\n_______________________________________')
        print("\nOpções:")
        print("1. Adicionar Um Livro Novo")
        print("2. Registrar Membro Novo")
        print("3. Emprestar Um Livro")

        user_escolha = input("Selecione uma opção: ")

        if user_escolha == "1":
            print('\n\nOpção: "Adicionar Livro..."\n')
            titulo1 = input("Digite o Título/Nome do livro: ")
            autor1 = input("Digite o Autor do livro: ")
            titulo = str(titulo1.lower())
            autor = str(autor1.lower())
            livro = Livro(titulo, autor)
            biblioteca.add_livros(livro)
            print(livro)
             
            
        elif user_escolha == "2":
            print('\n\nOpção: "Adicionar Membro..."\n')
            nome1 = input('Digite o seu Nome e Sobrenome: ')
            nome = str(nome1.lower())
            time.sleep(1.5)
            membro = Membro(nome)
            biblioteca.add_membro(membro)
            print(membro)
            print(biblioteca)

        elif user_escolha == "3":
            print('\n\n_____________BIBLIOTECA_______________\n\n')
            print('\n\nOpção: "Emprestimo Livro..."\n')
            nome_livro = input('digite o nome do livro: ')
            nome_pessoa = input('\ndigite seu nome: ')
            titulo = nome_livro.lower()
            nome = nome_pessoa.lower()
            emprestimo = biblioteca.emprestar_livro(titulo,nome)
        
        else:
            print('escolhe um numero burro.')
            exit()   
main()

