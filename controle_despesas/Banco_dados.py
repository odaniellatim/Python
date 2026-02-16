import json

class Banco_de_dados:
    def __init__(self, filename) -> None:
        self.filename = filename

    def salvar_dados_bd(self, items_salvar):
        with open(self.filename, "w") as bd:
            file_json = json.dumps(items_salvar, indent=4, ensure_ascii=False)
            bd.write(file_json)

    def ler_dados_bd(self):
        with open(self.filename, "r") as arquivo:
             file_json = json.load(arquivo)
             return file_json