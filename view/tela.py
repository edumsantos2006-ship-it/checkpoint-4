import customtkinter as ctk
from controller.controle import processar_cadastro



janela = ctk.CTk()
janela.geometry("700x500")
janela.title("Inventario de Produtos")

form = ctk.CTkFrame(janela)
form.pack(side="left", fill="both", expand=True, padx=10, pady=10)


titulo = ctk.CTkLabel(janela,text="Inventario de Produtos",font=("Arial", 22, "bold"))
titulo.pack(pady=20)

lbl_nome = ctk.CTkLabel(janela,placeholder_text="Nome")
lbl_nome.pack(pady=10)


lbl_preco = ctk.CTkLabel(janela, placeholder_text="preco")
lbl_preco.pack(pady=10)


lbl_quant = ctk.CTkLabel(janela, placeholder_text="quantidade")
lbl_quant.pack(pady=10)


lista = ctk.CTkFrame(janela)
lista.pack(side="right", fill="both",expand=True, padx=10, pady=10)

t_lista = ctk.CTkLabel(lista, text="Produtos", font=("Arial", 20, "bold"))
t_lista.pack(pady=10) 

area_lista = ctk.CTkTextbox(
    janela,
    width=350,
    height=150
)
area_lista.pack(pady=10)

botao = ctk.CTkButton(janela, text="cadastrar produto", command=processar_cadastro)
botao.pack(pady=20)

janela.mainloop()


