import time
import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_roleta_minimalista():
    simbolos = ["●", "♦", "♠", "♥", "♣", "★", "⭐", "🎯", "🎰", "💰"]
    cores = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    reset = "\033[0m"
    
    print("🎰 Roleta Girando... 🎰\n")
    
    for i in range(25):
        limpar_tela()
        
        # Gerar display aleatório
        display = []
        for _ in range(5):
            simbolo = random.choice(simbolos)
            cor = random.choice(cores)
            display.append(f"{cor}{simbolo}{reset}")
        
        print("╔══════════════════╗")
        print("║                  ║")
        print(f"║    {' '.join(display)}    ║")
        print("║                  ║")
        print("╚══════════════════╝")
        print(f"\nGirando... {i+1}/25")
        
        time.sleep(0.08)
    
    # Resultado final
    resultado = random.randint(0, 36)
    cor = "\033[92m" if resultado == 0 else "\033[91m" if resultado % 2 == 1 else "\033[94m"
    
    limpar_tela()
    print("╔══════════════════╗")
    print("║                  ║")
    print(f"║      {cor}{resultado:02d}{reset}       ║")
    print("║                  ║")
    print("╚══════════════════╝")
    print(f"\n🎉 Resultado: {resultado} 🎉")
    
    return resultado

# Executar
animacao_roleta_minimalista()