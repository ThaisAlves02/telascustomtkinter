 
import os
import re
import json
from datetime import datetime
 
NOME_ARQUIVO = "contatos.json"
 
 
def carregar_contatos():
    """Lê o contatos.json e devolve a lista de contatos (cria o arquivo se não existir)."""
    if not os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)
 
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)
 
 
def salvar_contatos(lista_contatos):
    """Grava a lista de contatos inteira no contatos.json."""
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista_contatos, f, indent=4, ensure_ascii=False)
 
 
def validar_email(email):
    padrao = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None
 
 
def validar_telefone(telefone):
    padrao = r"^(\(\d{2}\)\s?)?\d{4,5}-?\d{4}$"
    return re.match(padrao, telefone) is not None
 
 
def adicionar_contato(nome, telefone, email):
    """Cria um novo contato e salva. Devolve o contato criado."""
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
    return novo_contato
 
 
def atualizar_contato(id_contato, nome, telefone, email):
    """Encontra o contato pelo id e atualiza seus dados. Devolve True se encontrou, False se não."""
    contatos = carregar_contatos()
 
    for c in contatos:
        if c["id"] == id_contato:
            c["nome"] = nome
            c["telefone"] = telefone
            c["email"] = email
            salvar_contatos(contatos)
            return True
 
    return False
 
 
def excluir_contato(id_contato):
    """Remove o contato com o id informado. Devolve True se removeu, False se não encontrou."""
    contatos = carregar_contatos()
    tamanho_antes = len(contatos)
 
    contatos = [c for c in contatos if c["id"] != id_contato]
    salvar_contatos(contatos)