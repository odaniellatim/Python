import random
from orcamento_projeto import OrcamentoProjeto
from materiais import Materiais
from rich import print


class Projetos:
    def __init__(self):
        self.orcamentos: list[OrcamentoProjeto] = []
        self.lista_materiais: list[Materiais] = []
        # self.projeto_id_ramdom = random.randint(0, 10000)

    def pj_adicionar_orcamento(self, projeto_id: int, projeto_nome: str) -> dict:
        # projeto_id = self.projeto_id_ramdom
        orcamento = OrcamentoProjeto(projeto_id, projeto_nome)
        self.orcamentos.append(orcamento)
        print(f"Orcamento {projeto_nome} Adicionado com sucesso!")
        return orcamento.oc_listar_orcamento()

    def pj_cadastrar_materiais(
        self,
        material_id,
        material_nome,
        material_preco,
        material_qntd,
        material_unidade_medida,
        qntd_usado_projeto,     
    ):
        novo_material = Materiais(
            material_id,
            material_nome,
            material_preco,
            material_qntd,
            material_unidade_medida,
            qntd_usado_projeto,
        )
        self.lista_materiais.append(novo_material)
        return novo_material

    def pj_listar_materiais(self):
        materiais_adicionado = []
        for material in self.lista_materiais:
            materiais_adicionado.append(material.mt_listar_materiais())
        return materiais_adicionado

    def pj_selecionar_material_orcamento(self, material_id, qntd_usado_projeto):
        material_selecionado = None

        for mat in self.lista_materiais:
            if mat.cadastro_id == material_id:
                material_selecionado = mat
                break

        if material_selecionado:
            material_selecionado.mt_selecionar_produto(material_id, qntd_usado_projeto)

        for orc in self.orcamentos:
            return orc.oc_selecionar_material(material_selecionado)

    def pj_listar_orcamentos(self):
        for orcamento in self.orcamentos:
            dados_orcamento = orcamento.oc_listar_orcamento()

            materiais_orcamento = []
            if not dados_orcamento["orcamento_materiais"]:
                print("Nenhum material vinculado!")
            else:
                for mat in dados_orcamento["orcamento_materiais"]:
                    materiais_orcamento.append(mat.mt_listar_materiais())
            return {
                "orcamento_id": orcamento.orcamento_id,
                "orcamento_nome": orcamento.orcamento_nome,
                "orcamento_materiais": materiais_orcamento,
            }


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

    print("\n PROJETO LISTA", projeto.pj_listar_orcamentos())
