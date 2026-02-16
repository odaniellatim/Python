from Escrita_na_tela import Escrita_na_tela
from Item_despesa import Item_despesa

class Fatura_mensal:

    def __init__(self, id_fatura, user_id, mes_fatura) -> None:
        self.id_fatura = id_fatura
        self.user_id = user_id
        self.mes_fatura = mes_fatura
        self.items: list[Item_despesa] = [] # Item_despesa() 
    
    def listar_nome_fatura(self, id_user):
        if(id_user == self.user_id):
            return self.mes_fatura

    def adicionar_despesa(self,id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento):
        despesa = Item_despesa(id_item, id_fatura, id_user, nome_despesa, valor_pago, dia, mes, status_pagamento)
        self.items.append(despesa)
        return self.items
    
    def remover_item_fatura(self,id_user, id_despesa):
        item_removido = []
        for item in self.items:
            if(item.id_item == id_despesa and item.id_fatura == id_user):
                # print(f"{item.nome_despesa } apagado com sucesso.")
                item_removido.append(item.nome_despesa)
                item_removido.append('removido')
                self.items.remove(item)
                break
        return item_removido

    def listar_items_fatura(self, status: str | None = None) -> list:
        
        total_fatura = 0
        total_items_fatura = []
        
        if (status != None):
            for item in self.items:
                if(item.status_pagamento == status):                 
                    total_fatura += item.valor_pago;
                    total_items_fatura.append({
                        "id": item.id_item,
                        "nome_despesa": item.nome_despesa,
                        "valor_pago": item.valor_pago,
                        "dia_vencimento": item.dia_vencimento,
                        "mes_vencimento": item.mes_vencimento,
                        "status_pagamento": item.status_pagamento,
                        "total_fatura": total_fatura,
                    })
            return total_items_fatura
        else:
            for item in self.items:                 
                total_fatura += item.valor_pago;
                total_items_fatura.append({
                    "id": item.id_item,
                    "nome_despesa": item.nome_despesa,
                    "valor_pago": item.valor_pago,
                    "dia_vencimento": item.dia_vencimento,
                    "mes_vencimento": item.mes_vencimento,
                    "status_pagamento": item.status_pagamento,
                    "total_fatura": total_fatura,
                })
            return total_items_fatura
 
    def alterar_dia_item_fatura(self, id_despesa, nova_data):
        item_alterado = []
        if(nova_data >=1 and nova_data <= 31):
            for item in self.items: 
                
                if(item.id_item == id_despesa and nova_data != item.dia_vencimento):
                    item_alterado.append(item.nome_despesa)
                    item_alterado.append('alterado')
                    item.alterar_dia_vencimento(nova_data)
                    return item_alterado
                else:
                    Escrita_na_tela.alerta("Informe uma data diferente da já cadastrada.")
                    break
        else:
            Escrita_na_tela.alerta("Informe uma data maior que 0 e menor que 31")
        return item_alterado
        
    def altear_mes_item_fatura(self, id_despesa, nova_data):
        item_alterado = []
        if(nova_data >= 1 and nova_data <= 12):
            for mes in self.items:
                if(mes.id_item == id_despesa and mes.mes_vencimento != nova_data):
                    item_alterado.append(mes.nome_despesa)
                    item_alterado.append('alterado')
                    mes.alterar_mes_vencimento(nova_data)
                    return item_alterado
                else:
                    Escrita_na_tela.alerta("Informe uma data diferente da já cadastrada.")
                    break
        else:
            Escrita_na_tela.alerta("Informe um numero do mês valido.")
        return item_alterado

    def alterar_status_item_fatura(self, id_item, status):
 
        for item in self.items:
            if(item.id_item == id_item):
                item_alterado = item.alterar_status_item(status)
                if(item_alterado):
                    return [
                        item.nome_despesa,
                        'alterado'
                    ]
        return []
            

if __name__ == "__main__":
    jan = Fatura_mensal(1, 1, "janeiro")

                                # id_item - id_fatura - nome - valor - dia - mes - status
    item_1 = jan.adicionar_despesa(1, 1, 1,  "Luz", 175.89,  13,   1,   'pendente')
    item_2 = jan.adicionar_despesa(2, 1, 1, "Gás", 125.25, 20, 1, 'pago')
    item_3 = jan.adicionar_despesa(3, 1, 1, "Mercado", 468.89, 25, 1, 'pendente')
    item_4 = jan.adicionar_despesa(4, 2, 1, "Cartão Credito", 2190.65, 19, 1, 'pago')
    item_5 = jan.adicionar_despesa(5, 2, 1, "Carrefour", 650.65, 19, 1, 'pago')
    
    
    # item_removido = jan.remover_item_fatura(1, 2)
    # item_alterado_dia = jan.alterar_dia_item_fatura(2, 30)
    # item_alterado_mes = jan.altear_mes_item_fatura(2, 3)
    # alterar_status_item = jan.alterar_status_item_fatura(4,'Pendente')
    
    # Escrita_na_tela.msg(item_removido)
    # Escrita_na_tela.msg(item_alterado_dia)
    # Escrita_na_tela.msg(item_alterado_mes)
    # Escrita_na_tela.msg(alterar_status_item)

    fat01 = jan.listar_items_fatura(status="pendente")
    Escrita_na_tela.listar_faturas(fat01, mes=2, status="pendente")

    