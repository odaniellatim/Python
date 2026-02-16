import os

from Usuario import Usuario
# from Despesas import Despesas
from Contas_a_pagar import Contas_a_pagar
from Banco_dados import Banco_de_dados
from interface_menu import Interface_menu
from Escrita_na_tela import Escrita_na_tela


class Controle_sistema:
    def __init__(self) -> None:
        pass

    def menu_principal(self):
        encerrar = True
        while(encerrar):
            menu = Interface_menu.menu_inicial()
            match(menu):
                case 1:
                    os.system("clear")
                    self.logar_no_sistema()
                    print("")
                case 2:
                    os.system("clear")
                    # Criar uma conta de usuario.
                    self.cadastro_usuario()
                    print("")
                case _:
                    os.system("clear")
                    print("Opção 3: Selecionado")
                    print("")
                    encerrar = False

    def cadastro_usuario(self):
        novo_usuario = Interface_menu.criar_usuario()

        Usuario(novo_usuario['nome_completo'], novo_usuario['usuario_login'], novo_usuario['senha_usuario'])
        Escrita_na_tela.msg_sucesso("Usuario adicionado com sucesso!")

        new_bd = Banco_de_dados("usuarios.json")
        new_bd.salvar_dados_bd(novo_usuario)

    def logar_no_sistema(self):
        fazer_login = Interface_menu.logar_no_sistema()

        login_bd = Banco_de_dados('usuarios.json')
        dados_user = login_bd.ler_dados_bd()

        if(dados_user['usuario_login'] == fazer_login['usuario'] and dados_user['senha_usuario'] == fazer_login['senha']):
            print("Logado com sucesso.")
        else:
            print("Usuario ou senha invalidos.")