from Escrita_na_tela import Escrita_na_tela

class Catalogo_produtos:
    def __init__(self, id_produto: int, id_user: int, nome_produto: str, valor_venda: float, valor_compra: float) -> None:
        self.id_produto = id_produto
        self.id_user = id_user
        self.nome_produto = nome_produto
        self.valor_venda = valor_venda
        self.valor_compra = valor_compra
    
    # Lista os produtos cadastrados por usuario
    def listar_produtos(self, id_user):        
        if(id_user == self.id_user):
            obj = {
                    "id_produto": self.id_produto,
                    "nome_produto": self.nome_produto,
                    "valor_venda": self.valor_venda,
                    "valor_compra": self.valor_compra,
                }
            return obj
        else:
            return []
    
    # Atualiza os dados dos produtos de acordo com o usuario id e o id do produto.
    def editar_produto(self, id_user, id_produto, nome_produto = None, valor_venda = None, valor_compra = None):
        
        if(id_user == self.id_user and id_produto == self.id_produto):
            print(nome_produto)
            if(nome_produto != None):
                self.nome_produto = nome_produto
                Escrita_na_tela.alerta(f"Produto: {self.nome_produto} nome alterado com sucesso!")
            if(valor_venda != None):
                self.valor_venda = valor_venda
                Escrita_na_tela.alerta(f"Produto: {self.nome_produto} valor de venda alterado com sucesso!")
            if(valor_compra != None):
                self.valor_compra = valor_compra
                Escrita_na_tela.alerta(f"Produto: {self.nome_produto} valor de compra alterado com sucesso!")
                
            else:
                Escrita_na_tela.alerta(f"Nenhuma Alteração realizada no produto {self.nome_produto}")
        else:
            Escrita_na_tela.alerta("Nenhuma alteração realizada. Informe os valores para realizar a mudança")
            return []
        


if __name__ == "__main__":
    print("catalogo.")