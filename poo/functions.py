from save_data import SaveDataFile
from materiais import Materiais
from orcamento_projeto import OrcamentoProjeto
from projetos import Projetos

def handler_save_file(filename, foldername, data):
    '''Salvar os dados em um arquivo json'''
    save_data = SaveDataFile(foldername, filename)
    save_data.save_data(data)
    

def handler_load_file(filename: str, foldername: str):
    ''' Analisa os arquivos com os dados e carrega para a variavel global do programa'''

    file = SaveDataFile(foldername, filename)

    folder_exist = file.folder_exist()
    if not folder_exist:
        file.save_data([])

    save_data = file.load_data(foldername, filename)

    match foldername:
        case 'orcamentos':
            lista_orcamento_atualizada = []

            if len(save_data) == 0:
                return []
            
            for orcamento in save_data:               
                obj = OrcamentoProjeto(
                    orcamento['orcamento_id'], 
                    orcamento['orcamento_nome'],
                )

                lista_orcamento_atualizada.append(obj)

            return lista_orcamento_atualizada

        case 'materiais':
            lista_materiais_atualizada = []
            
            if len(save_data) == 0:
                return []
            
            for material in save_data:
                obj = Materiais(
                    material['mt_id'], 
                    material['mt_nome'], 
                    material['mt_valor'], 
                    material['mt_quantidade'], 
                    material['mt_padrao_medida']
                    )
                lista_materiais_atualizada.append(obj)

            return lista_materiais_atualizada
        case _:
            return []
    return []

# Funções de controle dos dados referente aos materiais
def handler_add_materiais(
        material_id: int,
        material_nome: str,
        material_qntd: int,
        material_valor: float,
        material_padrao_medida: str) -> Materiais:
    """ Função que adiciona novos materiais"""

    mt = Materiais(material_id, material_nome, material_qntd, material_valor, material_padrao_medida)
    return mt

def handler_remove_material(projeto: Projetos, material_id: int):
    '''Deletar um material cadastrado por ID'''
    lista = projeto.pj_deletar_material(material_id)
    return lista


# Funções de controle dos dados referente aos Orcamentos

def handler_add_orcamento(orcamento_id, orcamento_nome):
    oc = OrcamentoProjeto(orcamento_id, orcamento_nome)
    return oc

def handler_add_material_orcamento(
        projeto: Projetos, 
        lista_materiais: list[Materiais], 
        id_orcamento: int, 
        id_material: list):

    lista_materiais_selecionados = []

    for material in lista_materiais:
        for id_items in id_material:
            if material.material_id == id_items:
                lista_materiais_selecionados.append(material)
                break

    projeto.pj_adicionar_material_orcamento(id_orcamento, lista_materiais_selecionados)
    oc_update = projeto.pj_listar_orcamentos()
    return oc_update