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
    
    except sqlite3. Error as erro:
        print(f"Houve um erro: {erro}")
    finally:
        conexao.close()
    

def inserir_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VAlUES (?, ?, ?)", (nome, preco, quantidade))
    conexao.commit()


def buscar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    dados = cursor.fetchall()

    conexao.close()
    return dados


def atualizar_preco(id_produto,novo_preco):
    nomes = buscar_produtos()

    for nome in nomes:
        texto = f"ID: {nome[0]} | Nome:{nome[1]} | preco:{nome[2]} | quantidade:{nome[3]}"


def deletar_produtos(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id =?")
    conexao.commit()


if __name__ == "__main__":
    criar_tabela()