import fn
import comandos

if __name__ == "__main__":
    parser = fn.run()
    file_name = "db.json"

    # Executa a lista de comandos
    comandos.cm(parser)

    args = parser.parse_args()

    # Listar items no terminal
    if (args.listar):
        items = fn.listar_items(file_name)
        fn.f_obj(items)

    if (args.adicionar):
        p = fn.item(args.nome, args.medida, args.quantidade, args.preco)
        i = fn.listar_items(file_name)
        i.append(p)
        di = fn.save(i, file_name)

    if (args.clear):
        fn.save([], file_name)

    # fn.preview(args.nome, args.medida, args.quantidade, args.preco)
