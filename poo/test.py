import os
import random
import copy

from rich import print
from save_data import SaveDataFile
from orcamento_projeto import OrcamentoProjeto
from materiais import Materiais
from projetos import Projetos


def divider(headline):
    print("\n")
    print("-" * 70)
    print(headline.upper())
    print("-" * 70)

def handler_add_material() -> list[Materiais]:
    cores = ['Roxo', 'Branco', 'Azul', 'Rosa', 'Preto', 'Cinza', 'Amarelo', 'Verde', 'Vermelho']
    materiais_adicionados = []
    for number in range(10):
        numero_radom = random.randint(0, len(cores)-1)
        mt = Materiais(number, cores[numero_radom], 90, 33.33, 'g')
        materiais_adicionados.append(mt)
    return materiais_adicionados

def handler_selecionar_material(id_material: list, qntd_material_usado: int, lt_materiais: list[Materiais]) -> list[Materiais]:
    material_selecionado = []
    for mat in lt_materiais:
        for select in id_material:
            if mat.material_id == select:
                # A copia é importante para gerar um novo endereço de memoria do objeto
                # Permitindo atualizar as informações do objeto sem alterar os demais itens
                # que nao foram selecionados
                copia_obj = copy.deepcopy(mat)
                if qntd_material_usado > 0:
                   copia_obj.mt_update_qntd_produto_usado_projeto(qntd_material_usado)
                material_selecionado.append(copia_obj)
    return material_selecionado
        

if __name__ == "__main__":
    os.system("clear")

    # Variaveis globais
    numero_radom = random.randint(0, 10000)

    # Banco de dados em arquivos json
    folder_name = "materiais"
    file_name = "materiais.json"
    data = SaveDataFile(folder_name, file_name)

    # instancia lista de Materiais
    lista_materais = handler_add_material()

    # instancia Orcamento
    oc1 = OrcamentoProjeto(1, 'Orcamento 1')
    oc2 = OrcamentoProjeto(2, 'Orcamento 2')

    lista_orcamento = [oc1, oc2]

    # instancia Projeto
    pj1 = Projetos(lista_orcamento, lista_materais)

    # Métodos referente a classe Orcamento
    itens_add_orcamento = [2,4,6,8]
    copy_lista_orcamento = copy.deepcopy(lista_materais)
    lista_material_selecionado = handler_selecionar_material(itens_add_orcamento, 10, copy_lista_orcamento)

    pj1.pj_adicionar_material_orcamento(1, lista_material_selecionado)
    
    lista_orca = pj1.pj_listar_orcamentos()
    print(lista_orca)

    # Métodos referete a classe Materiais
    lista_itens = pj1.pj_listar_materiais_cadatrados()
    print(lista_itens)
    