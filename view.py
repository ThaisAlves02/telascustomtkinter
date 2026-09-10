import customtkinter as ctk
from tkinter import ttk, messagebox


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

ctk.CTkButton(frame_botoes, text="Adicionar",
              fg_color="#2e7d32", hover_color="#1b5e20").pack(side="left", padx=5, pady=10)
ctk.CTkButton(frame_botoes, text="Atualizar",
              fg_color="#f9a825", hover_color="#f57f17").pack(side="left", padx=5, pady=10)
ctk.CTkButton(frame_botoes, text="Excluir",
              fg_color="#c62828", hover_color="#8e0000").pack(side="left", padx=5, pady=10)
ctk.CTkButton(frame_botoes, text="Limpar Campos",
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

#funçoes de apoio para o controller

def obter_dados_formulario():
    return {
        "nome": entry_nome.get(),
        "telefone":entry_telefone.get(),
        "email":entry_email.get()    
    }

def atualizar_tabela(contatos):
    for item in tree.get_children():
            tree.delete(item)
    
    for c in contatos:
            tree.insert(
                "", "end", iid=str(c["id"]),
                values=(c["nome"], c["telefone"], c["email"], c["data_cadastro"])
            )



janela.mainloop()