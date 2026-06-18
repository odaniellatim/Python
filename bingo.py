import random as rd
import os
import time

#numeros do bingo em jogo
numeros_bingo = []
numeros_sorteados = []

#Randomiza os numeros do bingo.
rd.shuffle(numeros_bingo)

#Configuração do sistema antes de iniciar a roda.
print(" ")
print(" Defina o tempo de espeara entre cada Rodada: ")
tempo_rodada = int(input())

os.system('cls')

quantidade_numeros_bing = int(input("Digite a quantidade maxima de numeros a ser sorteados. \n -> "))
for numero in range(1, quantidade_numeros_bing):
  numeros_bingo.append(numero)

os.system('cls')


def gerador_aleatorio():

    #gera um numero aleatório
    n = rd.randint(0,quantidade_numeros_bing)
    return gera_numero(n)

def gera_numero(n):

    os.system('cls')
    
    print("-" * 50)
    print(" ")

    
    #Numero sorteado bingo
    if n in numeros_bingo:
        print(f"Numero Sorteado: {n}")
        numeros_sorteados.append(n)
        numeros_bingo.remove(n)

        # mostra o numero sorteado da Rodada Anterior
        if(len(numeros_sorteados) > 1):
          print("")
          print(f"Numero Anterior: {numeros_sorteados[-2]}")
        
        return n
    else:
        if len(numeros_bingo) > 0:
            #chama a função novamente para gerar um novo numero
            gerador_aleatorio()

while True:

    #Pausa o programa para as pessoas anotarem o numero gerado
    time.sleep(tempo_rodada)

    #Verifica se os numeros disponiveis para sorteio foram finalizados
    if len(numeros_bingo) == 0:
        os.system('cls')

        print(" ------------ VENCEDOR ------------")
        print(" ")

        # imprime na tela os numeros vencedores
        print("Cartela Sorteada: ", end=" ")
        i = 0
        for numero in numeros_sorteados:
            
            if i == (len(numeros_sorteados)-1):
                print(f"{str(numero)}", end="\n \n")
            else:
              print(f"{str(numero)}", end=" - ")
              i += 1 
              
        print("-" * 50)
        print("")

        # Cria um munu interativo para ENCERRAR ou CONTINUAR uma nova partida
        print("[S] -> Recomeçar? \n[N] -> Cancelar")
        print("")
        recomecar = input("-> ")

        if recomecar == "s" or recomecar == "S":
            os.system('cls')
            numeros_sorteados.clear();
            numeros_bingo = numeros_bingo
        else:
            break
    else:
        print(f'Rodada: {len(numeros_sorteados)}')
        print("-" * 50)

    #gera um numero aleatório
    n = rd.randint(0,10)

    #chama a função que gera o numero e valida se já existe
    gera_numero(n)
    
    print(" ")
    print("-" * 50)
    
    #Numeros que já foram sorteados           
    print(" ")
    
    # gerar numeros maior que 4 (1-4) evitar numeros sequenciais11
    
    #