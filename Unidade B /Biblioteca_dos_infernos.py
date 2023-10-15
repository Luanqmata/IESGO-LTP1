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
        return(f"    Nome: {self.nome} Registrado no Sistema. \n\n     Quantidade de Livros emprestados {len(self.livros_emprestados)}\n")
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
        print(f'\n\nO livro foi adicionado à Biblioteca:')
        time.sleep(1)
        
    def add_membro(self, membro):
        nome_membro = membro.nome
        time.sleep(0.5)
        self.membros[nome_membro] = membro #manda pro self.membros porém se o nome for igual ele nao acumula tem q colocar nme e sobrenome 
        print('\n\n_____________BIBLIOTECA_______________')
        print(f'\n\nO membro Foi adicionado com Sucesso!\n')
        time.sleep(0.5)
        
    def emprestar_livro(self, livro_escolhido, nome_membro):
        if livro_escolhido in self.livros and nome_membro in self.membros:# checka se o parametro estiver dentro da bibliteca self.livros
            emprestimo = self.livros.get(livro_escolhido) # busca o parametro passado dentro da biblioteca 
            membro = self.membros.get(nome_membro) # busca o parametro passado dentro da biblioteca
            if emprestimo.status == 'disponivel': # e o item buscado dentro da biblioteca estiver disponivel na leitura do self.status
                emprestimo.status = 'emprestado' # retorna q o status dele é 'emprestado' agora 
                membro.livros_emprestados.append(emprestimo)# adiciona dentro da classe com .membro , e dentro da lista da classe membro com .append , q é o titulo do livro 
                #membro.livros_emprestados.append(membro) 
                print(f'\nO Membro: "{nome_membro.title()}" , Pegou o livro: "{livro_escolhido.title()}" STATUS: {emprestimo.status}.\n\n')
            else:
                print(f'\nO livro "{emprestimo.titulo}" não está disponível.\n\n')# se o item nao estiver diponivel
        else:
            print(f'\nO livro "{livro_escolhido.title()}" ou o "{nome_membro.title()}" não existe nessa Biblioteca .\n\n') #retornara que o livro não esta na biblitoeca 
    
    
    def devolver_livro(self, livro_devolvido, nome_pessoa): # msm coisa da de cima so q reversa 
        if livro_devolvido in self.livros and nome_pessoa in self.membros:
            devolucao = self.livros.get(livro_devolvido) 
            membro = self.membros.get(nome_pessoa)
            if devolucao.status == 'emprestado':  
                devolucao.status = 'disponivel'
                membro.livros_emprestados.remove(devolucao)
                #membro.livros_emprestados.remove(membro)  
                print(f'\n\nO livro "{livro_devolvido.title()}" foi devolvido por {nome_pessoa.title()} para a biblioteca com sucesso  STATUS: {devolucao.status}.\n')
            else:
                print(f'\n\nO livro "{livro_devolvido.title()}" não está emprestado ou não está emprestado para {nome_pessoa.title()}.\n')
        else:
            print(f'\n\nO livro "{livro_devolvido.title()}" ou o membro "{nome_pessoa.title()}" não fazem parte do cadastro do sistema.\n')

    def remover_livro(self,nome_do_livro):
        if nome_do_livro in self.livros:
            time.sleep(0.5)
            del self.livros[nome_do_livro]
            print(f'\n\nO livro: {nome_do_livro.title()} Foi Excluido Da Biblioteca.')
    
    def remover_membro(self,nome):
        if nome in self.membros:
            time.sleep(0.5)
            del self.membros[nome]
            print(f'\n\nO livro: {nome.title()} Foi Excluido Da lista de membros.')
     
    def pesquisa_nome_livros(self,nome_livro):
        if nome_livro in self.livros:
            print('\n\nO livro se encontra "DISPONIVEL" na Biblioteca.')
        else:
            print('\n\nO livro se encontra "INDISPONIVEL" na Biblioteca.')
            
    def pesquisa_nome_membros(self,nome_membro):
        if nome_membro in self.membros:
            print('\nO membro se encontra REGISTRADO em nossos Sistemas.')
        else:
            print('\nO membro se encontra NÃO REGISTRADO em nossos Sistemas.')
            
def main():
    biblioteca = Biblioteca()

    while True:
        print('\n\n____________BEM_VINDO_____________')
        print("\nOpções:")
        print("1. Adicionar Um Livro Novo")
        print("2. Registrar Membro Novo")
        print("3. Emprestar Um Livro")
        print("4. Devolver Um Livro")
        print('5. Remover um Livro.')
        print('6. Remover um Membro.')
        print('7. Pesquisa Livro por Nome.')
        print('8. Pesquisa Membro por Nome e Sobrenome.')
        print('9. Sair.')

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
            print(membro)
        
        elif user_escolha == "4":
            print('\n\n_____________BIBLIOTECA_______________\n\n')
            print('\n\nOpção: "DEVOLUÇÃO Livro..."\n')
            livro_devolucao = input('digite o nome do livro: ')
            nome_pessoa = input('\ndigite seu nome: ')
            titulo = livro_devolucao.lower()
            nome = nome_pessoa.lower()
            devolucao = biblioteca.devolver_livro(titulo,nome)
            print(membro)
        
        elif user_escolha == '5':
            print('\n\n_____________BIBLIOTECA_______________\n\n')
            print('\n\nOpção: "Remover Livro..."\n')
            nome = input('\nDigite o nome do livro: "(Da Biblioteca)"')
            nome_livro = nome.lower()
            del_nome_livro = biblioteca.remover_livro(nome_livro)
            time.sleep(0.5)
            print(biblioteca)
            
        elif user_escolha == '6':
            print('\n\n_____________BIBLIOTECA_______________\n\n')
            print('\n\nOpção: "Remover Membro..."\n')
            nome = input('\nDigite o seu Nome e Sobrenome: ')
            nome_pessoa = nome.lower()
            del_nome_pessoa = biblioteca.remover_membro(nome_pessoa)
            time.sleep(0.5)
            print(biblioteca)
        
        elif user_escolha == '7':
            print('\n\n_____________BIBLIOTECA_______________\n\n')
            print('\n\nOpção: "Pesquisa por Nome... LIVROS "\n')
            nome = input("Digite o nome do livro: ")
            time.sleep(1)
            nome_livro = nome.lower()
            pesquisa = biblioteca.pesquisa_nome_livros(nome_livro)
        
        elif user_escolha == '8':
            print('\n\n_____________BIBLIOTECA_______________\n\n')
            print('\n\nOpção: "Pesquisa por Nome... in Membros "\n')
            nome = input("Digite o nome e Sobrenome: ")
            time.sleep(1)
            nome_membro = nome.lower()
            pesquisa = biblioteca.pesquisa_nome_membros(nome_membro)
        
        elif user_escolha == '9':  
            print('.')
            time.sleep(0.5)
            print('..')
            time.sleep(0.5)
            print('...')
            time.sleep(0.5)
            print('\n\tVOCE SAIU.\n\tADEUS.') 
        
        else:
            print('escolhe um numero entre 1 e 9.')
            exit()
         
main()

"""                                         2°metodo de fazer - emprestar livro  
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
