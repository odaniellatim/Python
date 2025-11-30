
# definição dos valores a pagar.
qt_tenis_pintados = 20
aluguel = 2_048.44
cc_pf_nubank = 1_749.30
cc_pj_nubank = 84.55
cc_carrefour = 462.92
agua = 140.00
luz = 250
claro = 300

def math_soma(aluguel, cc_pf_nubank, cc_pj_nubank, cc_carrefour, agua, luz, claro):
    # valor usado para calcular o valor de emergencia.
    EMERGENCY = 1.9
      
    # resultado da soma dos valores
    total = aluguel + cc_pf_nubank + cc_pj_nubank + cc_carrefour + agua + luz + claro
    margem = ( total * EMERGENCY ) / 100
    return [total, margem, total+margem]
    
resultado_math = math_soma(aluguel, cc_pf_nubank, cc_pj_nubank, cc_carrefour, agua, luz, claro)

    
print(f"Valor total: R$ {round(resultado_math[2], 2)}")
print(f"Valor Emergencia: R$ {round(resultado_math[1], 2)}")
print(f'Valor de cada tênis pintado: R$ {round(resultado_math[2] / qt_tenis_pintados, 2)}')