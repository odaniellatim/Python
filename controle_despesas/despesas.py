
# definição dos valores a pagar (valores de exemplo).
qt_tenis_pintados: float = 20
aluguel: float = 2_048.44
cc_pf_nubank: float = 1_749.30
cc_pj_nubank: float = 84.55
cc_carrefour: float = 462.92
agua: float = 140.00
luz: float = 250
claro: float = 300
cnpj: float = 80.00

def math_soma(aluguel:float,
              cc_pf_nubank:float,
              cc_pj_nubank:float,
              cc_carrefour:float,
              agua:float,
              luz:float,
              claro:float,
              cnpj:float) -> list :  
    # valor usado para calcular o valor de emergencia.
    EMERGENCY = 1.9
      
    # resultado da soma dos valores
    total_aluguel = aluguel
    total_cc = cc_pf_nubank + cc_pj_nubank + cc_carrefour
    total_house = agua + luz + claro
    empresa = cnpj
    
    total = total_aluguel + total_cc + total_house + empresa
    
    margem = ( total * EMERGENCY ) / 100
    return [
        total_aluguel,
        total_cc,
        total_house,
        empresa,
        total, 
        margem, 
        total + margem
        ]
    
resultado_math = math_soma(aluguel, cc_pf_nubank, cc_pj_nubank, cc_carrefour, agua, luz, claro, cnpj)

print(f"Total Aluguel: R$ {round(resultado_math[0], 2)}")
print(f"Total Cartão: R$ {round(resultado_math[1], 2)}")
print(f"Total Casa: R$ {round(resultado_math[2], 2)}")
print(f"Total CNPJ: R$ {round(resultado_math[3], 2)}")
print("-" * 30 )
print(f"Valor total: R$ {round(resultado_math[6], 2)}")
print(f"Valor Emergencia: R$ {round(resultado_math[5], 2)}")
print(" " * 30)
print(f'Valor de cada tênis pintado: R$ {round(resultado_math[6] / qt_tenis_pintados, 2)}')