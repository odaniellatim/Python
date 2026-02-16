class Interface_menu:
    
    @staticmethod
    def menu_inicial() -> int:
        print("1. Entrar com uma conta.")
        print("2. Criar uma conta.")
        print("3. Fechar Programa")

        print("." * 50)
        opcao = int(input("Selecione uma opção: "))
        return opcao
        
    @staticmethod
    def criar_usuario() -> dict:
        nome_completo = input("Informe seu nome completo: ")
        usuario_login = input("Informe um nome de usario: ")
        senha_usuario = input("informe sua senha: ")

        return {
            "nome_completo": nome_completo,
            "usuario_login": usuario_login,
            "senha_usuario": senha_usuario
        }
    
    @staticmethod
    def logar_no_sistema()-> dict:

        usuario = input(" Informe seu usuario: ")
        senha = input(" Informe sua senha: ")
        
        return {
            "usuario": usuario,
            "senha": senha
        }