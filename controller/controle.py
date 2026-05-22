from model.modelo import inserir_produto, deletar_produtos, atualizar_preco, buscar_produtos

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
 
    deletar_produtos(id_dig)
    return True
    
def atualizar_vitrine():
    nomes = buscar_produtos()
    texto = ""

    for nome in nomes:
        texto = f"ID: {nome[0]} | Nome:{nome[1]} | preco:{nome[2]} | quantidade:{nome[3]}\n"
    
    return texto
