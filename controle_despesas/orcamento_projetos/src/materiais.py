from .unidades_medida import UnidadeMedida

class Materiais:

    def __init__(self,material_id: int, material_nome: str, material_valor:float, material_quantidade: int, material_unidade_medida: UnidadeMedida, material_qntd_usado_projeto: float) -> None:
        self.material_id: int = material_id
        self.material_nome: str = material_nome
        self.material_valor: float = material_valor
        self.material_quantidade: int = material_quantidade
        self.material_unidade_medida: UnidadeMedida = material_unidade_medida
        self.material_qntd_usado_projeto: float = material_qntd_usado_projeto
        self.OZ = 28.34

    def material_valor_por_qntd(self, material_unidade_medida: UnidadeMedida) -> float:
        ValorZero = 0.00
        
        match(material_unidade_medida):

            case UnidadeMedida.LITRO:
                transformar_em_ml = self.material_quantidade * 1000
                valor_total_material_por_ml = self.material_valor / transformar_em_ml
                return round(valor_total_material_por_ml,2)
            
            case UnidadeMedida.MILILITRO:
                valor_total_material_por_ml = self.material_valor / self.material_quantidade
                return round(valor_total_material_por_ml,2)
            
            case UnidadeMedida.METRO:
                ...

            case UnidadeMedida.CENTIMETRO:
                ...

            case UnidadeMedida.UNIDADE:
                valor_total_material_por_g = self.material_valor / self.material_quantidade
                return round(valor_total_material_por_g,2)
            
            case UnidadeMedida.KILO:
                transformar_em_g = self.material_quantidade * 1000
                valor_total_material_por_g = self.material_valor / transformar_em_g
                return round(valor_total_material_por_g,2)
            
            case UnidadeMedida.GRAMA:
                valor_total_material_por_g = self.material_valor / self.material_quantidade
                return round(valor_total_material_por_g,2)
            
            case UnidadeMedida.ONCA:
                
                transformar_em_g = self.material_quantidade * self.OZ
                valor_total_material_por_oz = self.material_valor / transformar_em_g
                return round(valor_total_material_por_oz,2)
        
        return ValorZero

    def material_valor_total_qntd_usado_projeto(self):
        
        valor_por_unidade_medida = self.material_valor_por_qntd(self.material_unidade_medida)
        
        if(valor_por_unidade_medida != 0):
            total = self.material_qntd_usado_projeto * valor_por_unidade_medida
            return total
        else:
            raise ValueError(f"Valor informado não foi possivel realizar o calculo")
        
    def material_lista_cadastrados(self):
        print("-" * 100)
        print(" " * 100)
        print(f"ID material: {self.material_id}")
        print(f"Nome material: {self.material_nome}")
        # print(f"Unidade Medida: {self.material_unidade_medida}")
        print(f"Preço material: R$ {self.material_valor}")    
        print(f"Quantidade: {self.material_quantidade}/{self.material_unidade_medida}")  
        print(f"Qntd material usado: {self.material_qntd_usado_projeto}/{self.material_unidade_medida}")
        print(" " * 100)
        print(f"Preço por {self.material_unidade_medida}: R$ {self.material_valor_por_qntd(self.material_unidade_medida):.2f}")
        print(f"Preço de {self.material_qntd_usado_projeto}/{self.material_unidade_medida}: R$ {self.material_valor_total_qntd_usado_projeto():.2f}")
        print(" " * 100)
