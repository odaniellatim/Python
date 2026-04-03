class Custo_Fixo:

    def __init__(self, custo_fixo_id, custo_fixo_nome, custo_fixo_valor, custo_fixo_status, custo_fixo_numero_vendas, custo_fixo_durabilidade_meses, custo_fixo_valor_total_mes):

        self.custo_fixo_id = custo_fixo_id
        self.custo_fixo_nome = custo_fixo_nome
        self.custo_fixo_valor = custo_fixo_valor
        self.custo_fixo_numero_vendas = custo_fixo_numero_vendas
        self.custo_fixo_status = custo_fixo_status
        self.custo_fixo_durabilidade_meses = custo_fixo_durabilidade_meses
        self.custo_fixo_valor_total_mes = custo_fixo_valor_total_mes
        self.dias_mes = 30

    def custo_fixo_durabilidade_dias(self):
        """
        Retorna o valor total de dias que serão necessarios para pagar o produto
        Geralmente o produto já está pago, mas em algumas situações pode ser
        interessante prolongar o pagamento para ter uma margem maior no lucro
        """
        return round(self.custo_fixo_durabilidade_meses * self.dias_mes)

    def custo_fixo_total_projetos(self):
        """
        Retorn o numero total de projetos necessarios para pagar o produto
        completamente, em alguns casos esse numero é usado para ter controle
        das despesas fixas que tem como vencimento mensal, garantindo que nao
        vai faltar dinheiro para pagar essas contas.

        @param numero_projetos int -> Esse é o numero ideal de produtos/projetos vendidos,
        para garatir que os custos não serão acima do necessario,
        quanto maior o numero de projetos maior a margem de lucro,
        e também controle no preco final do projeto/produto.
        """
        projetos = self.custo_fixo_durabilidade_meses * self.custo_fixo_numero_vendas
        return projetos

    def custo_fixo_valor_por_projeto(self):
        return self.custo_fixo_valor / self.custo_fixo_total_projetos()

    def custo_fixo_total_porcentagem(self):
        return round((self.custo_fixo_valor_por_projeto() / self.custo_fixo_valor_total_mes) * 100, 2)

    def custo_fixo_valor_pago_mensal(self):
        return self.custo_fixo_numero_vendas * self.custo_fixo_valor_por_projeto()

    def custo_fixo_valor_total(self, load_data: list):
        """
        Retorna o valor de custo mensal com base na quantidade de vendas planejada mensalmente
        Os valores podem mudar de acordo com a quantidade de vendas mensal planejada.
        Esse valor é o que vai ser ser distribuido para cada produto de acordo com o planejamento
        de vendas, por isso é importante não ter poucas vendas e não aumentar muito para
        não perder o controle.
        """
        valor_total = 0
        for item in load_data:
            if item['custo_fixo_valor_por_projeto']:
                valor_total += item['custo_fixo_valor_por_projeto']
        return valor_total

    def custo_fixo_atualizar_items(
            self,
            id_item_update,
            conexao_bd,
            custo_fixo_nome=None,
            custo_fixo_valor=None,
            custo_fixo_status=None,
            custo_fixo_durabilidade_meses=None
    ):
        # Local onde vamos armazernar o novo objeto atualizado
        item_update = None

        # Carrega os dados do arquivo para selecionar o id correto para atualizar.
        load_data = conexao_bd.bd_load_data()

        # Variaveis usadas para construir o novo objeto e atualizar as informações
        # que o usuario não pode informar, devido as operações matematicas internas.
        cf_nome = None
        cf_valor = None
        cf_status = None
        cf_durabilidade_meses = None
        cf_numero_vendas = None
        cf_valor_pago_mensal = None

        for data in load_data:
            if data["custo_fixo_id"] == id_item_update:

                item_update = data
                load_data.remove(data)

                for key, value in item_update.items():
                    if key == "custo_fixo_nome":
                        if (custo_fixo_nome != None):
                            item_update[key] = custo_fixo_nome
                            cf_nome = custo_fixo_nome
                        else:
                            cf_nome = value
                    if key == "custo_fixo_valor":
                        if custo_fixo_valor != None:
                            item_update[key] = custo_fixo_valor
                            cf_valor = custo_fixo_valor
                        else:
                            cf_valor = value
                    if key == "custo_fixo_status":
                        if custo_fixo_status != None:
                            item_update[key] = custo_fixo_status
                            cf_status = custo_fixo_status
                        else:
                            cf_status = value
                    if key == "custo_fixo_durabilidade_meses":
                        if custo_fixo_durabilidade_meses != None:
                            item_update[key] = custo_fixo_durabilidade_meses
                            cf_durabilidade_meses = custo_fixo_durabilidade_meses
                        else:
                            cf_durabilidade_meses = value
                    if key == "custo_fixo_numero_vendas":
                        cf_numero_vendas = value
                    if key == "custo_fixo_valor_pago_mensal":
                        cf_valor_pago_mensal = value
                break

        # Constroi o objeto novamente para atualizar os métodos matematicos e garantir que as
        # contas necessarias estarão corretas
        update = Custo_Fixo(id_item_update, cf_nome, cf_valor, cf_status, cf_numero_vendas,
                            cf_durabilidade_meses, cf_valor_pago_mensal)

        # Chama o método get_dict() para construir novamente o dicionario com as informações
        # atualizadas e reescrever no arquivo do banco de dados json
        item = update.get_dict()

        # Com os dados do dicionario na variavel item, vamos fazer o merge dos dicionarios
        # para gravar no banco de dados json
        load_data.extend(item)

        # Resetamos o banco de dados para não reescrever novamente os dados com os dados antigos
        conexao_bd.bd_restart()

        # Escrevemos os dados no banco de dados usando o novo objeto criado.
        conexao_bd.bd_add_items(load_data)

    def get_dict(self) -> dict:
        # Método usado para salvar os dados em um arquivo json
        dicionario = {
            "custo_fixo_id": self.custo_fixo_id,
            "custo_fixo_nome": self.custo_fixo_nome,
            "custo_fixo_valor": self.custo_fixo_valor,
            "custo_fixo_numero_vendas": self.custo_fixo_numero_vendas,
            "custo_fixo_status": self.custo_fixo_status,
            "custo_fixo_durabilidade_meses": self.custo_fixo_durabilidade_meses,
            "custo_fixo_durabilidade_dias": self.custo_fixo_durabilidade_dias(),
            "custo_fixo_total_projetos": self.custo_fixo_total_projetos(),
            "custo_fixo_valor_por_projeto": self.custo_fixo_valor_por_projeto(),
            "custo_fixo_total_porcentagem": self.custo_fixo_total_porcentagem(),
            "custo_fixo_valor_pago_mensal": self.custo_fixo_valor_pago_mensal(),
        }
        # for k, v in dicionario.items():
        #     print(f"{k.ljust(30, '.')} {v}")
        return dicionario


if __name__ == "__main__":
    from src.banco_dados.banco_de_dados import Banco_de_dados

    # Nome do arquivo que vai ser usado para salvar os dados.
    bd_file_name = "teste_custo_fixo.json"

    # Nome da pasta onde vai ser salvo o banco de dados.
    bd_folder_name = "bd"

    # instancia do objeto
    cf1 = Custo_Fixo(
        1, "Telefone Celular", 5000, "pendente", 20, 50, 226.67
    )

    # Numero total de projetos para pagar a despesa / produto
    total_projetos = cf1.custo_fixo_total_projetos()

    # imprime o dicionario cadastrado
    # cf1.get_dict()

    # Atualiza um objeto atraves de um ID
    # Selecionar um item para realizar uma edição
    # os dados que vamos conseguir atualizar são

    # Nome, valor, status, durabilidade_meses
    # Conexão com o banco para puxar os dados do arquivo e atualizar corretamente.
    conexao_bd = Banco_de_dados(bd_file_name, bd_folder_name)

    # Carrega os dados do arquivo e envia para o construtor.
    load_data = conexao_bd.bd_load_data()

    id_item = 1
    nome = "Luz"
    valor = 250
    status = "pendente"
    durabilidade_meses = 1

    # update = cf1.custo_fixo_atualizar_items(id_item, conexao_bd, nome, valor, status, durabilidade_meses)

    valor_total_custo_fixo = cf1.custo_fixo_valor_total(load_data)
    print("Custo Fixo Total: ", round(valor_total_custo_fixo, 2))
    print()
