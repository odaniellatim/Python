import argparse
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from orcamento_projeto import OrcamentoProjeto
from Save_in_file import Save_in_file
from projetos import Projetos


def start():
    projeto = Projetos()

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
        "medida", type=str, help="Unidade de medida (g, ml, litros, etc.)"
    )

    # Subcomando para carregar dados do arquivo (banco de dados)
    parser_load = subparsers.add_parser("load", help="Carregar dados do arquivo json")


def opcao_selecionada(opt, projeto: Projetos):

    foldername = "materiais"
    filename = "materiais.json"

    console = Console()
    table = Table(show_lines=True)
    db = Save_in_file(foldername, filename)

    match opt.comando:
        case "list" | "lp":
            fileload = projeto.load_file_materiais(db, foldername, filename)
            pj = projeto.pj_listar_orcamentos()
            print(pj)
            projeto.pj_listar_materiais_projetos()

        case "add":
            id_m = len(orcamento.oc_listar_materiais())
            orcamento.oc_adicionar_materiais(
                id_m, opt.nome, opt.preco, opt.qntd, opt.medida
            )
            return orcamento.oc_listar_materiais()
        case "load":
            projeto.load_file_materiais()
        case _:
            print("Use --help para ajuda")


if __name__ == "__main__":
    teste = start()
    teste
