from datetime import date
import locale
import calendar
from Item_despesa import ItemDespesa

class FaturaMensal:

    def __init__(self, fatura_id, user_id, fatura_nome_mes) -> None:
        self.fatura_id = fatura_id
        self._user_id = user_id
        self._fatura_mes_nome: date = fatura_nome_mes
        self.items_despesa: list[ItemDespesa] = [] # Item_despesa() 
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def fatura_mes_nome(self):
        return date.strftime(self._fatura_mes_nome, "%B")
    
    @property
    def fatura_mes_numero(self):
        return date.strftime(self._fatura_mes_nome, "%m")
    
    def fatura_add_despesas(self, id_item, id_fatura, nome_despesa, valor_pago, data_vencimento, status_pagamento):
        add_despesa = ItemDespesa(id_item, id_fatura, nome_despesa, valor_pago, data_vencimento, status_pagamento)
        self.items_despesa.append(add_despesa)
        return self.items_despesa

    def fatura_listar_despesas(self, fatura_id: int = 0, despesa_mes: int = 0):
        valor_total = 0

        if(fatura_id != 0 and despesa_mes != 0):
            # Lista todas as despesas disponiveis filtrando por mes_vencimento e fatura id
                print(f"Lista de despesas do mês {calendar.month_name[despesa_mes].title()} e com a fatura ID {fatura_id}")

                for despesa in self.items_despesa:
                    if(despesa.item_mes_vencimento_numero == despesa_mes and despesa.fatura_id == fatura_id ):
                        valor_total += float(despesa.item_valor_pago)
                        despesa.listar_items_formatado
                            
        elif(fatura_id != 0):
            # Lista todas as despesas disponiveis filtrando por fatura_id
                print(f"Lista de despesas da fatura com ID: {fatura_id}")
                count = []

                for despesa in self.items_despesa:        
                    if(despesa.fatura_id == fatura_id):
                        count.append(despesa.fatura_id)
                        if(len(count) > 0): 
                            valor_total += float(despesa.item_valor_pago)
                            despesa.listar_items_formatado
                        else:
                            raise ValueError(f"Fatura com ID: {fatura_id} nenhuma despesa encontrada.")
                
        elif(despesa_mes != 0):
            if(despesa_mes > 0 and despesa_mes <= 12 ):
                # Lista todas as despesas disponiveis filtrando por fatura_id
                print(f"Lista de despesas com vencimento no mês: {calendar.month_name[despesa_mes].title()}")
                for despesa in self.items_despesa:
                    if(despesa.item_mes_vencimento_numero == despesa_mes):
                        valor_total += float(despesa.item_valor_pago)
                        despesa.listar_items_formatado
            else:
               raise ValueError(f"Mês não encontrado. Informe um numero entre 1 - 12.")

        else:
            # Lista com todas as despesas disponiveis sem filtro
            print("Lista de despesas pendentes e pagas")
            for despesa in self.items_despesa:
                valor_total += float(despesa.item_valor_pago)
                despesa.listar_items_formatado

        txt_desc = "Valor total a pagar:"
        print(f"{txt_desc.ljust(50, "_")} {locale.currency(valor_total, grouping=True)}")
    
    def fatura_listar_valor_total_mes(self):
        print("Relatorio dos valores pagos mensalmente.")
        print("-" * 50)
        relatorio_mes = {}
        
        for despesa in self.items_despesa:                        
            mes = despesa.item_data_vencimento.strftime("%m")
            
            if(mes not in relatorio_mes):               
                relatorio_mes[mes] = []         
            relatorio_mes[mes].append(despesa.item_valor_pago) 

        for mes, valores in relatorio_mes.items():
            print(f"Mês: {calendar.month_name[int(mes)].title().ljust(50, ("."))}Total: {locale.currency(sum(valores), grouping=True)}")

    def fatura_remover_despesa(self, id_despesa):
        item_removido = []

        for rm_despesa in self.items_despesa:
            if(rm_despesa.item_id ==id_despesa):
                print(f"Item ({rm_despesa.item_nome_despesa}) removido com sucesso.")
                item_removido.append(rm_despesa.item_nome_despesa)
                self.items_despesa.remove(rm_despesa)
        if(len(item_removido) == 0):
            raise ValueError(f"Item com o ID {id_despesa} não encontrado.")

    def fatura_alterar_status_item_despesa(self, id_despesa, status_despesa):
        status_pagamento_despesa = status_despesa.upper()
        for despesa in self.items_despesa:
            if(despesa.item_id == id_despesa):
                if(despesa.item_status_pagamento != status_pagamento_despesa):
                    despesa.item_status_pagamento = status_pagamento_despesa
                else:
                    raise ValueError(f"Não foi possivel alterar o status do pagamento. Informe um status diferente do informado.")


if __name__ == "__main__":
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        jan = FaturaMensal(1, 1, date.today())

        fatura_id1 = 1
        fatura_id2 = 2

        mes_fatura1 = 1
        mes_fatura2 = 2
        mes_fatura3 = 3

                                    # id_item - id_fatura - nome - valor - data - status
        item_1 = jan.fatura_add_despesas(1, fatura_id1,"Luz", 175.89,  date(2026, 1, 2), 'pendente')
        item_2 = jan.fatura_add_despesas(2, fatura_id2, "Gás", 125.25, date(2026, 2, 7), 'pago')
        item_3 = jan.fatura_add_despesas(3, fatura_id1, "Mercado", 468.89, date(2026, 3, 10), 'pendente')
        item_4 = jan.fatura_add_despesas(4, fatura_id2, "Cartão Credito", 2190.65, date(2026, 2 , 15), 'pago')
        item_5 = jan.fatura_add_despesas(5, fatura_id1, "Carrefour", 650.65, date(2026, 1, 20), 'pago')

        # print("-" * 70)
        # print(f"{jan.fatura_mes_nome} | {jan.fatura_mes_numero}") 

        # print("-" * 70)
        # jan.fatura_listar_despesas(despesa_mes=2)
        
        print("-" * 70)
        jan.fatura_listar_valor_total_mes()

        print("-" * 70)
        jan.fatura_remover_despesa(3)
        jan.fatura_alterar_status_item_despesa(2, "pendente")
        
        print("-" * 70)
        jan.fatura_listar_despesas(despesa_mes=2)
    
    except ValueError as e:
        print(f"Erro: {e}")
    
    
    except locale.Error as e:
        print(f"Locale error: {e}")
