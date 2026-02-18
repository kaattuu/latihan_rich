from tools import clear_view, jarak, inspectt
clear_view()
jarak(4)

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

console = Console()

users = ["Budi Utama", "Siska Amanda", "Andi Wijaya", "Rina Nose", "Tono Jati"]

user_renderables = [Panel(user, expand=False) for user in users]

console.print(Columns(user_renderables))

jarak(4)

inspectt(user_renderables)

jarak(4)
