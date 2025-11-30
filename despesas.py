
# definição dos valores a pagar (valores de exemplo).
qt_tenis_pintados = 20
aluguel = 2_048.44
cc_pf_nubank = 1_749.30
cc_pj_nubank = 84.55
cc_carrefour = 462.92
agua = 140.00
luz = 250
claro = 300

def math_soma(aluguel, cc_pf_nubank, cc_pj_nubank, cc_carrefour, agua, luz, claro) -> list :  
    # valor usado para calcular o valor de emergencia.
    EMERGENCY = 1.9
      
    # resultado da soma dos valores
    total_aluguel = aluguel
    total_cc = cc_pf_nubank + cc_pj_nubank + cc_carrefour
    total_house = agua + luz + claro
    
    total = total_aluguel + total_cc + total_house
    
    margem = ( total * EMERGENCY ) / 100
    return [
        total_aluguel,
        total_cc,
        total_house,
        total, 
        margem, 
        total + margem
        ]
    
resultado_math = math_soma(aluguel, cc_pf_nubank, cc_pj_nubank, cc_carrefour, agua, luz, claro)

print(f"Total Aluguel: R$ {round(resultado_math[0], 2)}")
print(f"Total Cartão: R$ {round(resultado_math[1], 2)}")
print(f"Total Casa: R$ {round(resultado_math[2], 2)}")
print("-" * 30 )
print(f"Valor total: R$ {round(resultado_math[3], 2)}")
print(f"Valor Emergencia: R$ {round(resultado_math[4], 2)}")
print(" " * 30)
print(f'Valor de cada tênis pintado: R$ {round(resultado_math[3] / qt_tenis_pintados, 2)}')