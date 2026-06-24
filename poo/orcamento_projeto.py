from materiais import Materiais

class OrcamentoProjeto:
    def __init__(self, orcamento_id: int, orcamento_nome: str):
        self.orcamento_id: int = orcamento_id
        self.orcamento_nome: str = orcamento_nome
        self.orcamento_custo_materiais: float = 0
        self.lista_materiais: list[Materiais] = []

    def oc_listar_detalhes_orcamento(self) -> dict:
        materiais_add = []
        for material in self.lista_materiais:
                materiais_add.append(material.mt_listar_detalhes_materiais())
        return {
            "orcamento_id": self.orcamento_id,
            "orcamento_nome": self.orcamento_nome,
            'orcamento_custo_materiais': 0,
            "orcamento_materiais": materiais_add,
        }

    def oc_selecionar_materiais(self, add_material: Materiais) -> bool:
        try:
            self.lista_materiais.append(add_material)
            return True
        except ValueError as err:
            return False


    def oc_custo_materiais_orcamento(self):
        total = 0
        for material in self.lista_materiais:
              total += material.material_valor_produto_usado_projeto
        return total

    # def oc_deletar_material(self, material_id) -> list | None:
    #     try:
    #         for material in self.lista_materiais:
    #             if material.cadastro_id == material_id:
    #                 item = self.lista_materiais.remove(material)
    #                 return item
    #     except ValueError:
    #         return print("Erro: Campo vazio")
