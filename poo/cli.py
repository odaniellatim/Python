import argparse
from rich import print

from projetos import Projetos
from functions import handler_add_materiais, handler_load_file, handler_save_file, handler_remove_material, handler_add_orcamento, handler_add_material_orcamento


def argumentos(parser):
    subparsers = parser.add_subparsers(
        dest="comando", required=True, help="Comandos disponiveis"
    )

    """ 
    ************************************************************************************************

    COMANDOS RELACIONADO AO CADASTRO DE MATERIAIS 

    ************************************************************************************************
    """

    subparsers.add_parser("list-material", aliases=["mt-list"], help="Listar todos os materiais")

    # Subcomando 'add' (Requer os dados do produto como argumentos posicionais)
    parser_add_mt = subparsers.add_parser("add-material", help="Adicionar um novo material")

    # Argumentos posicionais do comando 'add' (A ordem importa!)
    parser_add_mt.add_argument("nome", type=str, help="Nome do produto")
    parser_add_mt.add_argument("preco", type=float, help="Preço do produto")
    parser_add_mt.add_argument("qntd", type=int, help="Quantidade do produto")
    parser_add_mt.add_argument(
        "medida", choices=['g', 'ml', 'l', 'cm'], type=str, help="Padrão de medida (g, ml, litros, etc.)"
    )
    
    parser_del_material = subparsers.add_parser("del-material", help="Deletar um material por ID")
    parser_del_material.add_argument("id", type=str, help="informe o ID do material a ser deletado")


    """ 
    ************************************************************************************************

    COMANDOS RELACIONADO AO CADASTRO DE ORCAMENTOS
    
    ************************************************************************************************
    """

    subparsers.add_parser("list-orcamentos", aliases=["oc-list"], help="Listar todos os orcamentos")

    parser_add_oc = subparsers.add_parser('add-orcamento', help="Adicionar novo orçamento")
    parser_add_oc.add_argument("nome", type=str, help="Titulo do orcamento")

    parser_add_mt_oc = subparsers.add_parser("add-material-oc", help="Adicionar material em um orcamento")
    parser_add_mt_oc.add_argument("id", type=int, help="ID do orcamento que vai receber o material")
    parser_add_mt_oc.add_argument("material_id", nargs='+', type=int, help="ID do material selecionado")



def opcao_selecionada(opt, projeto: Projetos, lt_materiais: list, lt_orcamentos: list, filename: dict, foldername: dict):

    match opt.comando:
        case "list-material" | "mt-list":
            materiais = projeto.pj_listar_materiais_cadatrados()
            print(materiais)

        case "add-material":

            obj = handler_add_materiais(len(lt_materiais), opt.nome, opt.qntd, opt.preco, opt.medida)
            lt_materiais.append(obj)
            obj_save = []
            for m in lt_materiais:
                obj_save.append(m.mt_listar_detalhes_materiais())
            handler_save_file(filename['file_materiais'], foldername['folder_materiais'], obj_save)
        
        case "del-material":
            # Deletando um material da lista de materiais
            lista_atualizada = handler_remove_material(projeto, opt.id)
            handler_save_file(filename['file_materiais'], foldername['folder_materiais'], lista_atualizada)
            return f"Material com ID {opt.id} deletado com sucesso."

        case "list-orcamentos" | "oc-list":
            orcamento = projeto.pj_listar_orcamentos()
            print(orcamento)

        case "add-orcamento":
            obj_oc = handler_add_orcamento(len(lt_orcamentos), opt.nome)
            lt_orcamentos.append(obj_oc)

            obj_oc_save = []
            for o in lt_orcamentos:
                obj_oc_save.append(o.oc_listar_detalhes_orcamento())
            handler_save_file(filename['file_orcamentos'], foldername['folder_orcamentos'], obj_oc_save)

        case "add-material-oc":
            oc_update = handler_add_material_orcamento(projeto, lt_materiais, opt.id, opt.material_id)
            handler_save_file(filename['file_orcamentos'], foldername['folder_orcamentos'], oc_update)

        case _:
            print("Use --help para ajuda")


if __name__ == "__main__":

    # Load data dos arquivos 
    folder_names = {
        'folder_materiais': 'materiais',
        'folder_orcamentos': 'orcamentos'
    }

    files_names = {
        'file_materiais': 'materiais.json',
        'file_orcamentos': 'orcamentos.json',
    }
 
 
    # Variaveis globais que armazenara os dados relevantes do programa
    lt_orcamentos: list = handler_load_file(files_names['file_orcamentos'], folder_names["folder_orcamentos"])
    lt_materiais: list = handler_load_file(files_names['file_materiais'], folder_names['folder_materiais'])

    
    
    projeto = Projetos(lt_orcamentos, lt_materiais)

    parser = argparse.ArgumentParser(description="Gerenciador de Orçamentos Projetos")
    
    argumentos(parser)
    
    args = parser.parse_args()

    opcao_selecionada(args, projeto, lt_materiais, lt_orcamentos, files_names, folder_names)