from model_base_cadastro import CadastroItens
from rich import print

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

    def mt_selecionar_produto(self, material_id) -> str:
        if not material_id:
            raise ValueError("Erro: ID do material não pode ser vazio.")
            
        material_selecao = 'select' if self.material_status == 'unselect' else 'unselect'
        self.material_status = material_selecao
        
        return f"Material {self.cadastro_nome} alterado para {self.material_status}."


    def mt_valor_quantidade_projeto(self, qntd_projeto) -> float:
        if not qntd_projeto:
            raise ValueError("Erro: O numero de quantidade está vazio ou zerado")

        return qntd_projeto * self.mt_valor_unidade_medida()


    def mt_valor_unidade_medida(self) -> float:
        if self.material_unidade_medida.lower() == "g":
            valor_grama = self.get_item_valor / self.material_quantidade
            return valor_grama


    def mt_listar_materiais(self) -> dict:
        return {
            "id": self.cadastro_id,
            "nome": self.cadastro_nome,
            "valor": round(self.get_item_valor, 3),
            "quantidade": self.material_quantidade,
            "unidade_medida": self.material_unidade_medida,
            "valor_unidade_medida": round(self.mt_valor_unidade_medida(), 2),
            "status": self.material_status,
        }


if __name__ == "__main__":
    
    # instancia da classe
    material = Materiais(1, "Preto", 33.33, 90, 'g')
    
    # Alterar o produto de 'unselect' para 'select' - vice versa
    selecao = material.mt_selecionar_produto(1) 
    
    # Valor total usado no projeto
    selecao = material.mt_valor_quantidade_projeto(10)
    
    # Valor total por unidade medida
    selecao = material.mt_valor_unidade_medida()
    
    # Listar materiais formato dicionario / para salvar em json
    item =  material.mt_listar_materiais()
    
    print(selecao)
    print(item)
