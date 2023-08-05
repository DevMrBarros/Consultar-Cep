# Importando as bibliotecas necessárias.
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import *
import requests

# Criando a tela principal.
window = ctk.CTk()
window.title('Consultar CEP')
window.geometry('500x500')
window.transient()
window._set_appearance_mode('light')

def limpar_window():
    window.destroy()
    

def search_address():
    cep = cep_entry.get()

    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    # Checa se o campo CEP está vazio.
    if cep == "":
        messagebox.showinfo("Erro", "Preencha o CEP.")
        return

    # Checa se contém caracteres não númericos.
    if not cep.isdigit():
        messagebox.showwarning("Erro", "CEP inválido!")
        return

    link = f"https://viacep.com.br/ws/{cep}/json/"

    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()

    # Checa se o CEP não for encontrado.
    if "erro" in dic_requisicao:
        messagebox.showwarning("Erro", "CEP não encontrado!")
        return

    uf = dic_requisicao["uf"]
    cidade = dic_requisicao["localidade"]
    rua = dic_requisicao["logradouro"]
    bairro = dic_requisicao["bairro"]
    
    rua_var.set(rua)
    bairro_var.set(bairro)
    uf_var.set(uf)
    cidade_var.set(cidade)

# Criar a label e entry CEP.
cep_label = ctk.CTkLabel(window, text='Digite o CEP:')
cep_label.pack()
cep_entry = ctk.CTkEntry(window)
cep_entry.pack(pady=5)

# Criar o botão "Consultar"
consultar_button = ctk.CTkButton(window,
                                text="Consultar",
                                command=search_address
                                )
consultar_button.pack(pady=5)

# Criando os objetos Stringvars.
rua_var = ctk.StringVar()
bairro_var = ctk.StringVar()
uf_var = ctk.StringVar()
cidade_var = ctk.StringVar()

# Criando as entries e labels dos objetos StringVar.
rua_label = ctk.CTkLabel(window, text='Rua:')
rua_entry = ctk.CTkEntry(window, textvariable=rua_var, width=200)
bairro_label = ctk.CTkLabel(window, text='Bairro:')
bairro_entry = ctk.CTkEntry(window, textvariable=bairro_var, width=200)
uf_label = ctk.CTkLabel(window, text='UF:')
uf_entry = ctk.CTkEntry(window, textvariable=uf_var, width=200)
cidade_label = ctk.CTkLabel(window, text='Cidade:')
cidade_entry = ctk.CTkEntry(window, textvariable=cidade_var, width=200)

# Posicionando os widgets na tela.
rua_label.pack()
rua_entry.pack(pady=5)
bairro_label.pack()
bairro_entry.pack(pady=5)
uf_label.pack()
uf_entry.pack(pady=5)
cidade_label.pack()
cidade_entry.pack(pady=5)

# Função limpar campos.
def limpar_window():
    cep_entry.delete(0, tk.END)    
    rua_entry.delete(0, tk.END)
    bairro_entry.delete(0, tk.END)
    uf_entry.delete(0, tk.END)    
    cidade_entry.delete(0, tk.END)
    
def fechar_window():
    window.destroy()

# Botão "Fechar".
fechar_button = ctk.CTkButton(window, text='Fechar', command=fechar_window)
fechar_button.pack(pady=5)

# Botão "Sair".
limpar_button = ctk.CTkButton(window, text="Limpar", command=limpar_window)
limpar_button.pack(pady=5)

# Loop da tela principal.
window.mainloop()
