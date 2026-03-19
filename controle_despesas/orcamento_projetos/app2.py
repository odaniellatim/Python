from src.interface_menu import InterfaceMenu


# Start App
if __name__ == "__main__":

    # Menu Inicial
    # --------------------------------------------------------------------------------------
    app = InterfaceMenu()

    while (True):
        opt = app.menu_home()  # Menu inicial

        match(int(opt)):
            case 1:
                add_oc = app.if_add_orcamento()
            case 2:
                app.if_add_materiais()
            case 3:
                app.if_listar_materiais()

    # Cadastro de items para realizar o projeto Colorgin
    # id, nome, valor, quantidade, unidade_medida, qntd_usado_projeto
    # --------------------------------------------------------------------------------------

    # it1 = colorgin.add_itens_materiais(1, "Tinta Vermelha", 33.33, 90, "ml", 5)
    # it2 = colorgin.add_itens_materiais(2, "Verniz Novax", 49.90, 1000, "ml", 20)
    # it3 = colorgin.add_itens_materiais(3, "Bisturi", 35.97, 100, "unidade", 1)
    # it4 = colorgin.add_itens_materiais(4, "Tinta Cinza Veox", 27.90, 500, "ml", 5)

    # Local para executar as funções e analisar se o codigo está correto
    # --------------------------------------------------------------------------------------

    # Cadastro da renda mensal base.
    # --------------------------------------------------------------------------------------

    # colorgin.add_renda_mensal(5000,30,16)
