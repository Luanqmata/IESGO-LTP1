import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('teste_prova.db')
    cursor = conexao.cursor()
    
    cursor.execute(" CREATE TABLE IF NOT EXISTS usuarios( id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL, idade INTEGER NOT NULL) ")
    
    conexao.commit()
    conexao.close()

def vizualizar_lista():
    conexao = sqlite3.connect('teste_prova.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
    
    print("\n Lista de usuarios: ")
    for row in rows:
        print(row)               
        
    conexao.close()

def adicionar_membro():
    nome = input('digite sei nome: ')
    idade = int(input('Digite sua idade: '))
    
    conexao = sqlite3.connect('teste_prova.db')
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO usuarios( nome , idade ) VALUES (?,?)",(nome,idade))
    
    conexao.commit()
    conexao.close()

def remover_membro():
    id_remover = int(input('Digite o ID da pessoa para remove-la: '))
    
    conexao = sqlite3.connect('teste_prova.db')
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM usuarios WHERE id = ?",(id_remover,))
    
    conexao.commit()
    conexao.close()
    print("O membro Foi removido com SUCESSO.")

if __name__ == "__main__":
    criar_tabela()    

    while True:
        user_escolha = int(input('Ipção:'))
        
        if user_escolha == 1:
            vizualizar_lista()
        elif user_escolha == 2:
            adicionar_membro()
        elif user_escolha == 3 :
            remover_membro()
        else:
            print('BURRO.')
