
import fn
import fmt
from src.custo_fixo.custo_fixo import Custo_Fixo
from src.banco_dados.banco_de_dados import Banco_de_dados
# import comandos
# from src.lista_de_materiais import constroi_objeto


def load_data(data_json: list):
    """
    Instancia os dados do arquivo Json usando a classe Custo Fixo.
    facilitando a edição dos dados.
    """
    cx = []

    for data in data_json:
        cx1 = Custo_Fixo(
            data["custo_fixo_id"],
            data["custo_fixo_nome"],
            data["custo_fixo_valor"],
            data["custo_fixo_status"],
            data["custo_fixo_numero_vendas"],
            data["custo_fixo_durabilidade_meses"],
            226.67
        )
        cx.append(cx1.get_dict())
    return cx


if __name__ == "__main__":

    # Banco de dados Custo Fixo
    data = Banco_de_dados("teste_custo_fixo.json", "bd")
    data_json = data.bd_load_data()

    # Carrega os dados do arquivo json, usando a classe Custo Fixo.
    custo_fixo = load_data(data_json)
    print("-" * 60)

    # Filtra o lista de items pelo status de PAGO/PENDENTE
    id = "pendente"
    i = []
    for item in custo_fixo:
        for key, value in item.items():
            if key == "custo_fixo_status" and value == id:
                i.append(item)

    print("Total de Itens encontrados: ", len(i))
    for s in i:
        print("-" * 70)
        for status in s.items():

            print(status)
    print("-" * 60)
    # parser = fn.run()
    # file_name = "db.json"

    # # Executa a lista de comandos
    # comandos.cm(parser)
    # args = parser.parse_args()

    # item = constroi_objeto(args.nome, args.medida, args.quantidade,
    #                        args.preco, args.status)
    # fmt.draw_table(len(item[0]), item)

    # # Listar items no terminal
    # if (args.listar):
    #     items = fn.listar_items(file_name)
    #     fn.f_obj(items)

    # if (args.adicionar):
    #     p = fn.item(args.nome, args.medida, args.quantidade, args.preco)
    #     i = fn.listar_items(file_name)
    #     i.append(p)
    #     di = fn.save(i, file_name)

    # if (args.clear):
    #     fn.save([], file_name)
