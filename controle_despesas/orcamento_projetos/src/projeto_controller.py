from src.orcamento_projeto import OrcamentoProjeto
from src.unidades_medida import UnidadeMedida

class ProjetoController:
    def __init__(self):
        self.orcamento_projeto: list[OrcamentoProjeto] = []

    # Cadastro de orçamentos
    def pc_add_orcamento(self, id, orcamento_nome)-> None | bool:
        add_orcamento = OrcamentoProjeto(id, orcamento_nome)
        self.orcamento_projeto.append(add_orcamento)
        return True

    # TODO: Cadastrar materiais
    def pc_cadastrar_materiais(self, id: int, nome: str, valor: float, quantidade: int, unidade_medida: UnidadeMedida, qntd_material_usado_pj: int)-> bool:
        for pj in self.orcamento_projeto:
           pj.op_add_materiais(id, nome, valor, quantidade, unidade_medida, qntd_material_usado_pj)
        
        
    # TODO: Listar materiais cadastrados
    def pc_listar_materiais_cadastrados(self)-> dict:
        
        itens = []
        for oc in self.orcamento_projeto:
            it = oc.op_listar_materiais_cadastrados() 
            itens.extend(it)
        return itens


if __name__ == "__main__":
    # instancia do projeto controller
    pj = ProjetoController()

    # cadastro do orçamento (projeto)
    oc = pj.pc_add_orcamento(1, "tenis mickey")

    # produtos usados no projeto/orcamento
    mt1 = pj.pc_cadastrar_materiais(1, "tinta branca", 33.33, 90, "ml", 8)
    mt2 = pj.pc_cadastrar_materiais(2, "tinta vermelha", 33.33, 90, "ml", 15)
    mt3 = pj.pc_cadastrar_materiais(3, "tinta amarela", 33.33, 90, "ml", 17)

    # Lista de produtos cadastrados no projeto/orcamento
    print(pj.pc_listar_materiais_cadastrados())
          
    if(mt1):
        print("Produto Cadastrado com sucesso")
    else:
        print("Erro ao cadastrar produto")
        print(mt1)
