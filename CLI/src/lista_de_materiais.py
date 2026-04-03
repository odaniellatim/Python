import fmt


def constroi_objeto(lista_items: list):
    # Função que gerar os dados organizados em um dicionario
    # Antes de printar os dados é importante verificar se não existe um arquivo
    # Se existir carregar os dados para mostrar na tela.
    print("Modulo Lista de Materiais")

    if (len(lista_items) <= 0):
        raise TypeError("Nenhum item cadastrado")
    lista = []
    for item in lista_items:
        lista.append({
            "nome": item["nome"],
            "medida": item["medida"],
            "qntd": item["qntd"],
            "qntd_usado": item["qntd_usado"],
            "qntd_usado_medida": item["qntd_usado_medida"],
            "preco": item["preco"],
            "status": item["status"]
        })
    return lista


if __name__ == "__main__":

    lista = [
        {
            "nome": "Banana",
            "medida": "kg",
            "qntd": 1.5,
            "qntd_usado": 800,
            "qntd_usado_medida": "g",
            "preco": 7.99,
            "status": False
        },
        {
            "nome": "Maça",
            "medida": "kg",
            "qntd": 1.2,
            "qntd_usado": 350,
            "qntd_usado_medida": "g",
            "preco": 10.00,
            "status": True
        },
        {
            "nome": "Farinha",
            "medida": "g",
            "qntd": 900,
            "qntd_usado": 350,
            "qntd_usado_medida": "g",
            "preco": 9.59,
            "status": True
        },
        {
            "nome": "Leite",
            "medida": "ml",
            "qntd": 1000,
            "qntd_usado": 350,
            "qntd_usado_medida": "ml",
            "preco": 6.99,
            "status": True
        },
    ]

    lista = constroi_objeto(lista)
    fmt.draw_table(len(lista[0]), lista, space=3)
