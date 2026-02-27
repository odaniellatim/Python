from .renda_mensal_base import RendaMensalBase

class MaoDeObra:
    def __init__(self, mao_de_obra_porcentagem: int, mao_de_obra_horas_trabalhadas: int, mao_de_obra_minutos_trabalhados: int, mao_de_obra_taxa_de_urgencia: float = 0) -> None:
        self._mao_de_obra_porcentagem: int = mao_de_obra_porcentagem
        self._mao_de_obra_horas_trabalhadas: int = mao_de_obra_horas_trabalhadas
        self._mao_de_obra_minutos_trabalhados: int = mao_de_obra_minutos_trabalhados
        self._mao_de_obra_taxa_de_urgencia: float = mao_de_obra_taxa_de_urgencia
        self.renda_mensal: list[RendaMensalBase] = []

    @property
    def mao_de_obra_porcentagem(self) -> int:
        return self._mao_de_obra_porcentagem
    
    @property
    def mao_de_obra_horas_trabalhadas(self) -> float:
        valor_hora = 0.0
        for renda in self.renda_mensal:
            valor_hora = renda.renda_valor_hora_real  * self._mao_de_obra_horas_trabalhadas
            return round(valor_hora, 4)
        return round(valor_hora, 4)
    
    @property
    def mao_de_obra_minutos_trabalhados(self) -> float:
        valor_minuto = 0.0
        for renda in self.renda_mensal:
            valor_minuto = renda.renda_valor_minuto_real * self._mao_de_obra_minutos_trabalhados
            return round(valor_minuto, 4)
        return round(valor_minuto, 4)
    
    @property
    def mao_de_obra_taxa_de_urgencia(self) -> float:
        return self._mao_de_obra_taxa_de_urgencia

    # Valor da hora trabalhada com base na renda mensal
    @property
    def renda_mensal_hora_real(self):
        """ Valor da hora trabalhada calculado com base na renda mensal. Retorna o primeiro valor encontrado. """
        valor_hora = 0.0
        for renda in self.renda_mensal:
            valor_hora = renda.renda_valor_hora_real # pega o primeiro valor
            return valor_hora
        return valor_hora
    
    # Valor da minuto trabalhado com base na renda mensal
    @property
    def renda_mensal_minuto_real(self):
        """ Valor da minuto trabalhada calculado com base na renda mensal. Retorna o primeiro valor encontrado. """
        valor_minuto = 0.0
        for renda in self.renda_mensal:
            valor_minuto = renda.renda_valor_minuto_real
            return valor_minuto
        return valor_minuto
    

if __name__ == "__main__":
    md = MaoDeObra(150, 6, 45, 0)

    print(f"Hora: {md.renda_mensal_hora_real}")
    print(f"Minuto: {md.renda_mensal_minuto_real}")

    print("" * 100)
    print(f"MDO Hora: {md.mao_de_obra_horas_trabalhadas}")
    print(f"MDO Minuto: {md.mao_de_obra_minutos_trabalhados}")
    print(f"MDO Urgencia: {md.mao_de_obra_taxa_de_urgencia}")