class CadastroItens:
    '''
    Classe base para usar as principais caracteristicas, evitando
    repetir itens no construtor de um cadastro.
    '''
    def __init__(self, cadastro_id: int, cadastro_nome: str, cadastro_valor: float ):
        self.cadastro_id: int = cadastro_id
        self.cadastro_nome: str = cadastro_nome
        self._cadastro_valor: float = cadastro_valor

    @property
    def get_item_valor(self):
        return self._cadastro_valor

    @get_item_valor.setter
    def set_item_valor(self, novo_valor_item):
        if novo_valor_item != "":
            self._cadastro_valor = novo_valor_item
        else:
            return False

if __name__ == "__main__":
    from materiais import Materiais
    item = Materiais(1, "Nome Material", 150.99, 150, 'g')
    
    item.mt_listar_materiais()
    item.set_item_valor = 140.99
    item.mt_listar_materiais()
