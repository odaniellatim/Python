import os
import json
from Escrita_na_tela import Escrita_na_tela

class Banco_de_dados:

    def __init__(self, filename) -> None:
        self.filename = filename
        self.dirname = "controle_despesas/controle_1.0/BD/"
        self.caminho_completo = os.path.join(self.dirname, self.filename)
    
    # Cria um arquivo com os dados do usuario cadastrado.
    def salvar_dados_user(self, data_user):

        if not(os.path.exists(self.dirname) ):
            os.mkdir(self.dirname)

        with open(self.caminho_completo, 'w') as file_user:            
            file_json_user = json.dumps(data_user, indent=4, ensure_ascii=False)
            file_user.write(file_json_user)

    # Salva os dados do sistema completo em um arquivo.
    def salvar_dados_bd(self, items_salvar):
        if not(self.dirname):
            os.mkdir(self.dirname)
        caminho = self.dirname +self.filename

        with open(caminho, "w") as bd:
            file_json = json.dumps(items_salvar, indent=4, ensure_ascii=False)
            bd.write(file_json)
            Escrita_na_tela.alerta("Dados salvos com sucesso.")

    # Carrega os dados completo do sistema salvo em um arquivo.
    def ler_dados_bd(self):
        caminho = self.caminho_completo
        with open(caminho, "r") as arquivo:
             file_json = json.load(arquivo)
             Escrita_na_tela.alerta("Dados carregado com sucesso.")
             return file_json
        