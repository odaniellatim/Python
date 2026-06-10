import random
import os


def load_word() -> list:
    lista_palavras = []
    # Carregando palavras do arquivo.
    with open("palavras.txt", "r") as f:
        data = f.read()
        data = data.split("\n")
        for item in data:
            if item == "":
                continue
            lista_palavras.append(item.lower())
    return lista_palavras


def pergunta_letra(old_letras: dict) -> str | bool:
    letra = input("Informe uma letra: ")
    if not (letra in old_letras):
        if len(letra) == 1 and len(letra) < 2:
            return letra.lower()
        else:
            print("Digite apenas uma unica letra.")
            return False
    else:
        print("Letra já utilizada")
        return False


def letras_digitos(caracteres: list) -> str:
    return " ".join(caracteres)


def total_tentativas(total: list) -> int:
    return len(total)


def selecionar_palavra(palavras: list) -> str:
    word = "".join(random.choices(palavras))
    return word


def verificar_caracter_existe(
    caractere: str, select_word: str, mask_word: list
) -> None | bool:
    if mask_word.count("_") != 0:
        for id, char in enumerate(select_word):
            if caractere in char:
                mask_word[id] = char


def enviar_palavra_completa(
    palavra_user: str, select_word: str, mask_word: list
) -> bool:
    palavra_user.strip()
    palavra_user.lower()
    for letra_user in palavra_user:
        verificar_caracter_existe(letra_user, select_word, mask_word)


def win(mask: list, tentativa: int, letras_usadas: str, size_word: int) -> bool:
    if not ("_" in mask):
        os.system("clear")

        print(f"\n\tParabéns palavra encontrada com {tentativa} tentativas\n")
        print("-" * 50)
        print(f"\n\tPALAVRA X: {mask}\n")
        print("-" * 50)
        print(f"\tLetras: {letras_usadas}\n")
        return True
    return False
