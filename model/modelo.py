import sqlite3

def conectar():
    return sqlite3.connect("inventario.db")


def criar_tabela():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   preco FLOAT,
                   quantidade INTEGER
               )
         """ )
        conexao.commit()
    
    except sqlite3.Error as erro:
        print(f"Houve um erro: {erro}")
    finally:
        conexao.close()
    

def inserir_produto(nome, preco, quantidade):
    with conectar() as conexao:

        cursor = conexao.cursor()
        cmd_sql = "INSERT INTO produtos (nome, preco, quantidade) VAlUES (?, ?, ?)"
        cursor.execute(cmd_sql, (nome, preco, quantidade))
        
        conexao.commit()



def buscar_produtos():
    with conectar() as conexao:

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtos")

        dados = cursor.fetchall()

        
    return dados


def atualizar_preco(id_produto,novo_preco):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?",(novo_preco, id_produto))
        
        conexao.commit()
    
def deletar_produto(id_dig):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM produtos WHERE id =?",(id_dig,))
        conexao.commit()

        return cursor.rowcount


if __name__ == "__main__":
    criar_tabela()