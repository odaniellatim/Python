from materiais import Materiais


class OrcamentoProjeto:
    def __init__(self, orcamento_id, orcamento_nome):
        self.orcamento_id = orcamento_id
        self.orcamento_nome = orcamento_nome
        self.lista_materiais = []
        self.add_produto_teste()

    def oc_adicionar_materiais(
        self,
        material_id,
        material_nome,
        material_preco,
        material_quantidade,
        material_unidade_medida,
    ):
        item = Materiais(
            material_id,
            material_nome,
            material_preco,
            material_quantidade,
            material_unidade_medida,
        )
        self.lista_materiais.append(item)

    def oc_valor_total_estoque(self):
        valor_total = 0
        for preco in self.lista_materiais:
            valor_total += preco.mt_get_material_valor()
        return valor_total

    def oc_listar_materiais_cadastrados(self):
        for material in self.lista_materiais:
            material.mt_listar_materiais()
        print(f"Valor em Estoque: R$ {round(self.oc_valor_total_estoque(),2)}")

    def add_produto_teste(self):
        item1 = Materiais(1, "Azul", 33, 90, "g")
        item2 = Materiais(2, "Amarelo", 33, 90, "g")
        item3 = Materiais(3, "Preto", 33, 90, "g")
        item4 = Materiais(4, "Rosa", 33, 90, "g")
        self.lista_materiais.append(item1)
        self.lista_materiais.append(item2)
        self.lista_materiais.append(item3)
        self.lista_materiais.append(item4)
