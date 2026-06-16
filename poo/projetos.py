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

    def pj_listar_orcamentos(self):
        lista_projetos = []
        print(self.orcamentos)
        # for orcamento in self.orcamentos:
            # lista_projetos.append(orcamento.oc_nome_orcamento())
        # return lista_projetos
        
    def pj_listar_materiais_projetos(self):
        # oc_listar_materiais
        for materiais in self.orcamentos:
            print(materiais.oc_listar_materiais())

    def load_file_materiais(self, bd: Save_in_file, folder, filename):
        data = bd.load_data(folder, filename)
        for orcamento in data:
            projeto = OrcamentoProjeto(
                orcamento["orcamento_id"], orcamento["orcamento_nome"]
            )
            for materiais in orcamento["orcamento_materiais"]:
                projeto.oc_adicionar_materiais(
                    materiais["id"],
                    materiais["nome"],
                    materiais["valor"],
                    materiais["quantidade"],
                    materiais["unidade_medida"],
                )
                self.orcamentos.append(projeto)
            return self.orcamentos
