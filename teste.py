"""
Página de teste de codigos Python
"""

import os

lista = ["Maria", "Helena", "Luiz"]


def cadastro():
    os.system('clear')
    print(" " * 50)
    nome = input("Informe seu nome: \n")
    lista.append(nome)

def apagar(item):
    os.system('clear')
    print(" " * 50)

    item_removido = lista.pop(int(item))
    print(f"{item_removido.upper()} foi removido com sucesso ")
    return item_removido
 
def listarItens():
    os.system('clear')

    print(" " * 50)
    indices = range(len(lista))

    print("")
    print("-------- Itens Cadastrados ------------ ")
    print("")

    for indice in indices:        
        print(f"{indice} - {lista[indice]}")
        
    print(" " * 50)

# Menu do programa
def menu():
    
    print("")
    print("-------- BEM VINDO ------------ ")
    print("")

    print("Selecione uma opção abaixo:")
    print("")

    print("1. Cadastrar")
    print("2. Listar Items")
    print("3. Apagar Item")
    print("4. Sair")

    print("")
    print("")

# FrontEnd programa

while True:

    menu()
    opcao = int(input("Digite a opção desejada: \n -> "))

    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listarItens()
    elif opcao == 3:
        listarItens()
        item = input("Informe o nome do item que vai ser apagado: \n -> ")
        apagar(item)
    elif opcao == 4:
        os.system('clear')
        listarItens()
        break

    
    
print(" " * 50)
