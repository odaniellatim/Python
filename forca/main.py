import os
from rich import print
from rich.padding import Padding
from functions import (
    load_word,
    pergunta_letra,
    letras_digitos,
    total_tentativas,
    selecionar_palavra,
    verificar_caracter_existe,
    enviar_palavra_completa,
    win,
)

# Limpar o terminal para nao ficar com muitas informações na tela.
os.system("clear")


# Letras que o usuario informou anteriormente.
letras = []
logs = []
# Armazena a lista de palavras do arquivo.
word = load_word()

# Armazena a palavra escolhida para a rodada
select_word = selecionar_palavra(word)

# Verifica o numero de caracteres que tem a palavra da rodada
total_char_palavra = len(select_word)

# Cria uma mascara para apresentar para o usuario
mask_palavra_selecionada = ["_"] * total_char_palavra

print("Palavra Aleatória: ", select_word)
print("Caracteres total: ", total_char_palavra)
print("Mask Palavra: ", mask_palavra_selecionada)
print("-" * 50)


while True:
    os.system("clear")
    print("\n\t[bold]Jogo da Forca - Selecione uma das alternativas[/bold]")

    print("-" * 50)
    arrow = "->"
    pd = Padding(f"[bold][red]{arrow} {select_word}[/red][/bold]", (0, 5))
    print(pd)
    print(f"\n\tPALAVRA X: {mask_palavra_selecionada}\n")
    print("-" * 50)
    print(f"\n\tTotal: {total_tentativas(letras)}\t", end="")
    print(f"\tLetras: {letras_digitos(letras)}\n")

    print("-" * 70)
    print("\t1. Informar uma letra", end="")
    print("\t2. Informar a palavra", end="")
    print("\t0. Sair")
    print("-" * 70)
    print("\n")

    print("-" * 70)

    info_acao = list(reversed(logs[-3:]))
    if len(info_acao) > 0:
        print("LOG: ")
        for id, item in enumerate(info_acao):
            if id < 3:
                print(f"{id}. {item}")
        print("-" * 70)
        print("\n")

    status_game = win(
        mask_palavra_selecionada,
        total_tentativas(letras),
        letras_digitos(letras),
        len(letras),
    )
    if status_game:
        break

    try:
        opt = int(input("Informe o numero da opção: "))

        match (opt):
            case 1:
                # perguntar uma letra
                caractere = pergunta_letra(letras)
                if caractere:
                    letras.append(caractere)
                else:
                    continue

                status = verificar_caracter_existe(
                    caractere, select_word, mask_palavra_selecionada
                )
            case 2:
                # Perguntar a palavras
                palavra_user = input("Iforme a palavra: ")
                valido = enviar_palavra_completa(
                    palavra_user, select_word, mask_palavra_selecionada
                )
                if valido:
                    letras.append(palavra_user)
                    id = 0

                    for word in mask_palavra_selecionada:
                        word = palavra_user[id]
                        id += 1
                else:
                    logs.append("Errouuuuuu! tente novamente!")
                    letras.append(palavra_user)
                    continue
            case 0:
                print("Programa finalizado com sucesso.")
                exit()
            case _:
                print("Opção nao encontrada.")

    except ValueError as e:
        print("ValueError: ", e)
