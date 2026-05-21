from model.modelo import inserir_produto

def processar_cadastro(nome, preco_txt, quant_txt):
    if nome == "" or preco_txt == "":
        print("Erro: Campo está vazio")
        return False
    try:
        preco = float(preco_txt)
        quantidade = int(quant_txt)
    except ValueError:
        print("Erro nos números!!")

    inserir_produto(nome, preco, quantidade)
    return True

