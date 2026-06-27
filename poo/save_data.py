from pathlib import Path
import json


class SaveDataFile:
    def __init__(self, folder_name, file_name):
        self._home_dir = Path()
        self.folder_name = folder_name
        self.file_name = file_name
        # self.folder_exist()

    @property
    def home_dir(self):
        """Gerando a url base do sistema"""
        return self._home_dir.home()

    def get_url_cwd(self):
        """Gerando a url base do diretorio com base no arquivo"""
        return self.home_dir.cwd()

    def save_data_url(self):
        """Gerando a url base para salver os dados no arquivo."""
        return Path(self.get_url_cwd(), self.folder_name, self.file_name)

    def folder_exist(self):
        """Validando se o diretorio (pasta) existe
        se não existir cria a pasta direto no construtor"""
        folder = self.save_data_url().parent
        exist = folder.exists()
        if not exist:
            folder.mkdir()
        return exist

    def save_data(self, data):
        # Verifica se a pasta para salvar o arquivo existe
        self.folder_exist()

        with open(self.save_data_url(), "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            print("Dados salvo com sucesso")

    def load_data(self, folder_name, file_name):
        """Carrega dos dados do arquivo salvo no sistema"""
        data = self.save_data_url()
        bd_file = ""
        try:
            with open(data, "r") as file:
                bd_file = json.load(file)
        except json.JSONDecodeError:
            bd_file = []
        return bd_file


if __name__ == "__main__":
    pasta = "data"
    arquivo = "data_.json"

    data = SaveDataFile(pasta, arquivo)
    # url_home = data.home_dir
    url_home = data.save_data_url()
    print(url_home)

    dicionario = [
        {"texto": "texto completo sobre o que vamos fazer para salvar"},
    ]

    url_home = data.save_data(dicionario)
    url_home = data.load_data(pasta, arquivo)
    print(url_home)
    # for item in url_home:
    #     print(item)

    pasta2 = "materiais"
    arquivo2 = "materiais.json"

    new_data = [{"item1": "resultado item 1"}]

    material = SaveDataFile(pasta2, arquivo2)
    item1 = material.save_data_url()
    print(item1)
    item1 = material.save_data(new_data)
    item1 = material.load_data(pasta2, arquivo2)
    print(item1)
