from tools import clear_view, jarak
clear_view()
jarak(4)


from rich import inspect

def inspectt(data, helps=None):
    if not helps:
        return inspect(data, methods=True)
    return inspect(data, methods=True, help=True)






from rich import print
data1 = "Halo Dunia!"
data2 = "Sedang belajar..."
data3 = "Rich"
cetak = f"[bold red]{data1}[/] {data2} [green]{data3}[/]"

# inspectt(cetak)






from rich.console import Console
console = Console()

# inspectt(console)

