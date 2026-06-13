import os
from Save_in_file import Save_in_file

# import random
from orcamento_projeto import OrcamentoProjeto


def divider(headline):
    print("\n")
    print("-" * 70)
    print(headline.upper())
    print("-" * 70)


if __name__ == "__main__":
    os.system("clear")

    folder_name = "materiais"
    file_name = "materiais.json"
    data = Save_in_file(folder_name, file_name)

    orcamento = OrcamentoProjeto(1, "Pintura")
    item1 = orcamento.oc_adicionar_materiais(10, "Branco", 150.99, 90, "g")
    item2 = orcamento.oc_adicionar_materiais(150, "Turquesa", 145.99, 150, "g")
    # divider(f"Orcamento: {orcamento.oc_nome_orcamento()}")

    orcamento.oc_alterar_status(10)
    orcamento.oc_alterar_status(2)
    # lista_materiais = orcamento.oc_listar_materiais_projeto()

    # data.save_data(orcamento.oc_dicionario_save())
    removido = orcamento.oc_deletar_material(2)
    print(removido)

    items = orcamento.oc_listar_materiais()
    for oc in items:
        for key, value in oc.items():

            if key == "orcamento_materiais":
                for produto in value:
                    # print(produto)
                    print("-" * 70)
            else:
                print(key, value)
        print("-" * 70)

    # estoque = orcamento.oc_valor_total_estoque()
    # print(f"Estoque: {estoque}")
    # data = data.load_data(folder_name, file_name)
    # # print(data)
    # for orcamento in data:
    #     for key, value in orcamento.items():

    #         if key == "orcamento_materiais":
    #             for produto in value:
    #                 print(produto)
    #                 print("-" * 70)
    #         else:
    #             print(key, value)
    #     print("-" * 70)
