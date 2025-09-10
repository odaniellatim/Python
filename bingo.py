import random as rd
import os
import time

#numeros do bingo em jogo
numeros_bingo = [0,1,2,3,4,5,6,7,8,9,10]
numeros_sorteados = []

#Randomiza os numeros do bingo.
rd.shuffle(numeros_bingo)

#gera um numero aleatório toda após a confirmação do usuario.
print(" ")
print(" Defina o tempo de espeara entre cada Rodada: ")
tempo_rodada = int(input())
os.system('clear')

def gerador_aleatorio():

    #gera um numero aleatório
    n = rd.randint(0,10)
    return gera_numero(n)

def gera_numero(n):

    os.system('clear')
    
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
        os.system('clear')

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
            os.system('clear')
            numeros_sorteados.clear();
            numeros_bingo = [0,1,2,3,4,5,6,7,8,9,10]
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
    