# Retorna o valor do dolar atual
def valor_dolar(dolar_atual: float = 5.17):
    return round(dolar_atual, 2)


# Define o valor de salario planejado para receber no Mês
def def_salario(salario_mes: float):

    if salario_mes != 0.00:
        salario = salario_mes
        # print(f"{salario} - Entrou no IF")
        return round(salario, 2)
    else:
        salario = 5_000.00
        # print(f"{salario} - Entrou no ELSE")
        return round(salario, 2)


# Retorna o valor médio em Real e em Dolar Americano
def valor_medio_projetos(salario: float, projetos: int):

    valor_medio = def_salario(salario) / projetos
    valor_medio_dolar = valor_medio / valor_dolar()

    return round(valor_medio, 2), round(valor_medio_dolar, 2)


# valor hora de trabalho
def valor_hora(renda: float, hora_trabalhado: int, minuto_trabalhado: int):
    # renda = salario(renda)  # Valor Salario Planejado no mês

    HORA_TOTAL_MES: int = 180  # horas total trabalhadas no mês
    valor_h_trabalhado_mes = (
        def_salario(renda) / HORA_TOTAL_MES
    )  # Calcula o valor trabalhado em 1 hora baseado na renda desejada.
    valor_m_trabalhado_mes = def_salario(renda) / (
        HORA_TOTAL_MES * 60
    )  # Calcula 0 valor do minuto trabalhado baseado na renda desejada.

    valor_total_de_horas = valor_h_trabalhado_mes * hora_trabalhado
    valor_total_de_minutos = valor_m_trabalhado_mes * minuto_trabalhado

    # converte hora em minutos para calcular o valor do minuto
    convert_hora_minuto = (hora_trabalhado * 60) + minuto_trabalhado
    valor_total_projeto = convert_hora_minuto * valor_m_trabalhado_mes

    return valor_total_projeto, valor_total_de_horas, valor_total_de_minutos


if __name__ == "__main__":
    # Variaveis de configuração base para o programa funcionar
    salario_mensal = 5000  # Valor do salario mensal desejado, usado para realizar os calculos do valor em hora e minuto
    horas_projeto = 3
    minutos_projeto = 38
    projetos_mensal = 15

    print(" " * 70)

    # Apresenta os dados de valor por hora
    orçamento2 = valor_hora(salario_mensal, horas_projeto, minutos_projeto)

    print(f"Valor total das {horas_projeto} horas é: R$ {round(orçamento2[1], 2)}")
    print(f"Valor total dos {minutos_projeto} minutos é: R$ {round(orçamento2[2], 2)}")
    print(" " * 70)
    print(
        f"Valor total das {horas_projeto} horas e {minutos_projeto} minutos trabalhadas: R$ {round(orçamento2[0], 2)}"
    )
    print(" " * 70)
    print("-" * 70)
    print(" " * 70)

    # Apresenta os dados de valor médio em Real e em Dolar
    valor_medio = valor_medio_projetos(salario_mensal, projetos_mensal)
    print(f"Valor médio: R$ {valor_medio[0]}")
    print(f"Valor médio: $ {valor_medio[1]}")

    print(" " * 70)
    print(" " * 70)
    print(" " * 70)
