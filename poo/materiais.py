class Materiais:
    def __init__(
        self,
        material_id,
        material_nome,
        material_valor,
        material_quantidade,
        material_unidade_medida,
    ):
        self.material_id = material_id
        self.material_nome = material_nome
        self.material_valor = material_valor
        self.material_quantidade = material_quantidade
        self.material_unidade_medida = material_unidade_medida
        self.material_status = "unselect"
        self.material_qntd_usado_projeto = 0
        self.material_qntd_usado_preco = 0

    def mt_get_material_valor(self):
        return self.material_valor

    def mt_selecionar_produto(self, material_id):
        if material_id != "":
            self.material_status = "select"
            return f"Material {self.material_nome} selecionado."

    def mt_valor_quantidade_projeto(self, qntd_projeto):
        if qntd_projeto != "":
            return qntd_projeto * self.mt_valor_unidade_medida()

    def mt_valor_unidade_medida(self):
        if self.material_unidade_medida == "g":
            valor_grama = self.material_valor / self.material_quantidade
            return valor_grama

    def mt_listar_materiais(self):
        print(f"ID. {self.material_id}")
        print(f"Nome: {self.material_nome}")
        print(f"Valor: {self.material_valor}")
        print(
            f"Quantidade: {self.material_quantidade} - {self.material_unidade_medida}"
        )
        print("Valor por grama: R$", round(self.mt_valor_unidade_medida(), 2))
        print(f"Status: {self.material_status}")
        print("-" * 70)
