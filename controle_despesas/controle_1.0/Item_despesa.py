class Item_despesa:
    
    def __init__(self,id_item, id_fatura, user_id, nome_despesa, valor_pago, dia_vencimento, mes_vencimento, status_pagamento) -> None:
        self.id_item = id_item
        self.id_fatura = id_fatura
        self.user_id = user_id
        self.nome_despesa = nome_despesa
        self.valor_pago =  valor_pago
        self.dia_vencimento = dia_vencimento
        self.mes_vencimento = mes_vencimento
        self.status_pagamento = status_pagamento

    def alterar_dia_vencimento(self, novo_vencimento):
        self.dia_vencimento = novo_vencimento

    def alterar_mes_vencimento(self, novo_vencimento):
        self.mes_vencimento = novo_vencimento

    def alterar_status_item(self, status_novo):
        txt = status_novo.lower()
        if not(txt == self.status_pagamento):            
            self.status_pagamento = txt
            return True
        else:
            return False