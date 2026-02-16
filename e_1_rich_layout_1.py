from tools import clear_view, jarak
clear_view()

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()
layout  = Layout()

layout.split_column(
    Layout(name="header", size=3),
    Layout(name="main"),
    Layout(name="footer", size=3)
)

layout["main"].split_row(
    Layout(name="sidebar"),
    Layout(name="body", ratio=2)
)

layout["header"].update(Panel("[bold yellow]DASHBORD ADMIN v2.0[/]", style="blue"))
layout["sidebar"].update(Panel("Menu:\n1. Home\n2. Settings", title="Navigasi"))
layout["body"].update(Panel("Selamat datang di sistem utama.", title="Main View"))
layout["footer"].update(Panel("status: [green]Online[/]", title="System Info"))

console.print(layout)