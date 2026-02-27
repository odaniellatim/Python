from src.orcamento_projeto import OrcamentoProjeto 


# Start App
if __name__ == "__main__":

    # Cria o projeto com ID e Nome
    #--------------------------------------------------------------------------------------
    
    colorgin = OrcamentoProjeto(1, "Tênis Colorgin")

    # Cadastro de items para realizar o projeto Colorgin
    # id, nome, valor, quantidade, unidade_medida, qntd_usado_projeto
    #--------------------------------------------------------------------------------------
    
    it1 = colorgin.add_itens_materiais(1, "Tinta Vermelha", 33.33, 90, "ml", 5)
    it2 = colorgin.add_itens_materiais(2, "Verniz Novax", 49.90, 1000, "ml", 20)
    it3 = colorgin.add_itens_materiais(3, "Bisturi", 35.97, 100, "unidade", 1)
    it4 = colorgin.add_itens_materiais(4, "Tinta Cinza Veox", 27.90, 500, "ml", 5)

    # Local para executar as funções e analisar se o codigo está correto
    #--------------------------------------------------------------------------------------
    
    # Cadastro da renda mensal base.
    #--------------------------------------------------------------------------------------

    # colorgin.add_renda_mensal(5000,30,16)
    colorgin.add_mao_de_obra(150, 6, 45) # Anotação usando atalho de teclado do emacs...
    
    try:
        print(f"ID:{colorgin.orcamento_id}")
        print(f"Items: ")
        colorgin.material_valor_total_produtos_usados
        
    except ValueError as e:
        print(f"Erro: {e}")
