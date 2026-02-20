from datetime import date
import locale
import re

class ItemDespesa:
    def __init__(self,id_item: int, id_fatura: int, nome_despesa: str, valor_pago: float, data_vencimento: date, status_pagamento: str) -> None:
        self._item_id: int = id_item
        self._fatura_id: int = id_fatura
        self._item_nome_despesa: str = nome_despesa
        self._item_valor_pago: float =  valor_pago
        self._item_data_vencimento: date = data_vencimento
        self._item_status_pagamento: str = status_pagamento

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
        return self._item_valor_pago
    
    @item_valor_pago.setter
    def item_valor_pago(self, novo_valor_item):
        if(novo_valor_item <= 0):
            raise ValueError(f"Valor não pode ser menor ou igual 0. Informe um valor valido!")
        else:
            self._item_valor_pago = float(novo_valor_item)
            print(f"{self.item_nome_despesa} teve seu valor alterado para R$ {self.item_valor_pago:.2f} com sucesso!")   

    @property
    def item_data_vencimento(self) -> date:
        return self._item_data_vencimento

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
    def item_mes_vencimento_numero(self):
        data_completa = self._item_data_vencimento.strftime("%m")
        return int(data_completa)

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
        legenda = ["ID fatura", "ID despesa.", "Status pagamento","Descrição", "Valor R$", "Data vencimento" ]
        space = 50

        print('.' * (space+10))
        print("")
        print(f"{legenda[0].ljust(space, "_")} {self.fatura_id:02d}")
        print(f"{legenda[1].ljust(space, "_")} {self.item_id:02d}")
        print(f"{legenda[2].ljust(space, "_")} {self.item_status_pagamento}")
        print(f"{legenda[3].ljust(space, "_")} {self.item_nome_despesa}")        
        print(f"{legenda[4].ljust(space, "_")} {locale.currency(self.item_valor_pago, grouping=True)}")
        print(f"{legenda[5].ljust(space, "_")} {date.strftime(self._item_data_vencimento,"%d/%m/%Y")}")
        print("")
    
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
    # Seta a localização das datas e moedas
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    item = ItemDespesa(1, 1,"telEFone",150.00, date.today(),"pendente")
    print(f"DAta: {item.item_mes_vencimento_numero}")
    try:
        item.item_nome_despesa = "MAracuJA"
        print(item.item_valor_pago)
    except ValueError as e:
        print(f"Erro: {e}")