import customtkinter as ctk
from controller.controle import processar_cadastro

def btn_verificar_salvar():
    nome_digitado = cx_nome.get()
    preco_digitado = cx_preco.get()
    quant_digitado = cx_quant.get()

    if processar_cadastro(nome_digitado, preco_digitado, quant_digitado):
        lbl_aviso.configure(text="Produto cadastrado com sucesso!", text_color="green")
    else:
        lbl_aviso.configure(text="O nome do produto não pode estar vazio!", text_color="red")

janela = ctk.CTk()
janela.geometry("700x500")
janela.title("Inventario de Produtos")

form = ctk.CTkFrame(janela)
form.pack(side="left", fill="both", expand=True, padx=10, pady=10)


titulo = ctk.CTkLabel(janela,text="Inventario de Produtos",font=("Arial", 22, "bold"))
titulo.pack(pady=20)

cx_nome = ctk.CTkEntry(form,placeholder_text="Nome")
cx_nome.pack(pady=10)


cx_preco = ctk.CTkEntry(form, placeholder_text="preco")
cx_preco.pack(pady=10)


cx_quant = ctk.CTkEntry(form, placeholder_text="quantidade")
cx_quant.pack(pady=10)

lbl_aviso = ctk.CTkLabel(janela, text="")
lbl_aviso.pack(pady=5)


lista = ctk.CTkFrame(janela)
lista.pack(side="right", fill="both",expand=True, padx=10, pady=10)

t_lista = ctk.CTkLabel(lista, text="Produtos", font=("Arial", 20, "bold"))
t_lista.pack(pady=10) 

area_lista = ctk.CTkTextbox(
    lista,
    width=350,
    height=150
)
area_lista.pack(pady=10)

gravar_produto = ctk.CTkButton(janela,
    text="cadastrar produto", 
    command=btn_verificar_salvar

 )
gravar_produto.pack(pady=20)

cx_excluir_id = ctk.CTkEntry(form, placeholder_text="ID p/ excluir ")
cx_excluir_id.pack(pady=5)

btn_excluir = ctk.CTkButton(
    form,text="exluir Produto",
    fg_color="red", hover_color="darkred",
    )
btn_excluir.pack(pady=20)

janela.mainloop()




