from tools import clear_view, jarak
clear_view()
jarak(4)

from rich.console import Console
from rich.panel import Panel

console = Console()

data1 = "PENGUMUMAN...!"
data2 = "Server akan maintenance pada jam"
data3 = "23:00 WIB"

console.print(
    Panel(
        f"[bold yellow]{data1}[/]\n\n{data2} [bold red]{data3}[/]",
        title = "[white]Sistem[/]",
        subtitle = "[white]Info Penting[/]",
        border_style = "green"
    )
)

jarak(4)
