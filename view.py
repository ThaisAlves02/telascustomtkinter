import customtkinter as ctk
from tkinter import ttk, messagebox
 
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
 
# ------------------------------------------------------------------
# Construção da janela e dos widgets
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
 
# --- Botões (sem "command=" — o controller que vai conectar) ---
frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(padx=20, pady=5, fill="x")
 
btn_adicionar = ctk.CTkButton(frame_botoes, text="Adicionar",
                               fg_color="#2e7d32", hover_color="#1b5e20")
btn_adicionar.pack(side="left", padx=5, pady=10)
 
btn_atualizar = ctk.CTkButton(frame_botoes, text="Atualizar",
                               fg_color="#f9a825", hover_color="#f57f17")
btn_atualizar.pack(side="left", padx=5, pady=10)
 
btn_excluir = ctk.CTkButton(frame_botoes, text="Excluir",
                             fg_color="#c62828", hover_color="#8e0000")
btn_excluir.pack(side="left", padx=5, pady=10)
 
btn_limpar = ctk.CTkButton(frame_botoes, text="Limpar Campos",
                            fg_color="gray40", hover_color="gray30")
btn_limpar.pack(side="left", padx=5, pady=10)
 
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
# repare que NÃO tem tree.bind() aqui — quem faz o bind é o controller,
# porque é ele que decide qual função roda quando o usuário seleciona um contato
 
 
# ------------------------------------------------------------------
# Funções de apoio — é por aqui que o controller conversa com a tela
# ------------------------------------------------------------------
 
def obter_dados_formulario():
    """Devolve o que está escrito nos campos agora, como um dicionário."""
    return {
        "nome": entry_nome.get().strip(),
        "telefone": entry_telefone.get().strip(),
        "email": entry_email.get().strip(),
    }
 
 
def preencher_formulario(nome, telefone, email):
    """Preenche os campos do formulário com os dados de um contato."""
    entry_nome.delete(0, "end")
    entry_nome.insert(0, nome)
 
    entry_telefone.delete(0, "end")
    entry_telefone.insert(0, telefone)
 
    entry_email.delete(0, "end")
    entry_email.insert(0, email)
 
 
def limpar_formulario():
    entry_nome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")
 
 
def atualizar_tabela(contatos):
    """Recebe a lista de contatos e redesenha a Treeview do zero."""
    for item in tree.get_children():
        tree.delete(item)
 
    for c in contatos:
        tree.insert(
            "", "end", iid=str(c["id"]),
            values=(c["nome"], c["telefone"], c["email"], c["data_cadastro"])
        )
 
 
def obter_id_selecionado():
    """Devolve o iid (string) do contato selecionado na tabela, ou None se nada selecionado."""
    selecionado = tree.selection()
    if not selecionado:
        return None
    return selecionado[0]
 
 
def obter_valores_selecionados():
    """Devolve a tupla (nome, telefone, email, data) do item selecionado na tabela."""
    item_id = obter_id_selecionado()
    if item_id is None:
        return None
    return tree.item(item_id, "values")
 
 
def mostrar_erro(mensagem):
    messagebox.showerror("Erro", mensagem)
 
 
def mostrar_aviso(mensagem):
    messagebox.showwarning("Aviso", mensagem)
 
 
def mostrar_sucesso(mensagem):
    messagebox.showinfo("Sucesso", mensagem)
 
 
def confirmar(mensagem):
    return messagebox.askyesno("Confirmar", mensagem)

def abrir_janela():
    janela.mainloop()