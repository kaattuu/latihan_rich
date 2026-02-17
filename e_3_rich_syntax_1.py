from tools import clear_view, jarak
clear_view()
jarak(4)


from rich.console import Console
from rich.syntax import Syntax

console = Console()

kode_python = """
def sapa_dunia():
    print("Halo dari Rich!")
"""

syntax = Syntax(kode_python, "python", theme="monokai", line_numbers=True)

console.print(syntax)

jarak(4)
