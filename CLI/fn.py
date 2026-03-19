import os
import json
from argparse import ArgumentParser
import fmt

def item(nome, medida, quantidade, preco):
    # Função que gerar os dados organizados em um dicionario
    if (nome is None or medida is None or medida is None):
        exit()
    return {
        "nome": nome,
        "medida": medida,
        "quantidade": quantidade,
        "preco": preco
    }


def f_obj(lista_items: list):
    total_items = len(lista_items)
    valor_total = 0
    valor_proporcao = 0
    count = 0

    # Função que formata a impressão dos dados na tela.
    fmt.draw_table(4, lista_items)
    #fmt.tabela_vertical((len(lista_items) +1), lista_items)
    
    for value in lista_items:
        valor_total += value['preco']
        valor_proporcao += value['preco']/value['quantidade']

    resumo_compras = [
        {
            "valor_total": str(round(valor_total, 2)),
            "valor_total_proporcao": str(round(valor_proporcao, 2)),
        }
    ]
    fmt.tabela_vertical((len(resumo_compras) + 1), resumo_compras)


def run():
    # Função que inicia o argparse para receber os argumentos
    # limpa a tela quanto um comando é enviado
    os.system("clear")

    return ArgumentParser(
        prog="DP >> ",
        usage="Controle de despesas",
        description="""
        Transforma o valor do produto pegando
        sua quantidade, seja em {g, kg, l, unidade} e transforma
        em valor (R$) em uma proporção menor de uso.
        """,
        epilog="Criado por Daniel Latim",
    )


def listar_items(file_name):
    i = []

    if (os.path.exists(file_name)):
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                db = json.load(f)
                if isinstance(db, list):
                    i = db
                else:
                    i = [db]
            except json.JSONDecodeError:
                i = []

    return i


def save(data: dict, file_name: str) -> str | None:
    with open(file_name, "w", encoding="utf-8") as f:
        db_json = json.dumps(data, indent=2, sort_keys=True)
        f.write(db_json)
        fmt.tabela_vertical(2, alerta("Dados salvos com sucesso"))


def alerta(msg):
    return [
        {
            "mensagem": msg
        }
    ]
