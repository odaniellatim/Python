
# --- Camada VIEW ---
class TerminalView:         
    def exibir_resultado_soma(self, dado):
        print("."*100)
        print("")
        print(f"O resultado é: {dado}")
        print("")
        print("."*100)
        
    def exibir_resultado_multiplicar(self, dado):
        print("."*100)
        print("")
        print(f"O resultado é: {dado}")
        print("")
        print("."*100)
        
    def menu_principal(self):
        """Menu principal do software onde estarta o programa"""
        print("Menu Principal")
        print("")
        print("1. Realizar a soma: ")
        print("2. Realizar a multiplicação: ")
        print("0. Fechar programa")
        print("")
        opt = int(input("Selecione uma opção: "))
        return opt

# --- Camada MODEL ---
class CalculadoraModel:
    def somar(self, a, b):
        return a + b

    def multiplicar(self, a, b):
        return a * b
    
# --- Camada CONTROLLER (O Agregador) ---
class CalculadoraController:
    def __init__(self, model_recebido, view_recebida):
        # Aqui acontece a AGREGAÇÃO: 
        # O Controller guarda as instâncias para usar depois
        self.model = model_recebido 
        self.view = view_recebida

    def executar_soma(self, v1, v2):
        """ Executa a soma entre dois numeros"""
        # Aqui acontece a ASSOCIAÇÃO: 
        # O Controller chama métodos do Model e da View
        resultado = self.model.somar(v1, v2)
        self.view.exibir_resultado_soma(resultado)

    def executar_multiplicar(self, v1, v2):
        """ Executa a multiplicação  entre dois numeros"""
        # Aqui acontece a ASSOCIAÇÃO: 
        # O Controller chama métodos do Model e da View
        resultado = self.model.multiplicar(v1, v2)
        self.view.exibir_resultado_multiplicar(resultado)

# --- INICIALIZAÇÃO (Main) ---
meu_model = CalculadoraModel()
minha_view = TerminalView()

# Passamos os objetos prontos para o Controller
app = CalculadoraController(meu_model, minha_view)

# Transforma o menu em um loop
while(True):
    teste = CalculadoraModel()    
    opcao = minha_view.menu_principal()

    if(opcao == 1):
       num1 = input("")
      
    if(opcao == 1):               
        num1 = input("Informe o primeiro numero: ")
        num2 = input("Informe o segundo numero: ")
        
        app.executar_soma(int(num1), int(num2))

    if(opcao == 2):               
        num1 = input("Informe o primeiro numero: ")
        num2 = input("Informe o segundo numero: ")
        
        app.executar_multiplicar(int(num1), int(num2))
        
    elif(opcao == 0):
        exit()



        
