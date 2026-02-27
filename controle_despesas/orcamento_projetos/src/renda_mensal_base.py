class RendaMensalBase:
    def __init__(self, renda_mensal_real: float, renda_dias_trabalhados: int, renda_horas_trabalhadas_dia:int ) -> None:
        self.renda_mensal_real = renda_mensal_real
        self.renda_dias_trabalhados: int = renda_dias_trabalhados
        self.renda_horas_trabalhadas_dia: int = renda_horas_trabalhadas_dia

    @property
    def renda_valor_hora_real(self):
        renda_hora = self.renda_mensal_real / (self.renda_dias_trabalhados * self.renda_horas_trabalhadas_dia)
        return round(renda_hora, 4)
    
    @property
    def renda_valor_minuto_real(self):
        renda_minuto = self.renda_valor_hora_real / 60
        return round(renda_minuto, 4)
    

