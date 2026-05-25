from model.modelo import inserir_produto, deletar_produto, atualizar_preco, buscar_produtos

def processar_cadastro(nome, preco_txt, quant_txt):
    if nome == "" or preco_txt == "" or quant_txt == "":
        print("Erro: Campo está vazio")
        return False
    try:
        preco = float(preco_txt)
        quantidade = int(quant_txt)
    except ValueError:
        print("Erro nos números!!")
        return False

    inserir_produto(nome, preco, quantidade)
    return True


def excluir_produto(id_dig):
    if id_dig == "": 
        print("Erro")
        return False
    try:
        id_dig = int(id_dig)
    except ValueError:
        print("ID invalido")
        return False
    
    linhas_afetadas = deletar_produto(id_dig)
    
    if linhas_afetadas == 0:
        print("ID não encontrado")
        return False
    
    return True
    
def atualizar_vitrine():
    produtos = buscar_produtos()
    texto = ""

    for produto in produtos:
        texto += f"ID: {produto[0]} | Nome:{produto[1]} | preco:{produto[2]} | quantidade:{produto[3]}\n"
    
    return texto

def alterar_preco(id_txt, novo_preco_txt):

    if id_txt == "" or novo_preco_txt == "":
        return False

    try:
        id_produto = int(id_txt)
        novo_preco = float(novo_preco_txt)

    except ValueError:
        return False

    atualizar_preco(id_produto, novo_preco)

    return True