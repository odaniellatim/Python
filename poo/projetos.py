import random   
from orcamento_projeto import OrcamentoProjeto
from rich import print

class Projetos:
    def __init__(self):
        self.orcamentos = []
        self.orcamento_materiais = []
        #self.projeto_id_ramdom = random.randint(0, 10000)

    def pj_adicionar_projeto(self,projeto_id: int, projeto_nome: str) -> str:
        #projeto_id = self.projeto_id_ramdom
        orcamento = OrcamentoProjeto(projeto_id, projeto_nome)
        self.orcamentos.append(orcamento)
        print(f"Orcamento {projeto_nome} Adicionado com sucesso!")

    def pj_listar_orcamentos(self):
        lista_projetos = []
        for orcamento in self.orcamentos:
            lista_projetos.append(orcamento.oc_nome_orcamento())
        return lista_projetos
    
    def pj_adicionar_materiais_projeto(self, 
            projeto_id,
            id_material,
            nome_material,
            valor_material,
            peso_material,
            unidade_medida_material):
            
        for orcamento in self.orcamentos:
            if orcamento.oc_id()  == projeto_id:
                item_add = orcamento.oc_adicionar_materiais(
                    #12, "preto", 15.90, 90, 'g')
                    id_material,
                    nome_material,
                    valor_material,
                    peso_material,
                    unidade_medida_material
                )
                return item_add
                
                
    # TODO: Continuar a seleção do item por id
    def pj_selecionar_materiais_projeto(self, material_id):
        for material in self.orcamentos:
            lista_mt = material.oc_listar_todos_materiais()
            
            if lista_mt[0]['id'] == material_id:
                select = material.oc_alterar_status(material_id)
                self.orcamento_materiais.append(select)
                return select
            
    
    def pj_listar_materiais_projetos(self, projeto_id: int ) -> list:
        for materiais in self.orcamentos:
            if materiais.oc_id() == projeto_id:
                return materiais.oc_listar_materiais_select()
        

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
            
    def pj_dicionario(self):
        for orcamento in self.orcamentos:
            projeto = orcamento.oc_nome_orcamento()        
            
            if projeto['orcamento_id']:
                return {
                    'projeto_id': projeto['orcamento_id'],
                    'projeto_nome': projeto['orcamento_nome'],
                    'projeto_materiais': self.orcamento_materiais,
                }


if __name__ == "__main__":
    projeto = Projetos()
    orcamento = projeto.pj_adicionar_projeto(1, "Teste")
    orcamento = projeto.pj_listar_orcamentos()
    
    add1 = projeto.pj_adicionar_materiais_projeto(1, 2, "preto", 15.90, 90, 'g')
    add2 = projeto.pj_adicionar_materiais_projeto(1, 3, "Branco", 15.90, 90, 'g')
    add3 = projeto.pj_adicionar_materiais_projeto(1, 4, "Azul", 15.90, 90, 'g')
    add4 = projeto.pj_adicionar_materiais_projeto(1, 5, "Rosa", 15.90, 90, 'g')
    
    select = projeto.pj_selecionar_materiais_projeto(2)
    select = projeto.pj_selecionar_materiais_projeto(3)
    print("select", select)
    
    lista_materiais = projeto.pj_listar_materiais_projetos(1)
    lista_materiais2 = projeto.pj_listar_materiais_projetos(5)
    
    dicionario = projeto.pj_dicionario()
    
    print(dicionario)
