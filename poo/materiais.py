from model_base_cadastro import CadastroItens


class Materiais(CadastroItens):

    def __init__(
        self,
        cadastro_id,
        cadastro_nome,
        cadastro_valor,
        material_quantidade,
        material_unidade_medida,
    ):

        super().__init__(cadastro_id, cadastro_nome, cadastro_valor)
        self.material_quantidade = material_quantidade
        self.material_unidade_medida = material_unidade_medida
        self.material_status = "unselect"
        self.material_qntd_usado_projeto = 0
        self.material_qntd_usado_preco = 0

    def mt_selecionar_produto(self, material_id):
        if material_id != "":
            self.material_status = "select"
            return f"Material {self.cadastro_nome} selecionado."

    def mt_valor_quantidade_projeto(self, qntd_projeto):
        if qntd_projeto != "":
            return qntd_projeto * self.mt_valor_unidade_medida()

    def mt_valor_unidade_medida(self):
        if self.material_unidade_medida == "g":
            valor_grama = self.get_item_valor / self.material_quantidade
            return valor_grama

    def mt_listar_materiais(self):
        return {
            "id": self.cadastro_id,
            "nome": self.cadastro_nome,
            "valor": round(self.get_item_valor, 3),
            "quantidade": self.material_quantidade,
            "unidade_medida": self.material_unidade_medida,
            "valor_unidade_medida": round(self.mt_valor_unidade_medida(), 2),
            "status": self.material_status,
        }
