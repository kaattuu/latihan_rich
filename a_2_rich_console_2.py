from tools import clear_view, jarak
clear_view()
jarak(4)

from rich.console import Console
from rich.panel import Panel

console = Console()

data1 = "INSTALASI BERHASIL...!"
data2 = "Selamat datang di dunia terminal yang penuh warna."
data3 = "Sistem Konfirmasi"
data4 = "v1.0.0"

console.print(
    Panel(
        f"[bold cyan]{data1}[/]\n[italic]{data2}[/]",
        title    = f"[bold green]{data3}[/]",
        subtitle = f"{data4}"
    )
)

jarak(4)
