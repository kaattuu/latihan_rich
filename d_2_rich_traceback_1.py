from tools import clear_view, jarak
clear_view()
jarak(4)


from rich.traceback import install

install(show_locals=True)

def bagi_nol():
    angka   = 10
    pembagi = 0
    return angka/pembagi


bagi_nol()


jarak(4)