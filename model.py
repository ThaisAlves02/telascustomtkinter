import os
import re
import json
from datetime import datetime

NOME_ARQUIVO = "contatos.json"

contato_selecionado_id = None

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


def adicionar_contato(nome,telefone,email):
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

def atualizar_contato(id_contato, nome, telefone,email):
    contatos = carregar_contatos()
    
    for c in contatos:
        if c["id"] == id_contato:
            c["nome"] = nome
            c["telefone"] = telefone
            c["email"] = email
            salvar_contatos(contatos)
            break

def excluir_contato(id_contato):
    contatos = carregar_contatos()
    contatos = [c for c in contatos if c["id"] != id_contato]
    
    salvar_contatos(contatos)