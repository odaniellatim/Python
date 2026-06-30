
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
        self.material_valor_padrao_medida = 0
        self.material_valor_produto_usado_projeto = 0
        self.material_qntd_produto_usado_projeto = 0

        # Calcula o valor da fração do produto com base no padrao de medida
        self.mt_valor_padrao_medida(self.material_padrao_medida)
        

    def mt_update_qntd_produto_usado_projeto(self, qntd_material: int) -> bool:
        ''' Atualiza a quantidade de produto usado no projeto para adicionar no orcamento'''
        if qntd_material > 0:
            self.material_qntd_produto_usado_projeto = qntd_material
            self.mt_update_valor_produto_usado_projeto()
            return True
        else:
            return False
        
    def mt_update_valor_produto_usado_projeto(self) -> None:
        '''Atualiza o valor total usado no projeto, baseado no preco fracionado do padrao de medida'''
        self.material_valor_produto_usado_projeto = self.material_valor_padrao_medida

    
    def mt_valor_padrao_medida(self, padrao_medida_produto: str) -> None:
        '''Valor calculado baseado no tipo de padrão de medida do produto selecionado'''
        match padrao_medida_produto:
            case 'g':
                valor_g = round(self.material_valor / self.material_quantidade, 4)
                self.material_valor_padrao_medida = valor_g
            case 'ml':
                valor_ml = round(self.material_valor / self.material_quantidade, 4)
                self.material_valor_padrao_medida = valor_ml
            case 'l':
                valor_l = round(self.material_valor / (self.material_quantidade * 1000), 4)
                self.material_valor_padrao_medida = valor_l
            case _:
                self.material_valor_padrao_medida = 0

    def mt_listar_detalhes_materiais(self) -> dict:
        return {
            "mt_id": self.material_id,
            "mt_nome": self.material_nome,
            "mt_valor": round(self.material_valor, 3),
            "mt_quantidade": self.material_quantidade,
            "mt_padrao_medida": self.material_padrao_medida,
            'mt_valor_padrao_medida': self.material_valor_padrao_medida
        }
    
    def mt_listar_detalhes_material_selecionado(self) -> dict:
        return {
            "mt_id": self.material_id,
            "mt_nome": self.material_nome,
            "mt_valor": round(self.material_valor, 3),
            "mt_quantidade": self.material_quantidade,
            "mt_padrao_medida": self.material_padrao_medida,
            'mt_valor_padrao_medida': self.material_valor_padrao_medida,

            # informações complementares quando o produto é selecionado no projeto
            'mt_qntd_produto_usado_projeto': self.material_qntd_produto_usado_projeto,
            'mt_valor_produto_usado_projeto': self.material_valor_produto_usado_projeto,
        }
