def cadastro_custo_fixo():
    lista = []
    while True:

        def_cadastro = atualiza_custo_fixo()

        if def_cadastro is None:
            break
        else:
            lista.append(def_cadastro)
            valor_total_itens(lista)


def atualiza_custo_fixo():

    while True:
        input_nome = input("Digite o nome do item: ")
        if input_nome == "x" or input_nome == "X":
            break

        input_valor = input("Digite o valor do item: ")
        input_validade = input("Qual a validade do produto em meses: ")

        novo_item = [input_nome, float(input_valor), int(input_validade)]

        return novo_item


def valor_total_itens(lista_itens):
    # print(lista_itens)
    itens_novos = 0
    valide = 0
    print()  # separador

    for itens in lista_itens:
        print(f"-> Item: {itens[0]} - Valor: {itens[1]} - Validede: {itens[2]}")
        itens_novos += itens[1]
        valide += itens[2]

    print("-" * 70)
    print(f"Total: R$ {itens_novos} - Validade Total: {valide}")
    print()


if __name__ == "__main__":

    # print()
    # print("-" * 70)

    cadastro_custo_fixo()
