from pathlib import Path
import os
import json


class Banco_de_dados:

    def __init__(self, bd_file_name, bd_folder_name):
        self.bd_file_name = bd_file_name
        self.bd_folder_name = bd_folder_name

        # URL do caminho da raiz do projeto "CLI"
        self.bd_dir_raiz = Path.cwd()

        # URL do caminho completo de onde o banco de dados vai ser salvo "PASTA/NOME_FILE".
        self.bd_dir_name = Path(
            self.bd_dir_raiz, self.bd_folder_name, self.bd_file_name)

        # Cria os arquivos essenciais de configuração nos locais corretos.
        self.bd_criar()

    def bd_folder_validate(self) -> None | str:
        """"
        Verifica se a pasta informada já foi criado no sistema.
        @return None -> Se a pasta existir não retorna nada.
        @return str -> Se a pasta não existir no sistema retorna uma mensagem de sucesso.
        """
        if not Path(self.bd_folder_name).is_dir():
            Path(self.bd_dir_raiz, self.bd_folder_name).mkdir(
                parents=True, exist_ok=True)
            print(f"Pasta {self.bd_folder_name} Criada com sucesso")

    def bd_load_data(self):
        """
        Carrega os dados do arquivo json.
        @param file_materiais str -> Caminho completo do arquivo json.
        @return list -> Retorna uma lista de dicionarios
        """
        try:
            # Carrega os dados do arquivo json de materiais e adiciona em uma variavel
            with open(self.bd_dir_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            return []

        return banco_dados

    def bd_criar(self):
        """
        Verifica se o arquivo de configuração existe, caso nao exista
        gera o arquivo com uma lista vazia "[]"

        @return str -> Se o arquivo não existe e é criado, retorna uma msg de sucesso.
        @return None -> Se o arquivo existir, não retorna nada, apenas se existir algum erro.
        """
        data = []
        msg = None

        # Comando para validar se a pasta onde vai ser salvo o banco de dados existe.
        self.bd_folder_validate()

        if not os.path.exists(self.bd_dir_name):
            try:
                with open(self.bd_dir_name, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=2)
                    msg = f"Arquivo {self.bd_file_name} criado com sucesso!"
            except Exception as e:
                raise f"Não foi possivel gerar o arquivo {
                    self.bd_file_name}: {e}"
        return msg

    def bd_add_items(self, data):

        bd = self.bd_load_data()
        if len(bd) > 0:
            bd.extend(data)
            print(bd)
        else:
            bd = data
        try:
            with open(self.bd_dir_name, "w", encoding="utf-8") as file:
                json.dump(bd, file, indent=2, ensure_ascii=False)
                print(f"Os dados foram salvos corretamente no arquivo {
                      self.bd_file_name}.")
        except Exception as e:
            raise Exception(f"Erro ao cadastrar os dados no arquivo {e}")

    def bd_restart(self):
        try:
            with open(self.bd_dir_name, "w", encoding="utf-8") as file:
                json.dump([], file)
        except Exception:
            return []

    def bd_apagar_items(self, id_item_remove):
        load_items_bd = self.bd_load_data()

        for data in load_items_bd:
            if data["custo_fixo_id"] == id_item_remove:
                load_items_bd.remove(data)
                break
        self.bd_restart()
        self.bd_add_items(load_items_bd)

    def get_dic_file(self):
        dicionario = [
            {
                "bd_file_name": self.bd_file_name,
                "bd_folder_name": self.bd_folder_name,
                "bd_dir_raiz": self.bd_dir_raiz,
                "bd_dir_name": self.bd_dir_name,
            }
        ]
        print(" DADOS PARA SALVAR O ARQUIVO")
        print("-" * 60)
        for d in dicionario:
            for key, value in d.items():
                print(f"{key.ljust(20, '.')} {value}")
        print("")


if __name__ == "__main__":
    from src.custo_fixo.custo_fixo import Custo_Fixo
    print("-" * 60)

    # Nome do arquivo que vai ser usado para salvar os dados.
    bd_file_name = "teste_custo_fixo.json"

    # Nome da pasta onde vai ser salvo o banco de dados.
    bd_folder_name = "bd"

    # Instancia o banco de dados e passa as informações referente ao arquivo e pasta
    bd = Banco_de_dados(bd_file_name, bd_folder_name)
    bd.get_dic_file()  # -> Imprime um resumo formatado na tela apenas para consulta

    # Cria o objeto com os dados no construtor
    # cf1 = Custo_Fixo(1, "Telefone Celular", 5000, "pendente", 20, 50, 226.67)
    # cf2 = Custo_Fixo(2, "Água", 150, "pendente", 20, 1, 226.67)

    # imprime e retonar um dicionario formatado para visualização e também para cadastro
    # data = cf1.get_dict()
    # data2 = cf2.get_dict()

    # Adiciona novos items no banco de dados.
    # bd.bd_add_items([data, data2])

    # Carregar os dados que estão salvos no arquivo.
    # data = bd.bd_load_data()
    # print(data)

    # Apaga um item pelo ID e atualiza o banco de dados
    # apagar_item = bd.bd_apagar_items(2)

    # Zerar o banco de dados completamente.
    # bd.bd_restart()

    def add(bd):

        id_item = len(bd.bd_load_data()) + 1
        nome_item = input("Nome do produto / serviço: ")
        valor_item = float(input("Valor do produto / serviço: "))
        status_item = input("informe o status de pagamento: [pendente|pago]")
        vendas_item = 20
        durabilidade_meses_item = int(input(
            "Informe a durabilidade do produto/serviço numero em meses: "))
        valor_despesa_total_item = 226.67

        cf1 = Custo_Fixo(id_item, nome_item, valor_item, status_item, vendas_item,
                         durabilidade_meses_item, valor_despesa_total_item)
        data = cf1.get_dict()
        bd.bd_add_items(data)

    oppcao = None
    while (True):
        print("Selecione uma das opções: ")
        print("1. Cadastrar items")
        print("2. Reset Banco de Dados")
        print("9. Fechar programa")
        oppcao = int(input("Infome o numero da opção: "))
        match (oppcao):
            case 1:
                add(bd)
            case 2:
                bd.bd_restart()
            case 9:
                exit()

    print("-" * 60)
