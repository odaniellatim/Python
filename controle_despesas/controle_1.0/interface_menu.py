import os
from Gerenciador_sistema import Gerenciador_sistema

class Interface_menu:
    def __init__(self) -> None:
        self.user_id = id(self)
        self.gerenciado_sistema = Gerenciador_sistema()
    
    def menu_inicial(self):
            print("1. Entrar com uma conta.")
            print("2. Criar uma conta.")
            print("3. Fechar Programa")

            print("." * 50)
            opcao = int(input("Selecione uma opção: "))

            if(opcao == 1):
                ...
            elif(opcao == 2):
                self.criar_usuario()
            if(opcao == 3):
                exit()
        
    def criar_usuario(self):
        nome_completo = input("Informe seu nome completo: ")
        usuario_login = input("Informe um nome de usario: ")
        senha_usuario = input("informe sua senha: ")

        self.gerenciado_sistema.cadastrar_usuario(self.user_id, nome_completo, usuario_login, senha_usuario)
        
    
    def logar_no_sistema(self)-> dict:

        usuario = input(" Informe seu usuario: ")
        senha = input(" Informe sua senha: ")
        
        return {
            "usuario": usuario,
            "senha": senha
        }
    
    def user_logado(self):
        # os.system("clear")
        print("1. Adicionar mês Despesas: ")
        print("2. Adicionar despesas: ")
        # print("3. Adicionar Produto: ")
        # print("4. Relatório Mensal: ")
        # print("5. Relatório Anual: ")
        # print("6. Dados da Conta: ")
        # print("7. Excluir Conta: ")
        # print("8. Fechar programa")

        opcao = int(input("Informe um numero do menu: "))

        if(opcao == 8):
            exit()
        elif(opcao == 1):
            self.menu_add_mes_despesas()

        print(f"Opcao selecionado: {opcao}")
    
    def menu_add_mes_despesas(self):
        
        id_fatura = id(self)
        id_user = self.gerenciado_sistema.user_id()
        id_nome_mes = input("Digite o nome do mês da fatura: ")
        print(id_fatura, id_user, id_nome_mes)
        self.gerenciado_sistema.cadastrar_fatura(id_fatura, id_user, id_nome_mes)
        print("Cadastro realizado com sucesso.")

    def menu_add_items_despesas(self):
        #id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento
        id_item = id(self)
        id_fatura = id(self)
        id_user = self.gerenciado_sistema.user_id()
        nome_despesa = input("Informe o nome da despesa: ")
        valor_pago = float(input("Informe o valor da despesa R$: "))
        dia = int(input("informe o dia do vencimento: "))
        mes = int(input("Informe o nome do mês de vencimento: "))
        
        print("Essa conta está Pago ou Pendente: 1. Pago | 2. Pendente")        
        status_pagamento = int(input("Selecione uma opcao: "))
        
        if(status_pagamento == 1):
            status_pagamento = "pago"
        else:
            status_pagamento = "pendente"
        
        print(id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento)
        self.gerenciado_sistema.add_items_fatura(id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento)
        print("cadastro realizado")