import random
from src.projeto_controller import ProjetoController


class InterfaceMenu:
    """ Classe interface menu: onde é apresentada as opções para que possa permitir o usuario interagir com o software."""
    def __init__(self):
        self.pj_controller: ProjetoController = ProjetoController()

    def header_menu(self, headline: str = None):
        print("-" * 100)
        if (headline != None):
            print(f"{headline.upper()}")
        else:
            print(f"MENU PRINCIPAL")
        print("-" * 100)
        print("")

    # Menu principal de boas vindas
    def menu_home(self):
        self.header_menu()

        print("1. Cadastrar Orçamento")
        print("2. Cadastrar Materiais")
        print("3. Listar Materiais Cadastrados")

        print("")
        
        option = input("Informe o numero de uma das opções: ")
        return option

    # Add orcamento
    def if_add_orcamento(self):
        self.header_menu("Adicionar Orçamento")

        ID = random.randint(1, 10000)
        nome_orcamento = input("Informe o nome do orçamento: ")
        add = self.pj_controller.pc_add_orcamento(ID, nome_orcamento)

        if (add):
            print("Cadastro realizado com sucesso!")
            return True
        else:
            print("Erro: Não foi possivel realizar o cadastro.")

    # Add materiais
    def if_add_materiais(self):
        self.header_menu("Cadastrar Materiais")

        # op_add_materiais(self, id, nome, valor, quantidade, unidade_medida, qntd_usado_projeto)
        ID = random.randint(1, 10000)
        nome = input("Informe o nome do material: ")
        valor = float(input("Informe o valor pago no material: R$ "))
        quantidade = int(
            input("Informe a quantidade quantidade do material: "))

        print("1. litro")
        print("2. mililitro")
        print("3. kilo")
        print("4. grama")
        print("5. onca (oz)")
        print("6. unidade")
        print(" ")
        unidade_medida = input("Selecione uma das opções da unidade medida: ")

        qntd_usado = int(input("informe a quantidade usado no projeto: "))
        print("")

        add_material = self.pj_controller.pc_cadastrar_materiais(
            ID, nome, valor, quantidade, unidade_medida, qntd_usado)

        if (add_material):
            print("Material Adicionado com sucesso!")
        else:
            print("Não foi possivel cadastrar o material")

    # Listar materiais

    def if_listar_materiais(self):
        """ Listar materais cadastrados no projeto. Método da classe InterfaceMenu"""
        self.header_menu("Lista dos Materiais Cadastrados")

        mt = self.pj_controller.pc_listar_materiais_cadastrados()
        for material in mt:
            print(f"ID material: {material['material_id']}")
            print(f"Nome material: {material['nome_material']}")
            print(f"Preço material: R$ {round(material['preco_material'], 2)}")
            print(f"Quantidade: {
                  material['quantidade_material']}/{material['unidade_medida']}")
            print(f"Qntd material usado: {
                  material['qntd_material_usado']}/{material['unidade_medida']}")
            # print(f"Preço por {self.material_unidade_medida}: R$ {self.material_valor_por_qntd(self.material_unidade_medida):.2f}")
            # print(f"Preço de {self.material_qntd_usado_projeto}/{self.material_unidade_medida}: R$ {self.material_valor_total_qntd_usado_projeto():.2f}")
            print("-" * 100)
            # {'material_id': 6167, 'nome_material': 'Branco', 'preco_material': 33.33, 'quantidade_material': 90, 'unidade_medida': 'ml', 'qntd_material_usado': 10}


if __name__ == "__main__":

    app = InterfaceMenu()
    app.if_listar_materiais()

#    app.menu_home() # Menu Inicial

# app.if_add_orcamento() # Menu cadastro orçamento

# app.if_add_materiais() # Menu de Cadastro de Materiais
