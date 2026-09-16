import model
import view
 
# Guarda o id do contato selecionado na tabela no momento (None = nenhum)
contato_selecionado_id = None
 
 
def listar_contatos():
    contatos = model.carregar_contatos()
    view.atualizar_tabela(contatos)
 
 
def adicionar_contato():
    dados = view.obter_dados_formulario()
 
    if not dados["nome"] or not dados["telefone"] or not dados["email"]:
        view.mostrar_erro("Preencha todos os campos.")
        return
 
    if not model.validar_email(dados["email"]):
        view.mostrar_erro("Email inválido. Use o formato nome@dominio.com")
        return
 
    if not model.validar_telefone(dados["telefone"]):
        view.mostrar_erro("Telefone inválido. Use (85) 99999-9999 ou 85999999999")
        return
 
    model.adicionar_contato(dados["nome"], dados["telefone"], dados["email"])
    listar_contatos()
    view.limpar_formulario()
    view.mostrar_sucesso("Contato adicionado com sucesso!")
 
 
def selecionar_contato(event):
    global contato_selecionado_id
 
    item_id = view.obter_id_selecionado()
    if item_id is None:
        return
 
    valores = view.obter_valores_selecionados()
    view.preencher_formulario(valores[0], valores[1], valores[2])
 
    contato_selecionado_id = int(item_id)
 
 
def atualizar_contato():
    global contato_selecionado_id
 
    if contato_selecionado_id is None:
        view.mostrar_aviso("Selecione um contato na lista para atualizar.")
        return
 
    dados = view.obter_dados_formulario()
 
    if not dados["nome"] or not dados["telefone"] or not dados["email"]:
        view.mostrar_erro("Preencha todos os campos.")
        return
 
    if not model.validar_email(dados["email"]):
        view.mostrar_erro("Email inválido. Use o formato nome@dominio.com")
        return
 
    if not model.validar_telefone(dados["telefone"]):
        view.mostrar_erro("Telefone inválido. Use (85) 99999-9999 ou 85999999999")
        return
 
    model.atualizar_contato(contato_selecionado_id, dados["nome"], dados["telefone"], dados["email"])
    listar_contatos()
    view.limpar_formulario()
    contato_selecionado_id = None
    view.mostrar_sucesso("Contato atualizado com sucesso!")
 
 
def excluir_contato():
    global contato_selecionado_id
 
    if contato_selecionado_id is None:
        view.mostrar_aviso("Selecione um contato na lista para excluir.")
        return
 
    if not view.confirmar("Tem certeza que deseja excluir este contato?"):
        return
 
    model.excluir_contato(contato_selecionado_id)
    listar_contatos()
    view.limpar_formulario()
    contato_selecionado_id = None
 
 
def limpar_campos():
    global contato_selecionado_id
    view.limpar_formulario()
    contato_selecionado_id = None
    
    
view.btn_adicionar.configure(command=adicionar_contato)
view.btn_atualizar.configure(command=atualizar_contato)
view.btn_excluir.configure(command=excluir_contato)
view.btn_limpar.configure(command=limpar_campos)
view.tree.bind("<<TreeviewSelect>>", selecionar_contato)


listar_contatos()

view.abrir_janela()