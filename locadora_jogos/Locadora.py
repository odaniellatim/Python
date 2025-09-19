class Locadora:
    def __init__(self, fabricantes, consoles, jogos):
        self.fabricante = fabricantes
        self.consoles = consoles
        self.jogos = jogos
    
    def listar_jogos(self):
        for console in self.consoles:
            print("")
            print(f"JOGOS DO CONSOLE: {console.upper()}")
            print("-" * 130)
            
            for jogo in self.jogos:
                if console in self.jogos[jogo]['plataformas']:
                    print(f"Codigo: {jogo.ljust(30, '.')} Nome: {self.jogos[jogo]['nome'].ljust(35, '.')} Categoria: {self.jogos[jogo]['categoria'].ljust(20, '.')} Preço: $ {str(self.jogos[jogo]['preco_usd']).ljust(10, '.')} Alugado: {self.jogos[jogo]['alugado']}")
                    
            self.listar_fabricantes(console)
    
    def cadastrar_fabricante(self,fb_codi, fb_nome, fb_pais, fb_consoles):

        self.fabricante[fb_codi] = {
            "nome": fb_nome,
            "pais": fb_pais,
            "consoles": fb_consoles
        }
        print(f"O fabricante '{self.fabricante[fb_codi]['nome']}' Cadastrado com Sucesso!")
        
    def listar_fabricantes(self, fabricante_id=None):
        print("")       
 
        
        for id, fabricante in self.fabricante.items():
            fabricante_nome = self.fabricante[id]['nome']
            pais_nome = self.fabricante[id]['pais']
            consoles_nome = self.fabricante[id]['consoles'] # Lista de itens
            console_string = ", ".join(consoles_nome)
            
            if fabricante_id == None:
                print(f"id: {id.ljust(15,'.')} Empresa: {fabricante_nome.ljust(40, '.').title()} Pais: {pais_nome.ljust(20, '.').title()} Consoles: {console_string.title()}")
            else:
                if fabricante_id in self.fabricante[id]['consoles']:
                    print(f"id: {id.ljust(15,'.')} Empresa: {fabricante_nome.ljust(40, '.').title()} Pais: {pais_nome.ljust(20, '.').title()} Consoles: {console_string.title()}")
            
        print("")
        