
def colunas(objeto: list) -> int:
    total_letras = 0
    for col in objeto: # Lista os dicionarios
        for palavra in col.keys():
            if (len(palavra) > total_letras):
                total_letras = len(palavra)
    return total_letras


def linhas(objeto: list) -> int:
    total_letras = 0
    for linha in objeto:
        for palavra in linha.values():
            if (len(str(palavra)) > total_letras):
                total_letras = len(palavra)
    return total_letras

def draw_table(n_colunas: int, objeto: list) -> None:

    total_colunas = 0
    n_colunas = n_colunas + 1
    titulo_coluna = []
    total_linhas = 0
    
    col = colunas(objeto)
    lin = linhas(objeto)
    total_items_obj = len(objeto) + 1

    if (total_items_obj <= 0):
        print("Nenhum item cadastrado.")
        exit()
    
    # Verifica quem tem o maior numero de caracteres
    if(col > lin):
        caracteres  = col + 5
    else:
        caracteres = lin + 5

    # Defini a quantidade de caracteres para dividir as linhas
    divisoria = ((n_colunas - 1) * caracteres + 5)
     
    # Adicionar os nomes das colunas em uma lista
    for titulo in objeto:
        for t in titulo.keys():
            if (t not in titulo_coluna):
                titulo_coluna.append(t)

    # Controi as colunas com os titulos da tabela
    print("—" *  divisoria)
    for linha in range(n_colunas):
        total_colunas += 1
        
        if(total_colunas >= n_colunas):
            print("|")
        else:
            title = titulo_coluna
            print(f"|{title[(total_colunas-1)].center(caracteres, " ").title()}", end="")
    print("—" * divisoria)

    # Controi as linhas com os conteudos da tabela.
    for item in objeto:
        total_linhas += 1

        if (total_linhas >= total_items_obj):
            print("|", end="|")            
        else:
            item_value = list(item.values())
            for value in item_value:
                
                if isinstance(value, float):
                    valor = f"R$ {str(value)}"
                    print(f"|{valor.center(caracteres, " ").title()}", end="")
                else:
                    print(f"|{str(value).center(caracteres, " ").title()}", end="")
            print("", end="|")
            print("")
            print("—" * divisoria)


def tabela_horizontal(numero_colunas, lista_objeto):
    # Falta construir a tabela com o um codigo mais otimizado.
    pass

def tabela_vertical(numero_colunas: int, lista_objeto: list):

    caracteres_colunas = colunas(lista_objeto) # Pega o numero maior de caracteres das chaves
    caracteres_linhas = linhas(lista_objeto) # Paga o numero maior de caracteres dos valores
    caracteres = 0
    
    # Define o numero maximo de caracteres para expandir as colunas
    if (caracteres_colunas > caracteres_linhas):
        caracteres = caracteres_colunas + 3
    else:
        caracteres = caracteres_linhas + 3
    
    # Reeconstruindo novo objeto
    table_lista = []
    obj_titulos = {}
    
    for chave in lista_objeto[0].keys():
        obj_titulos[chave] = []

    for item in lista_objeto:        
        for key in item.keys():
            obj_titulos[key].append(item[key])
    
    table_lista.append(obj_titulos)

    # Colocando os dados em uma tabela formatada.
    contador = 0
    separador = numero_colunas * caracteres + 2

    for itens in table_lista:        
        for titulo, desc in itens.items():            
            print("-" * separador)
            print(f"|{titulo.center(caracteres, " ").title()}", end="|") 
            for content in desc:
                contador += 1                
                if not((contador % (numero_colunas - 1)) == 0):
                    print(f"{str(content).center(caracteres, " ").title()}", end="|")
                else:
                    print(f"{str(content).center(caracteres - 2, " ").title()}|") 
        print("-" * separador)
        

if __name__ == "__main__":
    lista = [
    {
        "nome": "Banana",
        "medida": "Kg",
        "quantidade": 1,
        "preco": 12.5,
    },
        {
            "nome": "Abacaxi Violeta",
            "medida": "Kg",
            "quantidade": 2,
            "preco": 13.5,
        },
        {
            "nome": "Morango",
            "medida": "g",
            "quantidade": 350,
            "preco": 15.5,
        },{
            "nome": "Morango",
            "medida": "g",
            "quantidade": 350,
            "preco": 15.5,
        },{
            "nome": "Morango",
            "medida": "g",
            "quantidade": 350,
            "preco": 15.5,
        },{
            "nome": "Morango",
            "medida": "g",
            "quantidade": 350,
            "preco": 15.5,
        },{
            "nome": "Morango",
            "medida": "g",
            "quantidade": 350,
            "preco": 15.5,
        },{
            "nome": "Morango",
            "medida": "g",
            "quantidade": 350,
            "preco": 15.5,
        },
    ]

    total_itens = len(lista) + 1
    print(total_itens)
    # tabela_horizontal(4, lista)
    tabela_vertical(total_itens, lista)
