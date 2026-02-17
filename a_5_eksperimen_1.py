from tools import clear_view, jarak
clear_view()
jarak(5)


from rich.console import Console
from rich.panel import Panel

console = Console()

# console
console.print("Teks ini rata tengah", style="bold white on blue", justify="center")


jarak(2)


# text styling
console.print("ini [bold italic yellow]penting[/]")


jarak(2)


# console vs text styling
console.print("[bold]ini gabungan console vs text styling[/]", style="on green", justify="center")


jarak(2)


# kombinasi dengan panel
console.print(
    Panel(
        "[bold cyan]INSTALASI BERHASIL![/]\n[italic]Selamat datang di dunia terminal yang penuh warna.[/]",
        title="[bold green]Sistem Konfirmasi[/]",
        subtitle="v1.0"
    )
)






jarak(5)
