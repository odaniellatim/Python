from datetime import date
import re

class Item_despesa:
    
    def __init__(self,id_item, id_fatura, nome_despesa, valor_pago, data_vencimento, status_pagamento) -> None:
        self._item_id = id_item
        self._fatura_id = id_fatura
        self._item_nome_despesa = nome_despesa
        self._item_valor_pago =  valor_pago
        self._item_data_vencimento: date = data_vencimento
        self._item_status_pagamento = status_pagamento

    @property
    def item_id(self):
        return self._item_id
    
    @property
    def fatura_id(self):
        return self._fatura_id
    
    @property
    def item_nome_despesa(self):
        return f"{self._item_nome_despesa.title()}"
    
    @item_nome_despesa.setter
    def item_nome_despesa(self, novo_nome_despesa):
        
        old_nome = self.item_nome_despesa
        nome_limpo = novo_nome_despesa.strip()
        total_caracteres = len(nome_limpo)
        expressao = r"[\-\*\/\|\\\(\)\[\]\{\}\?\!\'\" ]"

        if(re.search(expressao, novo_nome_despesa)):
            raise ValueError(f"{novo_nome_despesa} contem caracteres especiais. Use apenas letras e numeros.")

        if(total_caracteres <= 2):
            raise ValueError(f"O nome da despesa não pode estar vazio ou ter apenas duas letras.")
        elif(total_caracteres > 50):
            raise ValueError(f"Informe um nome da despesa com no maximo 50 caracteres. Atualmente o novo nome tem {total_caracteres} caracteres")
        else:
            self._item_nome_despesa = novo_nome_despesa
            print(f"A Despesa \"{old_nome}\" foi alterado para \"{self.item_nome_despesa}\" com sucesso!")
    
    @property
    def item_valor_pago(self):
        return round(self._item_valor_pago, 2)
    
    @item_valor_pago.setter
    def item_valor_pago(self, novo_valor_item):
        if(novo_valor_item <= 0):
            raise ValueError(f"Valor não pode ser menor ou igual 0. Informe um valor valido!")
        else:
            self._item_valor_pago = float(novo_valor_item)
            print(f"{self.item_nome_despesa} teve seu valor alterado para R$ {self.item_valor_pago:.2f} com sucesso!")   

    @property
    def item_data_vencimento(self) -> str:
        return date.strftime(self._item_data_vencimento,"%d/%m/%Y")

    @item_data_vencimento.setter
    def item_data_vencimento(self, nova_data_vencimento):

        data_atual = self.item_data_vencimento
        expressao = r"[\-\*\/\|\\\(\)\[\]\{\}\?\!\'\" ]" # Expressão regular para validar 
        data_sep = re.split(expressao, nova_data_vencimento.strip())

        # Levanta uma ecessão de erro caso a data nao tenha / ou - para separar os elementos.
        if (expressao in nova_data_vencimento) :
            raise ValueError(f"Informe a data nos seguites formatos: DD-MM-YYYY | DD/MM/YYYY.")

        # Verifica se tem 3 elementos no array onde vai ter dia mes ano.
        if(len(data_sep) == 3):
            self._item_data_vencimento = date(int(data_sep[2]),int(data_sep[1]), int(data_sep[0]))
        else:
            raise ValueError(f"Insira uma data valida. Use um dos formatos: DD-MM-YYYY | DD/MM/YYYY.")
        
        print(f"{self.item_nome_despesa} com a data de vencimento: {data_atual} foi alterado para {self.item_data_vencimento}")

    @property
    def item_status_pagamento(self):
        return self._item_status_pagamento.upper()
    
    @item_status_pagamento.setter
    def item_status_pagamento(self, novo_status_pagamento: str):
        status = novo_status_pagamento.lower()
        old_status = self.item_status_pagamento.lower()

        if(old_status == status):
            raise ValueError(f"{self.item_nome_despesa} já está com status de pagamento {self.item_status_pagamento}")
        
        match(status):
            case 'pago':
                self._item_status_pagamento = status
            case 'pendente':
                self._item_status_pagamento = status
            case _:
                raise ValueError(f"Tipo de pagamento invalido. Selecione entre PAGO ou PENDENTE.")

        print(f"{self.item_nome_despesa} teve o status de {old_status.upper()} alterado para {self.item_status_pagamento}")

    @property
    def listar_items_formatado(self):
        legenda = ["ID Item.", "Descrição", "Valor R$", "Data vencimento" ]
        space = 50

        print('.' * (space+10))
        print("")
        print(f"{legenda[0].ljust(space, "_")} {self.fatura_id}")
        print(f"{legenda[1].ljust(space, "_")} {self.item_nome_despesa}")
        print(f"{legenda[2].ljust(space, "_")} {self.item_valor_pago:.2f}")
        print(f"{legenda[3].ljust(space, "_")} {self.item_data_vencimento}")
        print("")
        print('.' * (space+10))
    
    def listar_dados_item_obj(self):
        obj = {
            "item_id": self.item_id,
            "fatura_id": self.fatura_id,
            "item_nome": self.item_nome_despesa,
            "item_valor": self.item_valor_pago,
            "item_data": self.item_data_vencimento,
            "item_status": self.item_status_pagamento
        }
        return obj

if __name__ == "__main__":
    item = Item_despesa(1, 1,"telEFone",150.00, date.today(),"pendente")

    try:
        item.item_nome_despesa = "MAracuJA"

        item.listar_items_formatado
        print(f"\n{item.listar_dados_item_obj()}\n")

    except ValueError as e:
        print(f"Erro: {e}")