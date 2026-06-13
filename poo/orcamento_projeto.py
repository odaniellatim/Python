from materiais import Materiais


class OrcamentoProjeto:
    def __init__(self, orcamento_id: int, orcamento_nome: str):
        self.orcamento_id: int = orcamento_id
        self.orcamento_nome: str = orcamento_nome
        self.lista_materiais: Materiais = []

    def oc_adicionar_materiais(
        self,
        material_id: int,
        material_nome: str,
        material_preco: float,
        material_quantidade: int,
        material_unidade_medida: str,
    ) -> Materiais:

        item = Materiais(
            material_id,
            material_nome,
            material_preco,
            material_quantidade,
            material_unidade_medida,
        )
        self.lista_materiais.append(item)
        return item

    def oc_valor_total_estoque(self) -> float:
        valor_total = 0
        for preco in self.lista_materiais:
            valor_total += preco.get_item_valor
        return valor_total

    def oc_listar_materiais_projeto(self) -> list:
        lista_materiais_projeto = []
        for material in self.lista_materiais:
            if material.mt_listar_materiais()["status"] == "select":
                lista_materiais_projeto.append(material.mt_listar_materiais())
        return lista_materiais_projeto

    def oc_listar_materiais(self) -> list:
        lista_materiais_projeto = []
        for material in self.lista_materiais:
            lista_materiais_projeto.append(material.mt_listar_materiais())
        return lista_materiais_projeto

    def oc_nome_orcamento(self) -> str:
        return f"{self.orcamento_id}. {self.orcamento_nome}"

    def oc_dicionario_save(self) -> list:
        data = [
            {
                "orcamento_id": self.orcamento_id,
                "orcamento_nome": self.orcamento_nome,
                "orcamento_materiais": self.oc_listar_materiais_projeto(),
            }
        ]
        return data

    def oc_alterar_status(self, id_material: int) -> None:
        for material in self.lista_materiais:
            if material.cadastro_id == id_material:
                material.mt_selecionar_produto(id_material)

    def oc_deletar_material(self, material_id) -> list:
        try:
            for material in self.lista_materiais:
                if material.cadastro_id == material_id:
                    item = self.lista_materiais.remove(material)
                    return item
        except ValueError:
            return print("Erro: Campo vazio")

    def add_produto_teste(self):
        """Cadastro de materiais para realizar os testes"""
        item1 = Materiais(1, "Azul", 33, 90, "g")
        item2 = Materiais(2, "Amarelo", 33, 90, "g")
        item3 = Materiais(3, "Preto", 33, 90, "g")
        item4 = Materiais(4, "Rosa", 33, 90, "g")
        self.lista_materiais.append(item1)
        self.lista_materiais.append(item2)
        self.lista_materiais.append(item3)
        self.lista_materiais.append(item4)


# if __name__ == "__main__":

#     pasta = "materiais"
#     arquivo = "materiais.json"

#     bd = Save_in_file(pasta, arquivo)  # Class gerencia banco de dados
#     load_file = load_file_materiais(bd, pasta, arquivo)

#     oc = OrcamentoProjeto(1, "teste")

#     produto = oc.oc_listar_materiais()
#     print(load_file)
#     print(produto)
