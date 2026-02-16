import os
def clear_view():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def jarak(spacing:int):
    for i in range(spacing):
        print("")