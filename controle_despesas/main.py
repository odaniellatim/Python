from Banco_de_dados import *
from Despesas import *

# Instancia do banco de dados (Arquivo) para verificar se existe dados/arquivo de controle e puxar para a instancia das Despesas
bd = Banco_de_dados("bd_items.json")
obj = bd.ler_arquivo()

# definição dos valores a pagar (valores de exemplo).
QT_TENIS_PINTADOS: float = 20
aluguel: float = 2_048.44
cc_pf_nubank: float = 1_749.30
cc_pj_nubank: float = 84.55
cc_carrefour: float = 462.92
agua: float = 140.00
luz: float = 250
claro: float = 300
cnpj: float = 80.00
valor_emergencia = 2.0

# Instancia das Despesas com os valores do arquivo se existir 
despesas = Despesas(QT_TENIS_PINTADOS, aluguel, cc_pf_nubank, cc_pj_nubank, agua, luz, claro, cnpj, valor_emergencia)

# Calcula os valores das despesas e lista na tela o resultado.
resultado_math = despesas.math_soma()
despesas.listar_resultado(resultado_math)

bd.gravar_dados(resultado_math)
