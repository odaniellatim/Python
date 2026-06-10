import os
import random
from materiais import Materiais
from orcamento_projeto import OrcamentoProjeto
from projetos import Projetos


def divider(headline):
    print("\n")
    print("-" * 70)
    print(headline.upper())
    print("-" * 70)


if __name__ == "__main__":
    os.system("clear")

    item1 = Materiais(1, "Tinta Branca", 33.33, 90, "g")

    divider("MATERIAIS: Listar Itens cadastrados")
    item1.mt_listar_materiais()

    divider("Valor Total material usado projeto")

    total_projeto = item1.mt_valor_quantidade_projeto(10)
    print("Valor total qntd_material projeto: R$ ", round(total_projeto, 2))

    divider("MATERIAIS: Valor da grama do material")

    valor_grama = item1.mt_valor_unidade_medida()
    print("Valor total grama: R$ ", round(valor_grama, 2))

    divider("MATERIAIS: Alterar o status do material")
    selecionar_material = item1.mt_selecionar_produto(1)
    print(selecionar_material)

    divider("Listar Itens cadastrados")
    item1.mt_listar_materiais()

    divider("Classe Orcamento Projeto")
    orcamento = OrcamentoProjeto(1, "Pintura Tênis X")

    # opt = 0
    # while opt != 1:
    #     if opt == "1":
    #         opt = 1
    #     else:
    #         divider("Adicionar Materiais")
    #         id_produto = random.randint(0, 10000)
    #         nome_produto = input("Informe o nome do produto: ")
    #         preco_produto = input("Informe o preco do produto: ")
    #         quantidade_produto = input("Informe a quantidade da embalagem: ")
    #         unidade_medida_produto = input("Informe a unidade de medida (kg, g, mm): ")

    #         orcamento.oc_adicionar_materiais(
    #             id_produto,
    #             nome_produto,
    #             float(preco_produto),
    #             int(quantidade_produto),
    #             unidade_medida_produto,
    #         )

    divider("Listar materais cadastrados")
    orcamento.oc_listar_materiais_cadastrados()

    #         print("\n")

    #         opt = input("Digite 1 para encerrar")
    # divider("Orcamento: Listar materais cadastrados")
    # orcamento.oc_listar_materiais_cadastrados()

    projeto1 = Projetos()
    projeto1.pj_adicionar_projeto("Tenis X")
