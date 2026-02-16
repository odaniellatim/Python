# Receber no construtor os valores base (bruto) para o calculo do salario
# Permitindo quebrar o valor para o minimo e usar no orçamento com mais flexibilidade
# Separamos os valores ganhos por Dia, Horas e Minutos


class Config_salario:

    def __init__(
        self,
        salario_total: float,
        dias_trabalhados: int,
        horas_trabalhada_dia: float,
        dolar_atual: float,
    ):
        self.salario_mensal = salario_total
        self.valor_dolar = dolar_atual
        self.dias_trabalhados = dias_trabalhados
        self.horas_trabalhadas_dia = horas_trabalhada_dia

    # Valor Ganhos por Dia (Real / Dolar)
    def salario_dia(self) -> dict:

        # Calcula o valor ganho por dia de trabalho
        total_dia_real = self.salario_mensal / self.dias_trabalhados

        # Calcula o valor ganho por dia de trabalho e divide pelo valor do dolar atual
        total_dia_dolar = total_dia_real / self.valor_dolar

        return {"real_dia": total_dia_real, "dolar_dia": total_dia_dolar}

    # Valor Ganhos por Hora (Real / Dolar)
    def salario_hora(self) -> dict:
        ganho_real_dia = self.salario_dia()["real_dia"]
        ganho_dolar_dia = self.salario_dia()["dolar_dia"]

        # Calcula o valor total de horas trabalhadas no mês
        total_horas_trabalhadas_mes = self.horas_trabalhadas_dia * self.dias_trabalhados

        # Calcula o valor da hora trabalhada.
        valor_hora_real = self.salario_mensal / total_horas_trabalhadas_mes

        # Converte o valor da hora trabalhada para dolar.
        valor_hora_dolar = (
            self.salario_mensal / total_horas_trabalhadas_mes
        ) / self.valor_dolar

        return {"real_hora": valor_hora_real, "dolar_hora": valor_hora_dolar}

    # Valor Ganhos por Minutos (Real / Dolar)
    def salario_minuto(self) -> dict:
        ganho_real_hora = self.salario_hora()["real_hora"]
        ganho_dolar_hora = self.salario_hora()["dolar_hora"]
        minutos_dia = 60

        # Valor do minuto trabalhado
        valor_minuto_real = ganho_real_hora / minutos_dia
        valor_minuto_dolar = ganho_dolar_hora / minutos_dia

        return {"real_minuto": valor_minuto_real, "dolar_minuto": valor_minuto_dolar}

    # Retorna o numero de dias trabalhados para informar o usuario.
    def total_dias_trabalhados(self) -> int:
        return self.dias_trabalhados

    # Retorna o valor do salario definido pelo usuario para informar o usuario.
    def total_salario_bruto(self) -> float:
        return self.salario_mensal

    # Retorna a quantidade de horas definida para trabalhar por dia
    def max_hora_trabalho_dia(self) -> float:
        return self.horas_trabalhadas_dia

    # Quantos projetos é ideal para essa renda (usar um valor base para calcular a media ganho por projeto )


if __name__ == "__main__":

    renda = Config_salario(5000, 30, 16, 5.60)

    # Total de dias trabalhos no mês
    dias_trabalhados_total = renda.total_dias_trabalhados()
    print(f"Total de Dias Trabalhados: {dias_trabalhados_total}")

    # Total de horas trabalhadas no dia
    horas_trabalhadas_maxima = renda.max_hora_trabalho_dia()
    print(f"Total de horas maxima trabalhadas por dia: {horas_trabalhadas_maxima}")

    # Valor Salario Bruto definido
    salario_bruto = renda.total_salario_bruto()
    print(f"Salario bruto total: {salario_bruto}")
    print("-" * 50)

    # Valor Ganhos por Dia (Real / Dolar)
    real_dia = renda.salario_dia()["real_dia"]
    dolar_dia = renda.salario_dia()["dolar_dia"]

    print(f"Real: R$ {real_dia:.2f} | Dolar: $ {dolar_dia:.2f} / por dia")

    # Valor Ganhos por Hora (Real / Dolar)
    real_hora = renda.salario_hora()["real_hora"]
    dolar_hora = renda.salario_hora()["dolar_hora"]

    print(f"Real: R$ {real_hora:.2f} | Dolar: $ {dolar_hora:.2f} / por hora")

    # Valor Ganhos por Minutos (Real / Dolar)
    real_minuto = renda.salario_minuto()["real_minuto"]
    dolar_minuto = renda.salario_minuto()["dolar_minuto"]

    print(f"Real: R$ {real_minuto:.2f} | Dolar: $ {dolar_minuto:.2f} / por minuto")
    print()
