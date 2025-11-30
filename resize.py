# função que faz o calculo para econtrar o valor de altura ideal
def largura(x):
    wide = 16 * x / 9
    return round(wide)

# função que faz o calculo para econtrar o valor de largura ideal
def altura(x):
    altura = x * 9 / 16
    return round(altura)
    
# função que que verifica o valor e converte o numero em inteiro.
def convertimg(l=0, a=0):
    if l == "" or a == "":
        print("      ---------        ")
        return print("Erro: Numero de Largura Invalido!")
    elif l != 0 or a != 0:
        larguraobj = int(l)
        alturaobj = int(a)
        print("                               ")
        print("                               ")
        print(f"Para deixar 16:9 as medidas são: {larguraobj} x {largura(larguraobj)}")
        print(f"Para deixar 16:9 as medidas são: {altura(alturaobj)} x {alturaobj}")
    else:
        print("      ---------        ")
        print("O numero deve ser maior que 0!")

sair = ""
while True:
    if sair == "X" or sair == "x":
        break
    else:
        print("                               ")
        larg = input("Infome a largura da imagem? ").strip()
        alt = input("Infome a altura da imagem? ").strip()
        convertimg(larg, alt)
        print("                               ")
        print("                               ")
        print("                               ")

        sair = input("Digite [X] para sair ou aperte [ENTER] para continuar:  ")
