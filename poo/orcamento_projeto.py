from materiais import Materiais
from rich import print

class OrcamentoProjeto:
    def __init__(self, orcamento_id: int, orcamento_nome: str):
        self.orcamento_id: int = orcamento_id
        self.orcamento_nome: str = orcamento_nome
        self.lista_materiais: Materiais = []

    def oc_id(self):
        return self.orcamento_id
    
    def oc_adicionar_materiais(
        self,
        material_id: int,
        material_nome: str,
        material_preco: float,
        material_quantidade: int,
        material_unidade_medida: str,
    ) -> Materiais:
        try:    
            item = Materiais(
                material_id,
                material_nome,
                material_preco,
                material_quantidade,
                material_unidade_medida,
            )        
            self.lista_materiais.append(item)
        except ValueError as err:
            print("Erro: Campo preenchido incorretamente", err)
        return item.mt_listar_materiais()

    def oc_valor_total_estoque(self) -> float:
        valor_total = 0
        for preco in self.lista_materiais:
            valor_total += preco.get_item_valor
        return valor_total

    def oc_listar_materiais_select(self) -> list:
        lista_materiais_projeto = []
        for material in self.lista_materiais:
            if material.mt_listar_materiais()["status"] == "select":
                lista_materiais_projeto.append(material.mt_listar_materiais())
        return lista_materiais_projeto

    def oc_listar_todos_materiais(self) -> list:
        lista_materiais_projeto = []
        for material in self.lista_materiais:
            lista_materiais_projeto.append(material.mt_listar_materiais())
        return lista_materiais_projeto

    def oc_nome_orcamento(self) -> dict:
        return {'orcamento_id': self.orcamento_id, 'orcamento_nome' : self.orcamento_nome}

    def oc_dicionario_save(self) -> list:
        data = [
            {
                "orcamento_id": self.orcamento_id,
                "orcamento_nome": self.orcamento_nome,
                "orcamento_materiais": self.oc_listar_materiais_select(),
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

if __name__ == "__main__":
    oc = OrcamentoProjeto(1, "Orcamento Teste")
    
    # Armazena uma lista de materiais
    materiais = []
    
    # Adicionando material a lista de materiais
    materiais.append(oc.oc_adicionar_materiais(12, "preto", 15.90, 90, 'g'))
    materiais.append(oc.oc_adicionar_materiais(10, "Branco", 16.90, 90, 'g'))
    materiais.append(oc.oc_adicionar_materiais(9, "Rosa", 13.58, 90, 'g'))
    
    # Listando o valor do estoque total dos materiais
    total_estoque = oc.oc_valor_total_estoque()
    
    # Alterar o status de um material para selecionar
    oc.oc_alterar_status(10)
    oc.oc_alterar_status(9)
    
    # Listar materiais selecionados
    oc.oc_listar_materiais_select()
    
    # Listar todos os materiais
    oc.oc_listar_todos_materiais()
    
    # Listar dicionario completo para salvar em um arquivo
    data = oc.oc_dicionario_save()
    
    # Deletar o material
    delete = oc.oc_deletar_material(9)
    print(oc.oc_dicionario_save())
    
        
    print(data)
    print(f"Total Estoque: {round(total_estoque, 3)}")
    print(f"\n {oc.orcamento_nome} \n")
