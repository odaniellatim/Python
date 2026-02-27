from enum import StrEnum

class UnidadeMedida(StrEnum):
    # Liquidos
    LITRO = "l"
    MILILITRO = "ml"

    # Comprimento
    METRO = "m"
    CENTIMETRO = "cm"
    MILIMETRO = "mm"

    # Massa
    KILO = "kg"
    GRAMA = "g"
    ONCA = "oz" # = 28,35g

    # Unidade
    UNIDADE = "unidade"