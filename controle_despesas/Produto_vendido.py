from datetime import date

class Produto_vendido:
    def __init__(self, produto_vendido_mes, qntd_produtos_vendidos) -> None:
        self.produto_vendido_mes: date = produto_vendido_mes # informe o mês em numero.
        self.qntd_produtos_vendidos: int = qntd_produtos_vendidos

    
    def valor_medio_vendas(self, mes):
        """ Calcula o valor médido das vendas (mes)"""
        if(self.produto_vendido_mes == mes):
            print(f"Valor médio: {self.qntd_produtos_vendidos}")
