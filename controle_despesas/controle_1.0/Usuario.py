from Catalogo_produtos import Catalogo_produtos
from Fatura_mensal import Fatura_mensal
from Historico_vendas import Historico_vendas
from Escrita_na_tela import Escrita_na_tela

class Usuario:
    def __init__(self,id_user, nome_usuario, user_name, senha, nivel_usuario = "admin") -> None:
        self.id_user = id_user
        self.nome_usuario = nome_usuario
        self.user_name = user_name
        self.senha = senha
        self.nivel_usuario = nivel_usuario
        self.lista_produtos: list[Catalogo_produtos] = []
        self.historico_vendas: list[Historico_vendas] = []
        self.lista_de_faturas: list[Fatura_mensal] = []

    # Cria uma fatura mensal para o ID do usuario
    def adicionar_fatura_mensal(self,id_fatura, id_user, mes_fatura: str):
        if(id_user == self.id_user):
            nova_fatura = Fatura_mensal(id_fatura, id_user, mes_fatura)
            self.lista_de_faturas.append(nova_fatura)
            return self.lista_de_faturas

    # Lista todas as faturas criadas pelo id do usuario
    def listar_nome_fatura(self, id_user):
        faturas_nome = []
        for lista in self.lista_de_faturas:
            if(lista.user_id == id_user):
                faturas_nome.append(lista.listar_nome_fatura(id_user))
            else:
                Escrita_na_tela.alerta("Usuario não encontrado.")
                break
        return faturas_nome
    
    # Adiciona os items referente a fatura e o id do usuario.
    def add_items_fatura(self, id_item, id_fatura, user_id, nome_despesa, valor_pago, dia, mes, status_pagamento):
        for lista in self.lista_de_faturas:
            lista.adicionar_despesa(id_item, id_fatura, user_id, nome_despesa, valor_pago, dia, mes, status_pagamento)
    
    # Listar os items referente o id da fatura.
    def listar_itens_fatura(self, id_fatura: int, status: str|None = None):
    
        if not(status == None):
            for item in self.lista_de_faturas:
                if (item.id_fatura == id_fatura):
                    itens_cadastrado = item.listar_items_fatura(status.lower())
                    return itens_cadastrado
        else:
            for item in self.lista_de_faturas:
                if(item.id_fatura == id_fatura):
                    itens_cadastrado = item.listar_items_fatura()
                    return itens_cadastrado
        return []
            
    # Cadastro de produtos que serão vendidos
    def cadastrar_produtos(self, id_produto: int, id_user: int, nome_produto: str, valor_venda: float, valor_compra: float):
        novo_produto = Catalogo_produtos(id_produto, id_user, nome_produto, valor_venda, valor_compra)
        self.lista_produtos.append(novo_produto)
        return self.lista_produtos
    
    # Lista os produtos cadastrados de acordo com o usuario
    def produtos_cadastrados(self, id_user: int):
        lista_produtos = []
        
        for produto in self.lista_produtos:
            if(id_user == produto.id_user):
                lista_produtos.append( produto.listar_produtos(id_user))
        return lista_produtos
    
    def atualizar_produto(self, id_user, id_produto, nome_produto = None, valor_venda = None, valor_compra = None):
        for produto in self.lista_produtos:
            if(id_user == produto.id_user and id_produto == produto.id_produto):
                produto_alterado = produto.editar_produto(id_user, id_produto, nome_produto, valor_venda, valor_compra)
                return produto_alterado

    def remover_produtos_cadastrado(self, id_user, id_produto):
        item_removido = []
        for produto in self.lista_produtos:
            if(id_user == produto.id_user and id_produto == produto.id_produto):
                item_removido.append(produto.nome_produto)
                item_removido.append('removido')
                self.lista_produtos.remove(produto)
        return item_removido
    
    def lucro_produtos(self) -> float:
        lucro = 0
        for produto in self.lista_produtos:
            lucro += produto.valor_venda - produto.valor_compra
        return lucro
    
    # Cadastra historico de vendas e adiciona os produtos se existir
    def add_histico_vendas_mes(self, user_id, id_registro, id_mes, produto_nome, mes_vendas, total_vendidos):
        
        hv = Historico_vendas(user_id, id_registro, id_mes, produto_nome, mes_vendas, total_vendidos)

        produto_encontrado = None
        for p in self.lista_produtos:
            if p.nome_produto == produto_nome:
                produto_encontrado = p
                break
        
        if produto_encontrado:
            hv.produtos_vendidos.append(produto_encontrado)
        else:
            print(f"Aviso: Produto '{produto_nome}' não encontrado no catálogo!")

        self.historico_vendas.append(hv)

    # Lista os historico com os resultados de vendas e também do produto
    def listar_historico_vendas(self, user_id, id_mes = None):
        items = []

        # Filtra os resultados por id mensal
        if(id_mes != None):
            for historico in self.historico_vendas:
                if(historico.user_id == user_id and historico.id_mes == id_mes):
                    items.append(historico.ht_relatorio_de_vendas())
        else:
            for historico in self.historico_vendas:
                if(historico.user_id == user_id):
                    items.append(historico.ht_relatorio_de_vendas())
        return items


if __name__ == "__main__":
    user1 = Usuario(1, "daniel", "odaniel", "123456")

    # Cadastra a fatura para adicionar as despesas.
    user1.adicionar_fatura_mensal(1,1,'janeiro')
    # user1.adicionar_fatura_mensal('fevereiro')
    # user1.adicionar_fatura_mensal('marco')
    # user1.adicionar_fatura_mensal('abril')

    #Add items fatura referente ao mês cadastrado pelo usuario
    item_1 = user1.add_items_fatura(1, 1, 1,  "Luz", 175.89,  13,   1,   'pendente')
    item_2 = user1.add_items_fatura(2, 1, 1,  "Gás", 125.25, 20, 1, 'pago')
    item_3 = user1.add_items_fatura(3, 1, 1,  "Mercado", 468.89, 25, 1, 'pendente')
    item_4 = user1.add_items_fatura(4, 1, 1,  "Cartão Credito", 2190.65, 19, 1, 'pago')
    item_5 = user1.add_items_fatura(5, 1, 1,  "Carrefour", 650.65, 19, 1, 'pago')

    # Add produtos que serão vendidos pelo usuario cadastrado.
    produto1 = user1.cadastrar_produtos(1, 1, "Mouse xyz", 99.99, 35.36)
    produto2 = user1.cadastrar_produtos(2, 1, "Teclado xyz", 135.35, 70.99)
    produto3 = user1.cadastrar_produtos(3, 1, "Som xyz", 278.99, 169.99)
    produto4 = user1.cadastrar_produtos(4, 1, "Monitor xyz", 999.69, 475.98)
    produto4 = user1.cadastrar_produtos(5, 1, "Cabo HDMI", 999.69, 475.98)
    produto5 = user1.cadastrar_produtos(6, 2, "Som xyz", 278.99, 169.99)
    produto6 = user1.cadastrar_produtos(7, 2, "Monitor xyz", 999.69, 475.98)

    # Atualizando as informações do produto cadastrado. (Nome, valor de compra, valor de venda)
    # alt1 = user1.atualizar_produto(1, 1, "Maquina de Lavar", 1_350.75, 875.92)
    
    # Deleta um produto cadastrado pelo usuario por id do produto.
    # remover_produto = user1.remover_produtos_cadastrado(1,1)
    # Escrita_na_tela.msg(remover_produto)

    
    # Listar Itens da fatura cadastrados
    # items = user1.listar_itens_fatura(1, 'pendente')

    # adicionando novo historico de vendas
    hv1 = user1.add_histico_vendas_mes(1, 1, 1, 'Mouse xyz', 'janeiro', 75)
    hv2 = user1.add_histico_vendas_mes(1, 2, 1, 'Cabo HDMI', 'janeiro', 65)
    hv3 = user1.add_histico_vendas_mes(1, 3, 1, 'Teclado xyz', 'janeiro', 150)
    hv4 = user1.add_histico_vendas_mes(1, 4, 2, 'Som xyz', 'fevereiro', 35)
    hv5 = user1.add_histico_vendas_mes(1, 5, 2, 'Monitor xyz', 'fevereiro', 15)

    relatorio = user1.listar_historico_vendas(1)
    print(relatorio)
    Escrita_na_tela.historico_venda(relatorio)

    # fat = user1.listar_faturas(1)    
    # Escrita_na_tela.listar_faturas(items, status="pendente", mes=1)