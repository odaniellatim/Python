class Escrita_na_tela:
    @staticmethod
    def alerta(msg):
        print(msg)
    
    @staticmethod
    def msg(items: list) ->None:
        #Status = True or False
        if(items != None and len(items) > 0):
            
            if(len(items) >= 1):
                print(f"{items[0]} foi {items[1]} com sucesso. ")
            else:
                print(f"Item não encontrado. ")

  
    @staticmethod
    def listar_faturas(faturas: list, space = 45, status = None, mes = None):
        txt_legend = ["ID", "Nome Fatura", "Valor R$", "Vencimento", "Vencimento", "Status", "Total Pago/Pendente"]
        
        if(faturas):
            if(status == None):
                titulo = f"LISTA DE DESPESAS PENDENTES E PAGAS"
                print("-" * space)
                print(f"|{titulo.center(space)}|")
            elif(status == 'pago'):
                titulo = f"LISTA DE DESPESAS PAGAS MÊS: {mes}"
                print("-" * space)
                print(f"|{titulo.center(space)}|")
            else:
                titulo = f"LISTA DE DESPESAS PENDENTES MÊS: {mes}"
                print("-" * space)
                print(f"|{titulo.center(space)}|")

            for fatura in faturas:
                print("-" * space)
                print("")
                print(f"{txt_legend[0].ljust(space, '.')} {fatura['id']}")

                print(f"{txt_legend[1].ljust(space, '.')} {fatura['nome_despesa']}")

                print(f"{txt_legend[2].ljust(space, '.')} R$ {round(fatura['valor_pago'], 2)}")

                print(f"{txt_legend[3].ljust(space, '.')} Dia {fatura['dia_vencimento']}")

                print(f"{txt_legend[4].ljust(space, '.')} Mês {fatura['mes_vencimento']}")
                
                print(f"{txt_legend[5].ljust(space, '.')} {fatura['status_pagamento']}")
                print("")

            print("_" * space)
            print(" ")
            print(f"{str(txt_legend[6].ljust(space, '.'))} R$ {round(fatura['total_fatura'], 2)}")
            print(" ")
            print("_" * space)
        else:
            print("Nenhum Item Cadastrado")

    @staticmethod
    def listar_produtos(lista_produtos: list, space = 45):
        
        titulo = f"LISTA DE PRODUTOS CADASTRADOS"
        print("-" * space)
        print(f"|{titulo.center(space)}|")
        
        txt_legend = ["ID", "Nome Produto", "Valor Venda R$", "Valor Compra R$", "Total Valor de Venda R$", "Total Valor de Compra R$", "Total Lucro R$"]
        total_venda = 0
        total_compra = 0
        
        if(lista_produtos):
            for produto in lista_produtos:
                print("-" * space)
                print("")
                print(f"{txt_legend[0].ljust(space, '.')} {produto['id_produto']}")

                print(f"{txt_legend[1].ljust(space, '.')} {produto['nome_produto']}")

                print(f"{txt_legend[2].ljust(space, '.')} R$ {round(produto['valor_venda'], 2)}")

                print(f"{txt_legend[3].ljust(space, '.')} Dia {round(produto['valor_compra'], 2)}")

                total_venda += produto['valor_venda']
                total_compra += produto['valor_compra']
                
                print("")
            
            lucro = total_venda - total_compra
            print("_" * space)
            print(" ")
            print(f"{str(txt_legend[4].ljust(space, '.'))} R$ {round(total_venda, 2)}")
            print(f"{str(txt_legend[5].ljust(space, '.'))} R$ {round(total_compra, 2)}")
            print(f"{str(txt_legend[6].ljust(space, '.'))} R$ {round(lucro, 2)}")
            print(" ")
            print("_" * space)
        else:
            print("Nenhum produto cadastrado")

    @staticmethod
    def historico_venda(lista_historico: list, mes=None, space=45):
        titulo = f"HISTORICO DE VENDAS DO MÊS {mes}"
        print("-" * space)
        print(f"|{titulo.center(space)}|")
        
        txt_legend = ["ID", "Nome Produto", "Mês Relatorio", "Total Itens Vendidos", "Lucro R$", "Valor Total Vendidos R$"]
        total_venda = 0
        total_compra = 0
        
        if(lista_historico):
            for hv in lista_historico:
                print("-" * space)
                print("")
                print(f"{txt_legend[0].ljust(space, '.')} {hv['id_registro']}")

                print(f"{txt_legend[1].ljust(space, '.')} {hv['produto_nome']}")

                print(f"{txt_legend[2].ljust(space, '.')} {hv['mes_nome']}")

                print(f"{txt_legend[3].ljust(space, '.')} R$ {round(hv['total_vendidos'], 2)}")

                print(f"{txt_legend[4].ljust(space, '.')} R$ {round(hv['lucro'], 2)}")

                print(f"{txt_legend[5].ljust(space, '.')} R$ {round(hv['valor_total_vendas'], 2)}")
                
                print("")
            
            lucro = total_venda - total_compra
            print("_" * space)
            print(" ")
            # print(f"{str(txt_legend[4].ljust(space, '.'))} R$ {round(total_venda, 2)}")
            # print(f"{str(txt_legend[5].ljust(space, '.'))} R$ {round(total_compra, 2)}")
            # print(f"{str(txt_legend[6].ljust(space, '.'))} R$ {round(lucro, 2)}")
            print(" ")
            print("_" * space)
        else:
            print("Nenhum produto cadastrado")
    
    @staticmethod
    def relatorio_vendas(lista_historico: list, mes=None, space=45):
        titulo = f"HISTORICO DE VENDAS DO MÊS {mes}"
        print("-" * space)
        print(f"|{titulo.center(space)}|")
        
        txt_legend = ["ID Registro: ", "Nome Produto", "Mês Relatorio", "Total Itens Vendidos", "Lucro R$", "Valor Total Vendidos R$"]
        total_venda = 0
        total_compra = 0
        
        if(lista_historico):
            for hv in lista_historico:
                print("-" * space)
                print("")
                print(f"{txt_legend[0].ljust(space, '.')} {hv['id_registro']}")

                print(f"{txt_legend[1].ljust(space, '.')} {hv['produto_nome']}")

                print(f"{txt_legend[2].ljust(space, '.')} {hv['mes_nome']}")

                print(f"{txt_legend[3].ljust(space, '.')} {round(hv['total_vendidos'], 2)}")

                print(f"{txt_legend[4].ljust(space, '.')} R$ {round(hv['lucro'], 2)}")

                print(f"{txt_legend[5].ljust(space, '.')} R$ {round(hv['valor_total_vendas'], 2)}")
                
                print("")
            
            lucro = total_venda - total_compra
            print("_" * space)
            print(" ")
            # print(f"{str(txt_legend[4].ljust(space, '.'))} R$ {round(total_venda, 2)}")
            # print(f"{str(txt_legend[5].ljust(space, '.'))} R$ {round(total_compra, 2)}")
            # print(f"{str(txt_legend[6].ljust(space, '.'))} R$ {round(lucro, 2)}")
            print(" ")
            print("_" * space)
        else:
            print("Nenhum produto cadastrado")