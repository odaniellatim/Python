from model_base_cadastro import CadastroItens

class Materiais(CadastroItens):

    def __init__(
        self,
        cadastro_id,
        cadastro_nome,
        cadastro_valor,
        material_quantidade,
        material_unidade_medida,
        qntd_usado_projeto,
    ):

        super().__init__(cadastro_id, cadastro_nome, cadastro_valor)
        self.material_quantidade = material_quantidade
        self.material_unidade_medida = material_unidade_medida
        self.material_status = "unselect"
        self.material_qntd_usado_projeto = 0
        self.material_qntd_usado_preco = 0
        self.qntd_usado_projeto = qntd_usado_projeto
        self.valor_produto_usado_projeto = 0

    def mt_selecionar_produto(self, material_id, qntd_usado_projeto) -> dict:
        if not material_id:
            raise ValueError("Erro: ID do material não pode ser vazio.")

        if self.material_status == "unselect":
            self.material_status = "select"
            self.qntd_usado_projeto = qntd_usado_projeto
            self.mt_valor_produto_usado_projeto(qntd_usado_projeto)
        else:
            self.material_status = "unselect"

        return self.mt_listar_materiais()

    def mt_valor_quantidade_projeto(self, qntd_projeto) -> float:
        if not qntd_projeto:
            raise ValueError("Erro: O numero de quantidade está vazio ou zerado")
        return qntd_projeto * self.mt_valor_unidade_medida()
    
    def mt_valor_produto_usado_projeto(self, qntd):
        if qntd:
            self.valor_produto_usado_projeto = round(self.mt_valor_unidade_medida() * self.qntd_usado_projeto, 4)
            


    def mt_valor_unidade_medida(self) -> float:
        if self.material_unidade_medida.lower() == "g":
            valor_grama = self.get_item_valor / self.material_quantidade
            return valor_grama
        return 0


    def mt_listar_materiais(self) -> dict:
        return {
            "id": self.cadastro_id,
            "nome": self.cadastro_nome,
            "valor": round(self.get_item_valor, 3),
            "quantidade": self.material_quantidade,
            "unidade_medida": self.material_unidade_medida,
            "valor_unidade_medida": round(self.mt_valor_unidade_medida(), 2),
            'qntd_usado_projeto': self.qntd_usado_projeto,
            'valor_produto_usado_projeto': self.valor_produto_usado_projeto,
            "status": self.material_status,
        }
