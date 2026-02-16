import os
import json

class Banco_de_dados:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def ler_arquivo(self):
        
        if(os.path.exists(self.file_name)):
            arquivo = open(self.file_name, "r")            
            dados_bd = json.load(arquivo)
            arquivo.close()

            return dados_bd
        else:
            print("Arquivo criado com sucesso")
            arquivo = open(self.file_name, 'x')
            arquivo.close()

    def gravar_dados(self, items_despesas: list) -> None:
        arquivo = open(self.file_name, "w")
        arquivo.write(json.dumps(items_despesas, indent=4, ensure_ascii=False))
        arquivo.close()