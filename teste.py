# Nome com While

# nome = 'Daniel Latim'
# tamanho_nome = len(nome)

# start = 0
# finish = 1
# novo_nome = ''

# while start <= tamanho_nome:
#     if start == tamanho_nome:
#       break
#     novo_nome += f'*{nome[start]}'
#     start += 1


# print(novo_nome)

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

indices = range(len(lista))
for indice in indices:
    print(f"{indice} - {lista[indice]}")
