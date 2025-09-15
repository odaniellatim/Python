from bd import *

class Locadora:
    def __init__(self): #nome, categoria, preco, plataforma
        # self.nome = nome
        # self.categoria = categoria
        # self.preco = preco
        # self.plataforma = plataforma
        # self.plataformas_desejadas = plataformas_desejadas
        ...

    def console(self, *consoles):
      
        for console in consoles:
            
            for fabricante in consoles_db:
                
                if console in fabricante:
                    
                    _fabricante = consoles_db[console]['fabricante_id']
                    nome = consoles_db[console]['nome']
                    preco_usd = consoles_db[console]['preco_usd']
                    print(f"Fabricante: {_fabricante.ljust(20, '-').title()} Console: {nome.ljust(20, '-').title()} Preço: ${preco_usd}")      
        
    def cadastrar_fabricante(self): #nome_chave, nome, pais, *consoles

        nome_chave = input("Digite o nome da maraca do Fabricante. ")
        nome = input("Digite o Nome da Corporação. ")
        pais = input("Digite o Nome do pais origem. ")
        consoles = input("Digite os consoles que a empresa fabrica separados por virgula. ")
        
        dados_empresa = {
            "nome": nome,
            "pais": pais,
            "consoles": consoles.split(","),
        }
        fabricantes_db[nome_chave] = dados_empresa
        
        for fabricante_key, fabricante_nome in fabricantes_db.items():
            print(fabricante_key, fabricante_nome)

    def consoles_cadastrados(self):
        print("")
        
        # Aprenseta a lista com as opções de consoles cadastrados para o usuario
        for id, console in enumerate(consoles_db):
            jogos_por_consoles.append(console)            
            print(f"{id} - {console}")
        
        print("")

    def listar_consoles_cadatrados(self, *consoles_selecionados):
        jogos_por_consoles = []
        item_selecionado = []
        consoles_cadastrado = []
        
        # Cadastra as opções em uma variavel para cadastrar na lista de jogos selecionados pelo usuario
        for id, console in enumerate(consoles_db):
            jogos_por_consoles.append(console)            
                    
        id_plataforma_jogo = consoles_selecionados[0].split(',')
        
        # Filtra a opção do usuario e cadastra em uma variavel os consoles selecionados
        for item_selecao in id_plataforma_jogo:
            consoles_cadastrado.append(jogos_por_consoles[int(item_selecao)])

        #retorna o valor das opções selecionadas pelo usuario
        return consoles_cadastrado

    def cadastrar_jogos(self):
        # "nome": "Grand Theft Auto V",
        # "categoria": "acao",
        # "preco_usd": 30,
        # "plataformas": ["ps4", "xbox_series_x"]

        fabricante = []
        

        codigo_jogo = input("Digite o codigo do jogo 'gta, fortnite...'. ")
        nome_jogo = input("Digite o nome do jogo. ")
        categoria_jogo = input("Digite a categoria do jogo 'Supense, Ação...'. ")
        preco_jogo = input("Digite preco do jogo em dolares. ")

        self.consoles_cadastrados()
        
        consoles_selecionados = input("Digite o ID dos consoles compativeis com o jogo. ")
        
        consoles_selecionados = self.listar_consoles_cadatrados(consoles_selecionados)        
        
        dados_jogo = {
            "nome": nome_jogo,
            "categoria": categoria_jogo,
            "preco_usd": preco_jogo,
            "plataformas": consoles_selecionados,
        }

        jogos_db[codigo_jogo] = dados_jogo
        print(jogos_db)
        
    def listar_jogos(self):

        #print(jogos_db)
        
        for id, jogo in enumerate(jogos_db.keys()):
            nome_jogo = jogos_db[jogo]['nome']
            categoria_jogo = jogos_db[jogo]['categoria']
            preco_jogo = jogos_db[jogo]['preco_usd']
            print(f"{id}. {nome_jogo.ljust(30, '-')} {categoria_jogo.ljust(30, '-').title()} ${preco_jogo}")

    # Função que verifica jogos disponiveis de acordo com o console selecionado
    # Funçãom perfeita para trabalhar com dicionarios grandes e criar um filtro dinâmico.
    # Facilitando a leitura e também a localização das informações mais importantes.
    def jogo_plataforma(self, *plataformas_desejadas):

        if plataformas_desejadas == (): 
            
            self.bd_locadora()
            
        else:
            size_items = len(plataformas_desejadas)
            
            # 1. Itera sobre a lista de plataformas desejadas
            for plataforma in plataformas_desejadas:
                print("-" * 80)
                print(f"Jogos disponíveis para {plataforma.upper()}:")
                print("-" * 80)    
            
                # 2. Itera sobre cada jogo no dicionário de jogos
                for jogo_id, dados_jogo in jogos_db.items():
                    
                    # 3. Verifica se a plataforma atual está na lista de plataformas do jogo
                    
                    
                    if plataforma in dados_jogo['plataformas']:
                        print(f"Nome Jogo: {dados_jogo['nome'].ljust(30, '-')} Categoria: {dados_jogo['categoria'].ljust(20, '-').title()} Preço: ${dados_jogo['preco_usd']}")
                
                # Vefica o tamanho da lista de plataforma enviado pelo usuario e subtrai para saber quando o loop de um jogo é finalizado.
                items = len(plataformas_desejadas)
                size_items -= 1

                #imprime no final da lista o video game com o preço e seu fabricante.
                if size_items < items:
                    print("\n")
                    self.console(plataforma)
                    print("\n \n")

    def menu_principal(self):
        item_menu = {
            "listar_jogos": "listar_jogos",
            # "cadastrar_jogos": ,
            # "remover_jogos": ,
        
            # "listar_fabricantes": ,
            # "cadastrar_fabricantes": ,
            # "remover_fabricantes": ,
                                
            # "listar_consoles": ,
            # "cadastrar_consoles": ,
            # "remover_consoles": ,
        }
        
        for id, menu in enumerate(item_menu):
                print(f"{id}. {menu}")
        print("")
            
        item_selecionado = int(input("Selecione um opção do menu. "))
        
        encerrar_programa = True        
        while encerrar_programa:
            
            match item_selecionado:
                case 0:
                    self.listar_jogos()
                case _:
                    encerrar_programa = False