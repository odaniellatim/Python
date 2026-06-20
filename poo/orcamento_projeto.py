from materiais import Materiais

class OrcamentoProjeto:
    def __init__(self, orcamento_id: int, orcamento_nome: str):
        self.orcamento_id: int = orcamento_id
        self.orcamento_nome: str = orcamento_nome
        self.lista_materiais: list[Materiais] = []

    def oc_listar_orcamento(self) -> dict:
        materiais_add = []
        for material in self.lista_materiais:
            materiais_add.append(material)
        return {
            "orcamento_id": self.orcamento_id,
            "orcamento_nome": self.orcamento_nome,
            "orcamento_materiais": materiais_add,
        }

    def oc_selecionar_material(self, add_material) -> bool:
        try:
            self.lista_materiais.append(add_material)
            return True
        except ValueError as err:
            return False

    def oc_deletar_material(self, material_id) -> list | None:
        try:
            for material in self.lista_materiais:
                if material.cadastro_id == material_id:
                    item = self.lista_materiais.remove(material)
                    return item
        except ValueError:
            return print("Erro: Campo vazio")
