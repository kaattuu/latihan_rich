from tools import clear_view, jarak
clear_view()

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()
layout  = Layout()

layout.split_column(
    Layout(name = "header", size = 3),
    Layout(name = "main"),
    Layout(name = "footer", size = 3)
)

layout["main"].split_row(
    Layout(name = "sidebar"),
    Layout(name = "body", ratio = 9)
)

head1 = "[bold yellow]DASBOARD ADMIN v2.0.0[/]"
layout["header"].update(Panel(f"{head1}", style="bright_green"))


side1 = "[white]Menu\n1. Home\n2. Settings\n3. Contact\n4. ....[/]"
layout["sidebar"].update(Panel(f"{side1}", title="Navigasi", style="bright_yellow"))


body1 = "Selamat datang di sistem utama"
layout["body"].update(Panel(f"{body1}", title="Main View", style="bright_yellow"))

foot1 = "[white]Status: [/]"
foot2 = "[bright_green]Online[/]"
layout["footer"].update(Panel(f"{foot1}{foot2}", title="System Info", style="green"))

console.print(layout)