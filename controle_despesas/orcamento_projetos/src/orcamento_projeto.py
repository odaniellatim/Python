from src.materiais import Materiais
from src.renda_mensal_base import RendaMensalBase
from src.mao_de_obra import MaoDeObra
from src.unidades_medida import UnidadeMedida

class OrcamentoProjeto:
    def __init__(self,orcamento_id: str = None, orcamento_nome: str = None) -> None:
        self.orcamento_id = orcamento_id
        self.orcamento_nome = orcamento_nome
        self.itens_materiais: list[Materiais] = []
        self.mao_de_obra: list[MaoDeObra] = []

    # cadastro de materais para realizar o orçamento do projeto
    def op_add_materiais(self, id: int, nome: str, valor: float, quantidade: int, unidade_medida: UnidadeMedida, qntd_usado_projeto: int) -> bool:  
        """ Cadastro de novos materiais para utilizar no projeto. """

        # TODO:  Validar as seguintes validações antes de realizar o cadastro.
        # TODO:  Nome não pode ser nulo
        # TODO:  Valor não pode ser menor que 0
        # TODO:  quantidade deve ser maior que 1
        # TODO:  deve ser selecionado uma unidade de medida para liquido "ml" - "l"
        # TODO:  Quantidade de produto usado no projeto não deve ser 0.
        try:
            add_materiais = Materiais(id, nome, valor, quantidade, unidade_medida, qntd_usado_projeto)
            self.itens_materiais.append(add_materiais)
            return True
        except: 
            return False

    def op_listar_materiais_cadastrados(self)-> dict:
        lista_materiais = []
        for material in self.itens_materiais:
            lista_materiais.append(material.mt_lista_cadastrados)
        return lista_materiais
    
    # Valor total pago nos materiais para ter no estoque. (Valor estoque)
    @property
    def op_valor_total_estoque(self) -> float:
        """@property: Lista o valor total pago nos produtos cadastrados. """
        valor_total = 0
        for item in self.itens_materiais:
            valor_total += item.material_valor
        return valor_total
    
    # O valor total dos produtos usados no projeto
    @property
    def op_valor_total_materiais_usados(self)-> float:
        """@property: Lista todos os materiais que estão vinculados ao projeto. """
        valor_total_usados = 0
        if(len(self.itens_materiais) > 0):
           
            for item in self.itens_materiais:            
                valor_total_usados += item.mt_valor_qntd_usado_projeto()
            return valor_total_usados
        else:
            raise ValueError("Nenhum material encontrado. Cadastre novos materiais!") 

    # Cadastro dos valores da mão de obra
    def add_mao_de_obra(self, 
                        mao_de_obra_porcentagem, 
                        mao_de_obra_horas_trabalhadas, 
                        mao_de_obra_minutos_trabalhados, 
                        mao_de_obra_taxa_de_urgencia = 0):
        """ Valor da renda mensal para o calculo da mao de obra"""
        
        info_mao_de_obra = MaoDeObra(mao_de_obra_porcentagem,
                                     mao_de_obra_horas_trabalhadas,
                                     mao_de_obra_minutos_trabalhados,
                                     mao_de_obra_taxa_de_urgencia
                                     )
        self.mao_de_obra.append(info_mao_de_obra)

    # Valor total das hora trabalhadas no projeto ( Usado para adicionar no orçamento)
    @property
    def orcamento_valor_total_hora_trabalhado(self):
        """@property: Calcula o valor total de horas trabalhos no dia."""
        for hora in self.mao_de_obra:
            valor_hora = hora.renda_mensal_hora_real * hora.mao_de_obra_horas_trabalhadas
            return round(valor_hora, 2)
    
    # Valor total dos minutos trabalhadas no projeto ( Usado para adicionar no orçamento)
    @property
    def orcamento_valor_total_minutos_trabalhado(self):
        """@property: Calcula o valor total de minutos trabalhos no dia."""
        for minutos in self.mao_de_obra:
            valor_minutos = minutos.mao_de_obra_minutos_trabalhados * minutos.renda_mensal_minuto_real
            return round(valor_minutos, 2)


if __name__ == "__main__":
    # instancia da classe orcamento
    pj = OrcamentoProjeto(1, "Orcamento1")

    # Cadastro de produtos 
    produto1 = pj.op_add_materiais(1, "tinta branca", 33.33, 90, "ml", 10) # Retorna True / False
    produto2 = pj.op_add_materiais(2, "tinta vermelha", 33.33, 90, "ml", 13)
    produto3 = pj.op_add_materiais(3, "tinta amarela", 33.33, 90, "ml", 20)
    produto4 = pj.op_add_materiais(4, "tinta preto", 33.33, 90, "ml", 7)
    produto5 = pj.op_add_materiais(5, "tinta azul", 33.33, 90, "ml", 5)

    # Listar os materiais cadastrados
    for material in pj.op_listar_materiais_cadastrados():
        print(material)

    # Listar o valor total do Estoque
    print(pj.op_valor_total_estoque)

    # retorna o valor total dos materiais usados.
    print(pj.op_valor_total_materiais_usados)
    
