from .materiais import Materiais
from .renda_mensal_base import RendaMensalBase
from .mao_de_obra import MaoDeObra

class OrcamentoProjeto:
    def __init__(self,orcamento_id,orcamento_nome) -> None:
        self.orcamento_id = orcamento_id
        self.orcamento_nome = orcamento_nome
        self.itens_materiais: list[Materiais] = []
        self.mao_de_obra: list[MaoDeObra] = []

    # cadastro de materais para realizar o orçamento do projeto
    def add_itens_materiais(self, 
                            id, 
                            nome, 
                            valor, 
                            quantidade, 
                            unidade_medida, 
                            qntd_usado_projeto
                            ):
  
        """ Cadastro de novos materiais para utilizar no projeto. """
        add_materiais = Materiais(id, nome, valor, quantidade, unidade_medida, qntd_usado_projeto)
        self.itens_materiais.append(add_materiais)
    
    # Valor total pago nos materiais para ter no estoque. (Valor estoque)
    @property
    def material_valor_total_produtos(self):
        """@property: Lista o valor total pago nos produtos cadastrados. """
        valor_total = 0
        for item in self.itens_materiais:
            valor_total += item.material_valor
        return valor_total
    
    # O valor total dos produtos usados no projeto
    @property
    def material_valor_total_produtos_usados(self):
        """@property: Lista todos os materiais que estão vinculados ao projeto. """
        valor_total_usados = 0
        if(len(self.itens_materiais) > 0):
           
            for item in self.itens_materiais:            
                item.material_lista_cadastrados()
                valor_total_usados += item.material_valor_total_qntd_usado_projeto()
            print("-" * 100)
            print(f"Valor total da quantidade usada no projeto: R$ {valor_total_usados:.2f}")
            print(f"Valor total dos produtos: R$ {self.material_valor_total_produtos:.2f}")
            print("-" * 100)
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
