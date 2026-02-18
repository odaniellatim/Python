from Usuario import Usuario
from BD import Banco_de_dados

from Escrita_na_tela import Escrita_na_tela

class Gerenciador_sistema:
    def __init__(self) -> None:
        self.usuarios: list[Usuario] = []

    # Cadastro de usuarios no sistema.
    def cadastrar_usuario(self, id_user, nome_usuario, user_name, senha, nivel_usuario = "admin"):

        if(id_user and nome_usuario and user_name and senha and nivel_usuario):
            new_user = Usuario(id_user, nome_usuario, user_name, senha, nivel_usuario)
            self.usuarios.append(new_user)

            # Pega os dados salvo na instancia usuario e atualizado no banco de dados.
            self.salvar_dados_user_bd(new_user.__dict__) 
            return self.usuarios
    
    def user_id(self):
        for id in self.usuarios:
            return id.id_user

    # Apagar uma conta do sistema
    def deletar_usuario(self, id_user):
        for user in self.usuarios:
            if(user.id_user == id_user):
                print(f"{user.nome_usuario} deletado com sucesso.")
                self.usuarios.remove(user)
                break
    
    # Adiciona os produtos
    def add_produtos(self, id_produto: int, id_user: int, nome_produto: str, valor_venda: float, valor_compra: float):
        for user in self.usuarios:
            if(id_produto):
                produto = user.cadastrar_produtos(id_produto, id_user, nome_produto, valor_venda, valor_compra)
        return produto

    # Lista os produtos cadastrados
    def listar_produtos(self, id_user):
        for user in self.usuarios:
            if(id_user == user.id_user):
                return user.produtos_cadastrados(user.id_user)
        return []
    
    # Criar uma nova fatura para controlar as despesas.
    def cadastrar_fatura(self,id_fatura, id_user, fatura_mes: str):
        for user in self.usuarios:
            add_fatura = user.adicionar_fatura_mensal(id_fatura, id_user, fatura_mes)
            return "Fatura adicionada com sucesso"
        
    # Cadastrar uma despesa em uma fatura cadastrada
    def add_items_fatura(self, id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento):
        for user in self.usuarios:
            if(user.id_user == id_user):
                for fatura in user.lista_de_faturas:
                    if fatura.id_fatura == id_fatura:
                        fatura.adicionar_despesa(id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento)
                        break
    
    # Listar todas as despesas cadastradas no sistema, podendo separar por status (pago, pendente)
    def mostrar_items_faturas(self, id_user: int, id_fatura: int, status_fatura: str) -> list:
        for user in self.usuarios:
            if(user.id_user == id_user):
                return user.listar_itens_fatura(id_fatura, status_fatura)
        return []
    
    # Adiciona novo historico de vendas 
    def add_historico_vendas(self, user_id, id_registro, id_mes, produto_nome, mes_vendas: str, total_vendidos):
        for user in self.usuarios:
            user.add_histico_vendas_mes(user_id, id_registro, id_mes, produto_nome, mes_vendas, total_vendidos)
            break
    
    # Listas o historico de vendas de acordo com o mês e usuario
    def listar_historico_vendas(self, user_id, id_mes = None):
        for hv in self.usuarios:
            if(id_mes == None):
                return hv.listar_historico_vendas(user_id)
            else:
                return hv.listar_historico_vendas(user_id, id_mes)
        return []

    #salvar dados do usuario ao se cadastrar
    def salvar_dados_user_bd(self, data_user):
        
        new = Banco_de_dados("usuarios.json")
        new.salvar_dados_user(data_user)

    def salvar_dados_bd(self):
        data = []
        for user in self.usuarios:
            data.append({
                        "id": user.id_user,
                        "nome": user.nome_usuario,
                        "password": user.senha,
                        "nivel_usuario": user.nivel_usuario,
                        "catalogo_produtos": user.produtos_cadastrados(user.id_user),
                        "fatura":user.listar_itens_fatura(user.id_user),
                        "historico_vendas": user.listar_historico_vendas(user.id_user)
                    })

        bd = Banco_de_dados("system.json")
        bd.salvar_dados_bd(data)

    def carregar_bd(self):
        bd = Banco_de_dados("system.json")
        data = bd.ler_dados_bd()
        return data
    
    # Puxa os dados de vencimento dos items da Fatura usando Property
    def vencimento_fatura(self, user_id):
        print(f"Total de usuários na memória: {len(self.usuarios)}")
        for user in self.usuarios:
            if(user.id_user == user_id ):
                print(f"Nome: {user.nome_usuario.title()}")

                for fat in user.lista_de_faturas:
                    print(f"-- Mês: {fat.mes_fatura.title()}")

                    for i in fat.items:
                        print(f"--- Despesa: {i.nome_despesa.title()}")
                        i.data_vencimento
                    



if __name__ == "__main__":

    # Instancia da classe Gerenciador do sistema
    sys = Gerenciador_sistema()
    
    # Realiza o cadastro do usuario
    user1 = sys.cadastrar_usuario(1, "Daniel", "odaniel", "1234")
    
    # Deleta um usuario de acordo com o ID
    # remove = sys.deletar_usuario(1)

    # Add produtos que serão vendidos pelo usuario cadastrado.
    produto1 = sys.add_produtos(1, 1, "Mouse xyz", 99.99, 35.36)
    produto2 = sys.add_produtos(2, 1, "Teclado xyz", 135.35, 70.99)
    produto3 = sys.add_produtos(3, 1, "Som xyz", 278.99, 169.99)
    produto4 = sys.add_produtos(4, 1, "Monitor xyz", 999.69, 475.98)
    produto4 = sys.add_produtos(5, 1, "Cabo HDMI", 999.69, 475.98)
    produto5 = sys.add_produtos(6, 1, "Som xyz", 278.99, 169.99)
    produto6 = sys.add_produtos(7, 1, "Monitor xyz", 999.69, 475.98)

    # lista os produtos cadastrados pelo usuario
    listar_produto = sys.listar_produtos(1)
    # Escrita_na_tela.listar_produtos(listar_produto)

    # Cadastar uma fatura para adicionar as despesas
    fatura1 = sys.cadastrar_fatura(1, 1, 'janeiro')
    fatura2 = sys.cadastrar_fatura(2, 1, 'fevereiro')
    fatura3 = sys.cadastrar_fatura(3, 1, 'marco')
    # fatura4 = sys.cadastrar_fatura(4, 1, 'abril')
    # fatura5 = sys.cadastrar_fatura(5, 1, 'junho')
    # fatura6 = sys.cadastrar_fatura(6, 1, 'julho')

    #Add items fatura referente ao mês cadastrado pelo usuario
    item_1 = sys.add_items_fatura(1, 1,  1,  "Luz", 175.89,  13,   1,   'pendente')
    item_2 = sys.add_items_fatura(2, 2, 1,  "Gás", 125.25, 20, 1, 'pago')
    item_3 = sys.add_items_fatura(3, 3, 1,  "Mercado", 468.89, 25, 1, 'pendente')
    item_4 = sys.add_items_fatura(4, 1, 1,  "Cartão Credito", 2190.65, 19, 1, 'pago')
    item_5 = sys.add_items_fatura(5, 2, 1,  "Carrefour", 650.65, 19, 1, 'pago')

    # Lista os items cadastrados na fatura usando o ID
    # status = 'pago'
    # mes = 1
    # imprimir_fat = sys.mostrar_items_faturas(1, 2, status) # user, fatura
    # Escrita_na_tela.listar_faturas(imprimir_fat, mes=mes, status=status)
    # print(imprimir_fat)


    # adicionando novo historico de vendas    
    # hv1 = sys.add_historico_vendas(1, 1, 1, 'Mouse xyz', 'janeiro', 75)
    # hv2 = sys.add_historico_vendas(1, 2, 1, 'Cabo HDMI', 'janeiro', 65)
    # hv3 = sys.add_historico_vendas(1, 3, 1, 'Teclado xyz', 'janeiro', 150)
    # hv4 = sys.add_historico_vendas(1, 4, 2, 'Som xyz', 'fevereiro', 35)
    # hv5 = sys.add_historico_vendas(1, 5, 2, 'Monitor xyz', 'fevereiro', 15)

    # mes = 2
    # rs = sys.listar_historico_vendas(1, mes)
    # print(rs)
    # Escrita_na_tela.historico_venda(rs, mes)

    # Cria um arquivo "system.json" e salva os dados do usuario
    # items_bd = sys.salvar_dados_bd()
    
    # le o arquivo "system.json" e puxa todos os dados do usuario
    # items_bd = sys.carregar_bd()

    # Formata a impressão dos dados carregados do arquivo.json
    # if(len(items_bd) > 0):
    #     for item in items_bd:        
    #         for x, y in item.items():
    #             if(x == 'nome'):
    #                 print(f"Nome: {y}")

    #             if(x == 'catalogo_produtos'):
    #                 Escrita_na_tela.listar_produtos(y)
    #             if(x == 'fatura'):
    #                 Escrita_na_tela.listar_faturas(y)
    #             if(x == 'historico_vendas'):
    #                 Escrita_na_tela.historico_venda(y)
    # else:
    #     print("Nenhum usuario encontrado")
        
    i = sys.vencimento_fatura(1)
    
    import os 
    import pathlib
    dir = "BD"

    script_dir = f"{os.path.dirname(os.path.abspath(__file__))}/{dir}"
    print(script_dir)