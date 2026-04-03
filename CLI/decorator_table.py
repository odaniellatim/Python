def size_word(lista_dicionario: list) -> int:
    """
    Realiza a contagem de caracteres de uma lista com dicionarios 
    analisa cada palavra e retorna o numero maior com a quantidade de caracteres
    """
    word_size = 0
    for l in lista_dicionario:
        for key, value in l.items():
            if len(key) > word_size:
                word_size = len(key)

            if len(str(value)) > word_size:
                word_size = len(value)
    return word_size


def total_linhas(lista_dicionario: list):

    total_linhas = len(lista_dicionario)
    return total_linhas


def columns(lista_dicionario: list):
    colunas = 0
    for l in lista_dicionario:
        colunas = len(l)
    return colunas


def draw_lines(size_words: int, colunas: int, gap: int = 5):
    if gap > 5:
        gap = 5
    size_linha = (colunas * size_words) + gap
    return size_linha

# Decorador


def fn_table(fn_data):
    def dec(*args):

        size_words = args[1]
        colunas = args[2]
        linhas = args[3]
        gap = args[4]

        size_coluna = gap + size_words
        size_max_linha = (gap * colunas) + linhas

        print("Linhas", size_max_linha, end=" ")
        print("Colunas", size_coluna, end=" ")
        print("Size Palavras", args[1], end=" ")
        print("Gap: ", gap, end=" ")
        print("")

        header_name_colunas = []

        # Cadastra os nomes das colunas em uma lista nova
        for l in args[0]:
            header_name_colunas.extend(l.keys())

        # Remove os itens repetidos da lista
        header_name_colunas = dict.fromkeys(header_name_colunas)

        # Preencha as colunas com os cabeçalhos e as divisorias
        print("-" * size_max_linha)

        s_coluna = 1
        for header in header_name_colunas:
            if s_coluna <= 1:
                print(f"|{str(header).center(size_coluna, " ")}", end="|")
                s_coluna += 1

            elif (s_coluna > 1 and s_coluna <= colunas-1):
                print(f"{header.center(size_coluna, " ")}", end="|")
                # print(f"{s_coluna} {colunas}")
                s_coluna += 1
            else:
                print(f"{header.center(size_coluna, " ")}|")

        print("-" * size_max_linha)

        # Preencha as linhas com os textos e as divisorias

        for l in args[0]:
            count_linha = 1
            for value in l.values():
                str_value = str(value)

                if count_linha <= 1:
                    print(f"|{str_value.center(size_coluna, " ")}", end="|")
                    count_linha += 1
                elif (count_linha > 1 and count_linha <= colunas - 1):
                    print(f"{str_value.center(size_coluna, " ")}", end="|")
                    count_linha += 1
                else:
                    print(f"{str_value.center(size_coluna, " ")}|")

            print("-" * size_max_linha)

    return dec


@fn_table
def fn_data(objeto: list, size_word: int, colunas: int, draw_lines: int):
    return f"Item formatado em formato de tabela"


if __name__ == "__main__":

    dt = [
        {
            "nome_produto": "Banana",
            "medida": "kg",
            "quantidade": 350,
            "valor": 17.50
        },
        {
            "nome_produto": "Morango",
            "medida": "g",
            "quantidade": 650,
            "valor": 15.50
        },
        {
            "nome_produto": "Melancia",
            "medida": "unidade",
            "quantidade": 1,
            "valor": 24.50
        },
    ]

    word = size_word(dt)
    coluna = columns(dt)
    gap = 10
    draw_lines = draw_lines(word, coluna, gap)
    space = 5
    fn_data(dt, word, coluna, draw_lines, space)
