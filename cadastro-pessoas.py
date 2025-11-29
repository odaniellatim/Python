import json
from pathlib import Path
import os

menu_ativo = True
json_path = Path("texte.json")
cadastros = []    

def criar_file():
    os.system('clear')
    with open ("texte.json", "w") as arquivo:
        json.dump(cadastros, arquivo, indent=4)
        print("Arquivo gravado com sucesso!")
        
        

def get_items():
    os.system('clear')
    if json_path.is_file():    
        with open("texte.json", "r") as arquivo:
            data = arquivo.read()
            decode_json = json.loads(data)
            
            for indice in decode_json:            
                for key, item in indice.items(): 
                    print(f"{key.title()}: {item}")
                print(" " * 30) 
                print("- " * 30) 
                print(" " * 30) 
    else:
        criar_file()
        get_items()

def cadastrar():  
    os.system('clear')
    
    print(" " * 30) 
    print("- " * 30) 
    print(" " * 30) 
    
    id = len(cadastros) + 1
    if id <= 0:
        get_items()
        print("Dados Atualizados... Pronto para cadastrar novo item.")
        print(" " * 30) 
        print("- " * 30) 
        print(" " * 30) 
        
    
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    
    dicionario = {
            "id": id,  
            "nome": nome, 
            "idade": idade
        }
    
    cadastros.append(dicionario)
    
    with open("texte.json", "w") as arquivo:
        json.dump(cadastros, arquivo, indent=4)


def menu():
    
    opcoes = ["Cadastrar", "Listar", "Sair"]
    
    for number, opcao in enumerate(opcoes):
        print(f"{number}. {opcao}")
        

def item_selecionado(item_selecionado):
    match(item_selecionado):
        case 0 | "Cadastrar":
            cadastrar()
        case 1 | "Listar":
            get_items()
        


# if json_path.is_file():
    # get_items()
# else:
    # criar_file()

# get_items()
# for cadastro in cadastros:
#     print(cadastro)
 
# Cria um menu para o usuario selecionar um dos items.


while menu_ativo:
    menu()
    print(" " * 30) 
    print("- " * 30) 
    print(" " * 30) 
    opcao = int(input("Selecione uma das opções do menu: "))
    item_selecionado(opcao)
    
    if opcao == 2 or opcao == "sair":
        print("Finalizado com sucesso!")
        break