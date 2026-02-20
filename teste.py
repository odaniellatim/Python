"""
Página de teste de codigos Python
"""

class ClassePrincipal:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def result_num1(self):
        return self.numero1
    
    def result_num2(self):
        return self.numero2
    
class SubClasse(ClassePrincipal):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
def tabela():
    titulo = ["Gás", "Luz", "Água"]
    descrição = ["Conta de gás", "Conta de luz", "Conta de água"]
    valor = [150,252,150]
    headline = ["TITULO", "DESCRIÇÃO", "VALOR R$"]
    return f"""

    |{str(headline[0]).center(10)}|{str(headline[1]).center(30)}|{str(headline[2]).center(5)}|
    -----------------------------------------------------------------------------------------
    |{str(titulo[0]).center(10)}|{str(descrição[0]).center(30)}|{str(valor[0]).center(5)}|
    |{str(titulo[1]).center(10)}|{str(descrição[1]).center(30)}|{str(valor[1]).center(5)}|
    |{str(titulo[2]).center(10)}|{str(descrição[2]).center(30)}|{str(valor[2]).center(5)}|

"""
        
if __name__ == "__main__":    
    print(tabela())