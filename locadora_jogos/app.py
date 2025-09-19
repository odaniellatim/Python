#from locadora_jogos.odl_Locadora import *
from Locadora import Locadora
from base_dados import fabricantes_db, consoles_db, jogos_db


if __name__ == "__main__":
    
    # Instancia da Classe Locadora
    locadora = Locadora(
        fabricantes_db,
        consoles_db,
        jogos_db)
    locadora.listar_jogos()
    #locadora.cadastrar_fabricante("game1","Game One", "Brasil", ["pc", "ps4"])
    #locadora.cadastrar_fabricante("game2","Game two", "Africa", ["ps5", "xbox_series_x","ps4"])
    locadora.listar_fabricantes("ps4")