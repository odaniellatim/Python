from Catalogo_produtos import Catalogo_produtos
from Escrita_na_tela import Escrita_na_tela

class Historico_vendas:
    def __init__(self, user_id, id_registro, id_mes, produto_nome, mes_vendas, total_vendidos) -> None:
        self.user_id = user_id
        self.id_registro = id_registro
        self.id_mes = id_mes
        self.produto_nome = produto_nome
        self.mes_vendas = mes_vendas
        self.produtos_vendidos: list[Catalogo_produtos] = []
        self.total_vendidos = total_vendidos

    # Usado apenas para testar a classe Historico de vendas
    def add_produto(self,id_produto, id_user, nome_produto, valor_venda, valor_compra):
        produto = Catalogo_produtos(id_produto, id_user, nome_produto, valor_venda, valor_compra)
        self.produtos_vendidos.append(produto)

    def lista_produtos(self, user_id):
        produtos = []
        for produto in self.produtos_vendidos:
            if(produto.id_user == user_id):
                produtos.append(produto.listar_produtos(user_id))
        return produtos
    
    def ht_relatorio_de_vendas(self, ):    
       
        for produto in self.produtos_vendidos:            

            # TODO: montar um relatorio apresentavel para analise.
            rt = ({
                    # itens do historico
                    "id_registro": self.id_registro,                        
                    "mes_nome": self.mes_vendas,
                    "produto_nome": self.produto_nome,
                    "total_vendidos": self.total_vendidos,

                    # informações do produto
                    "valor_venda": produto.valor_venda,
                    "valor_compra": produto.valor_compra,
                })
            return rt
        return {}
    

if __name__ == "__main__":
    ht = Historico_vendas(1, 1, 1, "Mouse xyz", 'janeiro', 70) #user, id_registro, mes_vendas
    # ht1 = Historico_vendas(1, 2, 1, "Mouse xyz", 'janeiro', 70) #user, id_registro, mes_vendas
    # ht2 = Historico_vendas(1, 3, 1, "Mouse xyz", 'janeiro', 70) #user, id_registro, mes_vendas
    # ht3 = Historico_vendas(2, 4, 1, "Mouse xyz", 'janeiro', 70) #user, id_registro, mes_vendas
    # ht4 = Historico_vendas(2, 5, 1, "Mouse xyz", 'janeiro', 70) #user, id_registro, mes_vendas

    # Add produtos que serão vendidos pelo usuario cadastrado.
    produto1 = ht.add_produto(1, 1, "Mouse xyz", 99.99, 35.36)
    produto2 = ht.add_produto(2, 1, "Teclado xyz", 135.35, 70.99)
    produto3 = ht.add_produto(3, 1, "Som xyz", 278.99, 169.99)
    produto4 = ht.add_produto(4, 1, "Monitor xyz", 999.69, 475.98)

    produto5 = ht.add_produto(3, 2, "Som xyz", 278.99, 169.99)
    produto6 = ht.add_produto(4, 2, "Monitor xyz", 999.69, 475.98)

    lista_produtos = ht.ht_relatorio_de_vendas()
    print (lista_produtos)
    saida = Escrita_na_tela.historico_venda([lista_produtos])