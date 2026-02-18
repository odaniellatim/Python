import os
from interface_menu import Interface_menu

def load_data():
    file = "usuarios.json"
    dir = "controle_despesas/controle_1.0/BD/"
    full_dir = os.path.join(dir, file)
    
    if not(os.path.exists(full_dir)):
        return True
    else:
        return False
                

# Codigo de teste das classes
if __name__ == "__main__":
    init = Interface_menu()
    if(load_data()):
        while(True):   
            init.menu_inicial()
    else:
        while(True):
            init.user_logado()





