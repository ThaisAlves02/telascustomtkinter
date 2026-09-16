"""
CRUD DE CONTATOS - Tela (front-end)
------------------------------------

O "banco de dados" é um arquivo JSON chamado contatos.json.

Cada contato deve ter:
    - nome
    - telefone
    - email
    - data_cadastro   (preenchida automaticamente com datetime)
"""

import customtkinter as ctk
from tkinter import ttk, messagebox

# Bibliotecas que vocês vão usar no back-end:
import os
import re
import json
from datetime import datetime

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

NOME_ARQUIVO = "contatos.json"

# Guarda o id do contato selecionado na lista (None = nenhum selecionado)
contato_selecionado_id = None


# ------------------------------------------------------------------
# BACK-END - IMPLEMENTEM AS FUNÇÕES ABAIXO
# ------------------------------------------------------------------

def carregar_contatos():
    # Se o arquivo ainda não existe, cria com uma lista vazia
    if not os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_contatos(lista_contatos):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista_contatos, f, indent=4, ensure_ascii=False)


def validar_email(email):
    padrao = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None


def validar_telefone(telefone):
    padrao = r"^(\(\d{2}\)\s?)?\d{4,5}-?\d{4}$"
    return re.match(padrao, telefone) is not None


def adicionar_contato():
    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()
    email = entry_email.get().strip()

    if not nome or not telefone or not email:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if not validar_email(email):
        messagebox.showerror("Erro", "Email inválido. Use o formato nome@dominio.com")
        return

    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido. Use (85) 99999-9999 ou 85999999999")
        return

    contatos = carregar_contatos()

    novo_id = max([c["id"] for c in contatos], default=0) + 1
    novo_contato = {
        "id": novo_id,
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

    contatos.append(novo_contato)
    salvar_contatos(contatos)
    listar_contatos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")


def listar_contatos():
    # Limpa a treeview
    for item in tree.get_children():
        tree.delete(item)

    contatos = carregar_contatos()
    for c in contatos:
        tree.insert(
            "", "end", iid=str(c["id"]),
            values=(c["nome"], c["telefone"], c["email"], c["data_cadastro"])
        )


def selecionar_contato(event):
    global contato_selecionado_id

    selecionado = tree.selection()
    if not selecionado:
        return

    item_id = selecionado[0]
    valores = tree.item(item_id, "values")

    entry_nome.delete(0, "end")
    entry_nome.insert(0, valores[0])

    entry_telefone.delete(0, "end")
    entry_telefone.insert(0, valores[1])

    entry_email.delete(0, "end")
    entry_email.insert(0, valores[2])

    contato_selecionado_id = int(item_id)


def atualizar_contato():
    if contato_selecionado_id is None:
        messagebox.showwarning("Aviso", "Selecione um contato na lista para atualizar.")
        return

    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()
    email = entry_email.get().strip()

    if not nome or not telefone or not email:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if not validar_email(email):
        messagebox.showerror("Erro", "Email inválido. Use o formato nome@dominio.com")
        return

    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido. Use (85) 99999-9999 ou 85999999999")
        return

    contatos = carregar_contatos()
    for c in contatos:
        if c["id"] == contato_selecionado_id:
            c["nome"] = nome
            c["telefone"] = telefone
            c["email"] = email
            break

    salvar_contatos(contatos)
    listar_contatos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")


def excluir_contato():
    if contato_selecionado_id is None:
        messagebox.showwarning("Aviso", "Selecione um contato na lista para excluir.")
        return

    confirmar = messagebox.askyesno("Confirmar exclusão", "Tem certeza que deseja excluir este contato?")
    if not confirmar:
        return

    contatos = carregar_contatos()
    contatos = [c for c in contatos if c["id"] != contato_selecionado_id]

    salvar_contatos(contatos)
    listar_contatos()
    limpar_campos()


def limpar_campos():
    entry_nome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")
    global contato_selecionado_id
    contato_selecionado_id = None


# ------------------------------------------------------------------
# INTERFACE (já pronta, não precisa mexer aqui)
# ------------------------------------------------------------------

janela = ctk.CTk()
janela.title("Cadastro de Contatos")
janela.geometry("650x500")
janela.resizable(False, False)

# --- Formulário ---
frame_form = ctk.CTkFrame(janela)
frame_form.pack(padx=20, pady=15, fill="x")

ctk.CTkLabel(frame_form, text="Nome:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
entry_nome = ctk.CTkEntry(frame_form, width=250, placeholder_text="Ex: Maria Silva")
entry_nome.grid(row=0, column=1, padx=10, pady=8)

ctk.CTkLabel(frame_form, text="Telefone:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
entry_telefone = ctk.CTkEntry(frame_form, width=250, placeholder_text="Ex: (85) 99999-9999")
entry_telefone.grid(row=1, column=1, padx=10, pady=8)

ctk.CTkLabel(frame_form, text="Email:").grid(row=2, column=0, padx=10, pady=8, sticky="w")
entry_email = ctk.CTkEntry(frame_form, width=250, placeholder_text="Ex: maria@email.com")
entry_email.grid(row=2, column=1, padx=10, pady=8)

# --- Botões ---em
frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(padx=20, pady=5, fill="x")

ctk.CTkButton(frame_botoes, text="Adicionar", command=adicionar_contato,
              fg_color="#2e7d32", hover_color="#1b5e20").pack(side="left", padx=5, pady=10)
ctk.CTkButton(frame_botoes, text="Atualizar", command=atualizar_contato,
              fg_color="#f9a825", hover_color="#f57f17").pack(side="left", padx=5, pady=10)
ctk.CTkButton(frame_botoes, text="Excluir", command=excluir_contato,
              fg_color="#c62828", hover_color="#8e0000").pack(side="left", padx=5, pady=10)
ctk.CTkButton(frame_botoes, text="Limpar Campos", command=limpar_campos,
              fg_color="gray40", hover_color="gray30").pack(side="left", padx=5, pady=10)

# --- Lista de contatos (Treeview) ---
frame_lista = ctk.CTkFrame(janela)
frame_lista.pack(padx=20, pady=15, fill="both", expand=True)

colunas = ("nome", "telefone", "email", "data_cadastro")
tree = ttk.Treeview(frame_lista, columns=colunas, show="headings", height=10)

tree.heading("nome", text="Nome")
tree.heading("telefone", text="Telefone")
tree.heading("email", text="Email")
tree.heading("data_cadastro", text="Cadastrado em")

tree.column("nome", width=150)
tree.column("telefone", width=120)
tree.column("email", width=180)
tree.column("data_cadastro", width=140)

tree.pack(fill="both", expand=True, padx=5, pady=5)
tree.bind("<<TreeviewSelect>>", selecionar_contato)

# Carrega a lista assim que a tela abre
listar_contatos()

janela.mainloop()