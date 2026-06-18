class Materiais:
    def __init__(self, material_id, material_nome, material_preco, material_quantidade):
        self.material_id = material_id
        self.material_nome = material_nome
        self.material_preco = material_preco
        self.material_quantidade = material_quantidade

    def get_valor_produto(self):
        return self.material_preco

    def listar_material(self):
        print(f"ID. {self.material_id} \t", end="")
        print(f"Nome: {self.material_nome} \t", end="")
        print(f"Preço: {self.material_preco} \t", end="")
        print(f"Valor por qntd: {round(self.valor_quantidade(), 2)} \t")

    def valor_quantidade(self):
        return self.get_valor_produto() / self.material_quantidade

class Orcamento:
    def __init__(self, orcamento_id):
        self.orcamento_id = orcamento_id
        self.orcamento_materiais: list[Materiais] = []

    def oc_add_materiais(self, id_material, nome_material, preco_material, quantidade_material):
        if id_material and nome_material and preco_material and quantidade_material != "":
            material = Materiais(id_material, nome_material, preco_material, quantidade_material)
            self.orcamento_materiais.append(material)

    def oc_listar_materiais(self):
        for material in self.orcamento_materiais:
            material.listar_material()
            print("-" * 70)
        print("Total Estoque: R$ ",self.oc_valor_estoque())

    def oc_valor_estoque(self):
        total_estoque = 0
        for material in self.orcamento_materiais:
            total_estoque += material.get_valor_produto()
        return total_estoque
            
class Painel:
    def __init__(self, orcamento) -> None:
        self.orcamento = orcamento
    
    def iniciar(self):
        while True:
            print("\n")
            print("PROGRAMA INICIADO")
            print("1. Listar produto")
            print("2. adicionar novo material")
            print("0. Sair")
            print("-" * 70)
            opcao = input("Selecione uma das opcoes: ")

            match opcao:
                case '1':
                    self.op1()
                case '2':
                    self.op2()
                case '3':
                    ...
                case '0':
                    break
                case _:
                    print("\n OPCAO NAO ENCONTRADA\n")

    def op1(self):
        print("\n LISTANDO OS MATERIAIS CADASTRADOS")
        print("-" * 70)
        self.orcamento.oc_listar_materiais()
        print("-" * 70)
        print("\n")

    def op2(self):
        print('\n\n')
        nome_material = input("Nome do produto: ")
        preco_material = input("Qual o valor pago no produto: ")
        quantidade_material = input("Informe a quantidade da embalagem: ")
        try:
            orcamento.oc_add_materiais(idRandom, nome_material, float(preco_material), int(quantidade_material))
        except:
            print("Erro ao realizar o cadastro.")






if __name__ == "__main__":
    import random

    idRandom = random.randint(1,99999)  
    orcamento = Orcamento(idRandom)

    menu = Painel(orcamento)
    menu.iniciar()
