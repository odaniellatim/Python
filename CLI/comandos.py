def cm(parser):
    
    # Chave para passar valores por comando.
    parser.add_argument(
        "-n",
        "--nome",
        required=False,
        help="Nome do produto",
    )

    parser.add_argument(
        "-m",
        "--medida",
        choices=["g", "kg", "mg", "l", "unidade"],
        required=False,
        help="Unidade de medida disponiveis -> ['g','kg','mg','l', 'unidade']",
    )

    parser.add_argument(
        "-q",
        "--quantidade",
        type=int,
        required=False,
        help="Quantidade que vem no produto (5g, 1000kg, 1 Unidade)",
    )

    parser.add_argument(
        "-p",
        "--preco",
        type=float,
        required=False,
        help="Preço pago no produto Ex.:(00.00)",
    )

    parser.add_argument(
        "-add",
        "--adicionar",
        action="store_true",
        help="Para salvar os dados no arquivo json"
    )

    parser.add_argument(
        "-c",
        "--clear",
        action="store_true",
        help="Para limpar os dados do arquivo json",
    )

    parser.add_argument(
        '-l',
        "--listar",
        action="store_true",
        help="Opcao para listar os items salvos",
    )
