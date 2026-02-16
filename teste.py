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
        
        
if __name__ == "__main__":    
    sub = SubClasse(10, 20)
    print(sub.numero1)
    print(sub.numero2)