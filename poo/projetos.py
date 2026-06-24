import random
from orcamento_projeto import OrcamentoProjeto
from materiais import Materiais
from rich import print


class Projetos:
    def __init__(self, orcamentos: list[OrcamentoProjeto], materiais: list[Materiais]):
        self.projeto_lista_orcamentos: list[OrcamentoProjeto] = orcamentos
        self.projeto_lista_materiais: list[Materiais] = materiais

        #self.projeto_id_ramdom = random.randint(0, 10000)

    """
        MÉTODOS REFERENTE A CLASSE ORCAMENTO
        Esses métodos depende da classe orcamento para ter o funcionamento correto
    """
    def pj_listar_orcamentos(self):
        lista_orcamentos = []
        for orcamento in self.projeto_lista_orcamentos:
            lista_orcamentos.append(orcamento.oc_listar_detalhes_orcamento())
        return lista_orcamentos
    
    def pj_adicionar_material_orcamento(self, oc_id: int, lista_objetos_modificados: list[Materiais]) -> None:
        for orcamento in self.projeto_lista_orcamentos:
            if orcamento.orcamento_id == oc_id:
                for add_material in lista_objetos_modificados:
                    orcamento.oc_selecionar_materiais(add_material)

    
    """
        MÉTODOS REFERENTE A CLASSE MATERIAIS
        Esses métodos depende da classe materiais para ter o funcionamento correto
    """
    def pj_listar_materiais_cadatrados(self):
        lista_material = []
        
        for material in self.projeto_lista_materiais:
            lista_material.append(material.mt_listar_detalhes_materiais())

        if len(lista_material) <= 0:
            return False
        return lista_material
