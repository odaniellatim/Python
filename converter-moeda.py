def moeda(state, gold):

    if (
        state == "BRL"
        or state == "EUA"
        or state == "ARG"
        or state == "EUR"
        or state == "CNY"
    ):
        state = state
        print("")
        print(f"O valor de {gold} {state}, convertido em REAL é: ")
    elif state == "":
        state = "EUA"
        print("")
        print(f"O valor de {gold} {state}, convertido em REAL é: ")
    else:
        print("")
        msg = "Digiete um pais valido!"
        return msg

    def converter(gold):
        if state == "BRL":
            result = int(gold) * 1
            moeadinha = f"R$ {round(result, 3)}"
            return moeadinha
        elif state == "EUA":
            result = int(gold) * 5.56
            moeadinha = f"R$ {round(result, 3)}"
            return moeadinha
        elif state == "ARG":
            result = int(gold) * 0.004
            moeadinha = f"R$ {round(result, 3)}"
            return moeadinha
        elif state == "EUR":
            result = int(gold) * 6.32
            moeadinha = f"R$ {round(result, 3)}"
            return moeadinha
        elif state == "CNY":
            result = int(gold) * 0.78
            moeadinha = f"0R$ {round(result, 3)}"
            return moeadinha
        else:
            print("Informe um pais valido.")

    return converter(gold)


while True:
    valor = input("Digite o valor para converter: ")
    print("")
    print("")

    moedas_disponivel = ["BRL", "EUA", "ARG", "EUR", "CNY"]

    print("Digite as Siglas para converter a moeda: ")
    for indice, moedas in enumerate(moedas_disponivel, 1):
        print(f"{indice} -> {moedas}")
    print("")

    pais = input("Digite o pais da moeda: ").upper()

    print(moeda(pais, int(valor)))

    print("")
    print("")

    sair = input("Digite [X] para sair ou [ENTER] para continuar: ")
    print("")
    if sair == "X" or sair == "x":
        break
