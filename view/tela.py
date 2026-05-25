import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller.controle import processar_cadastro, excluir_produto, atualizar_vitrine
from model.modelo import buscar_produtos


def btn_verificar_salvar():
    nome_digitado = cx_nome.get()
    preco_digitado = cx_preco.get()
    quant_digitado = cx_quant.get()

    if processar_cadastro(nome_digitado, preco_digitado, quant_digitado):
        lbl_aviso.configure(text="Produto cadastrado com sucesso!", text_color="green")
        atualizar()
    else:
        lbl_aviso.configure(text="Preencha os campos corretamente!", text_color="red")
    cx_nome.delete(0, "end")
    cx_preco.delete(0, "end")
    cx_quant.delete(0, "end")
    
    grafico()

def excluir():
    id_digitado = cx_excluir_id.get()
    if excluir_produto(id_digitado):
        lbl_aviso.configure(text="Produto excluido com sucesso!", text_color="green")
        atualizar()
    else:
        lbl_aviso.configure(text="ID não encontrado!!", text_color="red")

    cx_excluir_id.delete(0, "end")

    grafico()

def atualizar():
    area_lista.delete("0.0", "end")

    texto = atualizar_vitrine()

    area_lista.insert("end", texto)

def grafico():
    for widget in frame_grafico.winfo_children():
         widget.destroy()

    dados = buscar_produtos()

    nome = []
    preco = []
    quantidade = []

    for dado in dados:
        nome.append(dado[1])
        preco.append(dado[2])
        quantidade.append(dado[3])

    figura, ax = plt.subplots(figsize=(7, 5))

    barras = ax.bar(nome, preco)

    ax.set_title("preco dos produtos")
    ax.set_xlabel("nome")
    ax.set_ylabel("preco")

    for barra in barras:

            altura = barra.get_height()

            ax.text(
                barra.get_x() + barra.get_width()/2,
                altura,
                f'R$ {altura:.2f}',
                ha='center',
                va='bottom'
            )
    
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", padx=10)

    plt.close(figura)

    figura, ax = plt.subplots(figsize=(7, 5))

    barras = ax.bar(nome, quantidade)

    ax.set_title("quantidade de produtos")
    ax.set_xlabel("nome")
    ax.set_ylabel("quantidade")

    for barra in barras:

            altura = barra.get_height()

            ax.text(
                barra.get_x() + barra.get_width()/2,
                altura,
                f"{int(altura)}",
                ha='center',
                va='bottom'
            )
    
    canvas = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side="right", padx=10)

    plt.close(figura)
    


def janela_principal():
    global frame_grafico, area_lista, lbl_aviso, cx_excluir_id, cx_nome, cx_preco, cx_quant

    janela = ctk.CTk()
    janela.geometry("1200x700")
    janela.title("Inventario de Produtos")

    form = ctk.CTkFrame(janela)
    form.pack(side="left", fill="both", expand=True, padx=10, pady=10)


    titulo = ctk.CTkLabel(form,text="Inventario de Produtos",font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    cx_nome = ctk.CTkEntry(form,placeholder_text="Nome")
    cx_nome.pack(pady=10)


    cx_preco = ctk.CTkEntry(form, placeholder_text="preco")
    cx_preco.pack(pady=10)


    cx_quant = ctk.CTkEntry(form, placeholder_text="quantidade")
    cx_quant.pack(pady=10)

    lbl_aviso = ctk.CTkLabel(form, text="")
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


    gravar_produto = ctk.CTkButton(form,
        text="cadastrar produto", 
        command=btn_verificar_salvar

    )
    gravar_produto.pack(pady=20)

    cx_excluir_id = ctk.CTkEntry(form, placeholder_text="ID p/ excluir ")
    cx_excluir_id.pack(pady=5)

    btn_excluir = ctk.CTkButton(
        form,text="excluir Produto",
        fg_color="red", hover_color="darkred",
        command=excluir
        )
    btn_excluir.pack(pady=20)


    frame_grafico = ctk.CTkFrame(janela)
    frame_grafico.pack(fill="both", expand=True, padx=10, pady=10)

    btn_gerar_grafico = ctk.CTkButton(
        form, 
        text="ver gráfico",
        command=grafico
    )
    btn_gerar_grafico.pack(pady=20)

    atualizar()

    janela.mainloop()


