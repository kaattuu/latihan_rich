import os
from rich import inspect



def clear_view():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def jarak(spacing:int):
    for i in range(spacing):
        print("")


def inspectt(data, helps=None):
    if not helps:
        return inspect(data, methods=True)
    return inspect(data, methods=True, help=True)