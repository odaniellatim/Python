import argparse

print("")

def fnAction(lista: list):
    print(lista)

def fnCalc(lista: list):
    print(f"Soma de: ", end="")
    print(*lista, sep=" + ")
    total = 0
    for l in lista:
        total += l
    print("")
    print(f"Total: {total}")

def fnInput():
    n1 = input("Numero 1: ")
    n2 = input("Numero 2: ")
    print("Multiplicando.... \n\n")

    calc = float(n1) * float(n2)
    print(f"Resultado: {calc}")

parse = argparse.ArgumentParser(prog="Programa de teste", usage="Programa para teste conceitos de linha de comando")

# Recebe uma lista de informações
parse.add_argument("-numeros", help="Comando para somar multiplos numeros", type=float, nargs="+")

# Chama uma função especifica passando o parametro
parse.add_argument("-fn", help="Chama uma função ao usar esse comando", action="store_true")

args = parse.parse_args()

print(args)

if(args.numeros):
    fnAction(args.numeros)
elif (args.fn):
    fnInput()
print("")
