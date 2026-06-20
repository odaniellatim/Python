from Save_in_file import Save_in_file
from projetos import Projetos
import random

def handler_save_file(data):
    foldername = 'data'
    filename = 'orcamento.json'

    save_json = Save_in_file(foldername, filename)
    save_json.save_data(data)

if __name__ == "__main__":
    number_id_random = random.randint(1, 1000)

    # INSTANCIA: Projeto
    projeto = Projetos()

    # Criando novo orçamento e listando o orçamento
    orcamento = projeto.pj_adicionar_orcamento(number_id_random, "Teste")
    print(orcamento)

    # cadastrando a lista de materiais
    precos = [33.67, 32.15, 29.25, 30.29, 43.75, 40.98, 38.99]
    cores = [
        "amarelo",
        "azul",
        "rosa",
        "preto",
        "branco",
        "vermelho",
        "cinza",
        "verde",
        "laranja",
    ]
    for number in range(10):
        corNumber = random.randint(0, len(cores) - 1)
        precoNumber = random.randint(0, len(precos) - 1)
        mt = projeto.pj_cadastrar_materiais(
            number + 1, cores[corNumber], precos[precoNumber], 90, "g", 0
        )

    print("\nLISTA DE MATERIAIS CADASTRADOS")
    materiais_cadastrados = projeto.pj_listar_materiais()
    print(materiais_cadastrados, "\n")

    print("\n MATERIAL SELECIONADO PARA O PROJETO")
    projeto.pj_selecionar_material_orcamento(2, 10)
    projeto.pj_selecionar_material_orcamento(5, 10)
    projeto.pj_selecionar_material_orcamento(8, 10)
    projeto.pj_selecionar_material_orcamento(6, 15)

    print("\n PROJETO LISTA")
    orcamento1 = projeto.pj_listar_orcamentos()
    handler_save_file(orcamento1)
