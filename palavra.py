import os

separador = "                                  "
palavra_secreta = input("Digite a palavra secreta: ").lower()
letras_acertadas = ""
numero_tentativas = 0
numeros_validos = False
item_menu = 0
os.system("clear")

while True:
    print(separador)
    print("[1].  Digite 1 para selecionar uma letra.")
    print("[2].  Digite 2 para tentar uma palavra.")
    print(separador)

    print(f"A Palavra Secreta tem: {len(palavra_secreta)} letras")
    print(separador)
    opcao = input("Selecione um item do menu: ")
    opcao_valida = opcao.isdigit()

    # verifica se valor informado é valido.
    if opcao_valida == True:
        item_menu = int(opcao)
        os.system("clear")

    else:
        print("Digite apenas numeros.")

    # entra na execução do programa item 1 do menu - Digita a letra e verifica as faltantes.
    if item_menu == 1:
        print(item_menu)
        print(separador)
        print("Tentativa", numero_tentativas)

        numero_tentativas += 1
        letra_digitada = input("Digite uma letra: ").lower()

        if len(letra_digitada) > 1:
            print("Digite apenas uma letra.")
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        palavra_formada = ""

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += "*"

        print(separador)
        print("Palavra formada: ", palavra_formada)

        print(f"A Palavra Secreta tem: {len(palavra_secreta)} letras")

        if palavra_formada == palavra_secreta:

            print("VOCÊ GANHOU! PARABÉNS!")
            print("A palavra era", palavra_secreta)
            print(f"Você ACERTOU COM {numero_tentativas} TENTATIVAS")
            letras_acertadas = ""
            numero_tentativas = 0
            print(palavra_secreta)

    # entra na execução do programa item 2 do menu - Digitar palavra e veficar se está correta.
    elif item_menu == 2:
        print(separador)
        print("Tentativa", numero_tentativas)

        numero_tentativas += 1
        palavra_digitada = input("Digite uma palavra: ").lower()
        print(palavra_digitada)

        if palavra_digitada in palavra_secreta:
            os.system("clear")
            print("VOCÊ GANHOU! PARABÉNS!")
            print("A palavra era", palavra_secreta)
            print(f"Você ACERTOU COM {numero_tentativas} TENTATIVAS")
            letras_acertadas = ""
            numero_tentativas = 0
            print(palavra_secreta)
        else:
            print(f'Erro: A palavra "{palavra_digitada}" está errada!')

    else:
        print("Digite um numero que está no MENU.")
