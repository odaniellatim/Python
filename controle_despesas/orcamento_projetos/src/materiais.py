from src.unidades_medida import UnidadeMedida

class Materiais:
    def __init__(self,material_id: int, material_nome: str, material_valor:float, material_quantidade: int, material_unidade_medida: UnidadeMedida, material_qntd_usado_projeto: float) -> None:
        self.material_id: int = material_id
        self.material_nome: str = material_nome
        self.material_valor: float = material_valor
        self.material_quantidade: int = material_quantidade
        self.material_unidade_medida: UnidadeMedida = material_unidade_medida
        self.material_qntd_usado_projeto: float = material_qntd_usado_projeto
        self.OZ = 28.34


    def mt_preco_por_unidade_medida(self, material_unidade_medida: UnidadeMedida) -> float:
        ValorZero = 0.00
        
        match(material_unidade_medida):

            case UnidadeMedida.LITRO:
                transformar_em_ml = self.material_quantidade * 1000
                valor_total_material_por_l = self.material_valor / transformar_em_ml
                return valor_total_material_por_l

            case UnidadeMedida.MILILITRO:
                valor_total_material_por_ml = self.material_valor / self.material_quantidade
                return valor_total_material_por_ml
            
            case UnidadeMedida.METRO:
                ...
                
            case UnidadeMedida.CENTIMETRO:
                ...
            
            case UnidadeMedida.UNIDADE:
                valor_total_material_por_inid = self.material_valor / self.material_quantidade
                return valor_total_material_por_inid
            
            case UnidadeMedida.KILO:
                transformar_em_kg = self.material_quantidade * 1000
                valor_total_material_por_kg = self.material_valor / transformar_em_kg
                return valor_total_material_por_kg
            
            case UnidadeMedida.GRAMA:
                valor_total_material_por_g = self.material_valor / self.material_quantidade
                return valor_total_material_por_g
            
            case UnidadeMedida.ONCA:
                transformar_em_oz = self.material_quantidade * self.OZ
                valor_total_material_por_oz = self.material_valor / transformar_em_oz
                return valor_total_material_por_oz
            
            case _:
                return False
        
        return ValorZero

    def mt_valor_qntd_usado_projeto(self):
        valor_por_unidade_medida = self.mt_preco_por_unidade_medida(self.material_unidade_medida)
        if(valor_por_unidade_medida != 0):
            total = self.material_qntd_usado_projeto * valor_por_unidade_medida
            return total
        else:
            raise ValueError(f"Valor informado não foi possivel realizar o calculo")

    # Lista o material cadastrado em formato de dicionario
    @property
    def mt_lista_cadastrados(self) -> dict:
        return {
            "material_id": self.material_id,
            "nome_material": self.material_nome,
            "preco_material": self.material_valor,
            "quantidade_material": self.material_quantidade,
            "unidade_medida": self.material_unidade_medida,
            "qntd_material_usado": self.material_qntd_usado_projeto,
        }
        # print("-" * 100)
        # print(" " * 100)
        # print(f"ID material: {self.material_id}")
        # print(f"Nome material: {self.material_nome}")
        # print(f"Preço material: R$ {self.material_valor}")    
        # print(f"Quantidade: {self.material_quantidade}/{self.material_unidade_medida}")  
        # print(f"Qntd material usado: {self.material_qntd_usado_projeto}/{self.material_unidade_medida}")
        # print(" " * 100)
        # print(f"Preço por {self.material_unidade_medida}: R$ {self.material_valor_por_qntd(self.material_unidade_medida):.2f}")
        # print(f"Preço de {self.material_qntd_usado_projeto}/{self.material_unidade_medida}: R$ {self.material_valor_total_qntd_usado_projeto():.2f}")
        # print(" " * 100)


if __name__ == "__main__":
   
    material = Materiais(1, "Tinta Branca", 33.33, 90, 'ml', 10)
    print( material.mt_preco_por_unidade_medida('ml')) # Lista o valor do material por qntd (ml).
    print(material.mt_lista_cadastrados) # Lista o material cadastrado em formato de um dicionario.
