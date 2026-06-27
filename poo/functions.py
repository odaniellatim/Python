from save_data import SaveDataFile
from materiais import Materiais

def handler_save_file(filename, foldername, data):
    save_data = SaveDataFile(foldername, filename)
    save_data.save_data(data)

def handler_load_file(filename, foldername):
    save_data = SaveDataFile(foldername, filename)
    return save_data.load_data(foldername, filename)


def handler_add_materiais(material_id: int,
                          material_nome: str, 
                          material_qntd: int, 
                          material_valor: float, 
                          material_padrao_medida: str) -> Materiais:
    """ Função que adiciona novos materiais"""
    mt = Materiais(material_id, material_nome, material_qntd, material_valor, material_padrao_medida)
    return mt