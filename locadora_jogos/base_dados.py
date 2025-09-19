# Dicionário de Consoles (com ID)
consoles_db = {
    "ps5": {
        "fabricante_id": "sony",
        "nome": "PlayStation 5",
        "ano_lancamento": 2020,
        "preco_usd": 499,
        "armazenamento_gb": 825
    },
    "ps4": {
        "fabricante_id": "sony",
        "nome": "PlayStation 4",
        "ano_lancamento": 2013,
        "preco_usd": 299,
        "armazenamento_gb": 500
    },
    "xbox_series_x": {
        "fabricante_id": "microsoft",
        "nome": "Xbox Series X",
        "ano_lancamento": 2020,
        "preco_usd": 499,
        "armazenamento_gb": 1000
    },
    "pc": {
        "fabricante_id": "microsoft",
        "nome": "Windows 11",
        "ano_lancamento": 2019,
        "preco_usd": 699,
        "armazenamento_gb": 1000
    }
}

# Dicionário de Fabricantes (com ID)
fabricantes_db = {
    "sony": {
        "nome": "Sony Interactive Entertainment",
        "pais": "Japão",
        "consoles": ["ps4","ps5"],
    },
    "microsoft": {
        "nome": "Microsoft Corporation",
        "pais": "EUA",
        "consoles": ["xbox_series_x"],
    }
}

# Dicionário de Jogos (com ID e referências a consoles)
jogos_db = {
    "gta_v": {
        "nome": "Grand Theft Auto V",
        "categoria": "acao",
        "preco_usd": 39.90,
        "alugado": False,
        "plataformas": ["ps4", "xbox_series_x"]
    },
    "god_of_war": {
        "nome": "God of War",
        "categoria": "acao",
        "preco_usd": 59.90,
        "alugado": False,
        "plataformas": ["ps5"]
    },
    "halo_infinite": {
        "nome": "Halo Infinite",
        "categoria": "fps",
        "alugado": True,
        "preco_usd": 59.98,
        "plataformas": ["xbox_series_x"]
    },
    "cyberpunk_2077": {
        "nome": "Cyberpunk 2077",
        "categoria": "rpg",
        "preco_usd": 39.59,
        "alugado": False,
        "plataformas": ["ps5", "xbox_series_x", "pc"]
    },
    "the_witcher_3": {
        "nome": "The Witcher 3: Wild Hunt",
        "categoria": "rpg",
        "preco_usd": 22.59,
        "alugado": True,
        "plataformas": ["ps4", "xbox_series_x", "pc", "nintendo_switch"]
    },
    "animal_crossing": {
        "nome": "Animal Crossing: New Horizons",
        "categoria": "simulacao",
        "preco_usd": 58.90,
        "alugado": False,
        "plataformas": ["nintendo_switch"]
    },
    "fortnite": {
        "nome": "Fortnite",
        "categoria": "battle_royale",
        "preco_usd": 0.99,
        "alugado": True,
        "plataformas": ["ps5", "xbox_series_x", "pc", "nintendo_switch"]
    }
}