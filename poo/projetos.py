import random
from orcamento_projeto import OrcamentoProjeto


class Projetos:
    def __init__(self):
        self.orcamentos = []

    def pj_adicionar_projeto(self, projeto_nome):
        projeto_id = random.randint(0, 10000)
        orcamento = OrcamentoProjeto(projeto_id, projeto_nome)
        self.orcamentos.append(orcamento)
        print(f"Orcamento {projeto_nome} Adicionado com sucesso!")

    def pj_listar_orcamentos(self): ...
