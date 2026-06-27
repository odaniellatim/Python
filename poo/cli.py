import argparse

from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from save_data import SaveDataFile
from projetos import Projetos
from orcamento_projeto import OrcamentoProjeto
from materiais import Materiais
from functions import handler_add_materiais, handler_load_file, handler_save_file


def argumentos(parser):
    subparsers = parser.add_subparsers(
        dest="comando", required=True, help="Comandos disponiveis"
    )

    subparsers.add_parser("list", aliases=["lp"], help="Listar todos os materiais")

    # Subcomando 'add' (Requer os dados do produto como argumentos posicionais)
    parser_add = subparsers.add_parser("add", help="Adicionar um novo material")

    # Argumentos posicionais do comando 'add' (A ordem importa!)
    parser_add.add_argument("nome", type=str, help="Nome do produto")
    parser_add.add_argument("preco", type=float, help="Preço do produto")
    parser_add.add_argument("qntd", type=int, help="Quantidade do produto")
    parser_add.add_argument(
        "medida", type=str, help="Padrão de medida (g, ml, litros, etc.)"
    )

    # Subcomando para carregar dados do arquivo (banco de dados)
    parser_load = subparsers.add_parser("load", help="Carregar dados do arquivo json")


def opcao_selecionada(opt, lista_materiais, filename, foldername):


    match opt.comando:
        case "list" | "lp":
            data = handler_load_file(filename, foldername)
            return data

        case "add":
            
            obj = handler_add_materiais(1, opt.nome, opt.qntd, opt.preco, opt.medida)
            lista_materiais.append(obj.mt_listar_detalhes_materiais())
            handler_save_file(filename, foldername, lista_materiais)
        
        case "load":
            # Carregar Lista materiais
            # Carregar Lista Projetos
            # Carregar Lista orcamentos
            pass

        case _:
            print("Use --help para ajuda")


if __name__ == "__main__":

    # Load data dos arquivos 
    foldername = "materiais"
    filename = "materiais.json"
    data_file = handler_load_file(filename, foldername)
    
    # Variaveis globais que armazenara os dados relevantes do programa
    lista_orcamentos = []
    lista_materiais = data_file if len(data_file) > 0 else []
    
    projeto = Projetos(lista_orcamentos, lista_materiais)

    parser = argparse.ArgumentParser(description="Gerenciador de Orçamentos Projetos")
    
    argumentos(parser)
    
    args = parser.parse_args()
    result_opt = opcao_selecionada(args, lista_materiais, filename, foldername)

    # Resultado da opcao selecionada
    print(result_opt)