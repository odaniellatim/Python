import os
import collections

os.system("clear")

content = None
lista = []
invalidos = []

with open("bd.txt", "r") as f:
    content = f.read()

# Limpar os dados removendo espaços, emails invalidos e criando uma lista
content = content.lower()
content = content.replace(" ", "\n")
content = content.replace("\n", ",")
content = content.replace(";", ",")
content = content.split(",")

for item in content:
    if item:
        data = item.strip()
        if not data:
            continue
        else:
            if data.endswith("@"):
                invalidos.append(item.strip())
                continue
            if data.startswith("@"):
                invalidos.append(item.strip())
                continue
            if data.find("@") == -1:
                invalidos.append(item.strip())
                continue
            if data.count("@") > 1:
                invalidos.append(item.strip())
                continue
            if data.find(".com") < 1:
                invalidos.append(item.strip())
                continue
            lista.append(data)

# Remover os itens duplicados
itens_repetidos = collections.Counter(lista)
itens_unicos = set(lista)

duplicados = []
unicos = set()

for email in lista:
    if email in unicos:
        duplicados.append(email)
    else:
        unicos.add(email)

# Analisando a quantidade de emails por dominio
domain = []
for total in unicos:
    new_arr = total.split("@")
    new_arr = new_arr[1].split(".")
    domain.append(new_arr[0])

# Salvar os emails em um arquivo txt com um item por linha
with open("emails_limpos.txt", "w") as f:
    for email in unicos:
        f.write(f"{email}\n")

# Resultado dos filtros aplicados
print(f"Total de Emails validos - Total:({len(unicos)}) ")
print("-" * 50)
for email in unicos:
    print(f"\t{email}")
print("\n")

print(f"Total de emails por dominio - Total:({len(unicos)}) ")
print("-" * 50)
for count, dom in collections.Counter(domain).items():
    print(f"\t{count}\t {dom}")
print("\n")

print(f"Lista de itens duplicados - Total:({len(duplicados)}) ")
print("-" * 50)
for dup in duplicados:
    print(f"\t{dup}")
print("\n")

print(f"Lista de itens Invalidos - Total:({len(invalidos)}) ")
print("-" * 50)
for invalid in invalidos:
    print(f"\t{invalid}")

print("\n")
letras = "Python Sem Noção"
for py in letras:
    if ord(py) == 32:
        print("\n")
        continue
    letter = py
    print(letter.isascii(), end="\t")
    print(f"{ord(py)}\t{py}")
