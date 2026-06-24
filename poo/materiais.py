
class Materiais:

    def __init__(
        self,
        material_id: int,
        material_nome: str,
        material_quantidade: int,
        material_valor: float,
        material_padrao_medida: str,
    ):
        self.material_id = material_id
        self.material_nome = material_nome
        self.material_quantidade = material_quantidade
        self.material_valor = material_valor
        self.material_padrao_medida = material_padrao_medida
        self.material_valor_produto_usado_projeto = 0
        self.material_qntd_produto_usado_projeto = 0

    def mt_update_qntd_produto_usado_projeto(self, qntd_material: int) -> bool:
        if qntd_material > 0:
            self.material_qntd_produto_usado_projeto = qntd_material
            self.mt_update_valor_produto_usado_projeto()
            return True
        else:
            return False
        
    def mt_update_valor_produto_usado_projeto(self) -> None:
        self.material_valor_produto_usado_projeto = self.mt_valor_produto_qntd_usado()

    def mt_preco_gramas(self) -> float:
        if self.material_padrao_medida == 'g':
            return round(self.material_valor / self.material_quantidade, 4)
        else:
            return 0
    
    def mt_preco_ml(self) -> float:
        if self.material_padrao_medida == 'l':
            return round(self.material_valor / (self.material_quantidade * 1000), 4)
        else:
            return 0
        
    def mt_valor_produto_qntd_usado(self) -> float:
        if self.material_padrao_medida == 'g':
            valor_gramas = round(self.material_qntd_produto_usado_projeto * self.mt_preco_gramas(), 4)
            return valor_gramas
        elif self.material_padrao_medida == 'l':
            valor_ml = round(self.material_qntd_produto_usado_projeto * self.mt_preco_ml(), 4)
            return valor_ml
        return 0
    
    def mt_valor_padrao_medida(self):
        return round(self.material_valor / self.material_quantidade, 4)

    def mt_listar_detalhes_materiais(self) -> dict:
        return {
            "mt_id": self.material_id,
            "mt_nome": self.material_nome,
            "mt_valor": round(self.material_valor, 3),
            "mt_quantidade": self.material_quantidade,
            "mt_padrao_medida": self.material_padrao_medida,
            'mt_valor_padrao_medida': self.mt_valor_padrao_medida(),

            # informações complementares quando o produto é selecionado no projeto
            'mt_qntd_produto_usado_projeto': self.material_qntd_produto_usado_projeto,
            'mt_valor_produto_usado_projeto': self.material_valor_produto_usado_projeto,
        }
