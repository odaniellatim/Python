import argparse
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from orcamento_projeto import OrcamentoProjeto
from save_data import SaveDataFile
from projetos import Projetos


def start():
    # Variaveis globais que armazenara os dados relevantes do programa
    lista_orcamentos = []
    lista_materiais = []
    
    projeto = Projetos(lista_orcamentos, lista_materiais)

    parser = argparse.ArgumentParser(description="Gerenciador de Orçamentos Projetos")
    argumentos(parser)
    args = parser.parse_args()
    return opcao_selecionada(args, projeto)


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


def opcao_selecionada(opt, projeto: Projetos):

    foldername = "materiais"
    filename = "materiais.json"

    console = Console()
    table = Table(show_lines=True)
    db = SaveDataFile(foldername, filename)

    match opt.comando:
        case "list" | "lp":
            pass

        case "add":
            pass
        
        case "load":
            pass

        case _:
            print("Use --help para ajuda")


if __name__ == "__main__":
    teste = start()