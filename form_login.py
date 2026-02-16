import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def tampilkan_header():
    """Versi yang diperbaiki: justify dipindah ke console.print"""
    header_text = "[bold cyan]SISTEM AKSES TERPUSAT[/]\n[italic white]Silakan masukkan kredensial Anda[/]"
    
    # Perbaikan: justify ada di sini, bukan di dalam Panel()
    console.print(
        Panel(header_text, style="bold blue", expand=False), 
        justify="center"
    )

def proses_login():
    tampilkan_header()

    # Input menggunakan Rich Prompt
    username = Prompt.ask("[bold yellow]Username[/]")
    password = Prompt.ask("[bold yellow]Password[/]", password=True)

    with console.status("[bold green]Memverifikasi...[/]", spinner="bouncingBar"):
        time.sleep(1.5)

    if username == "admin" and password == "rahasia":
        console.print("\n[bold green]✔ Akses Diterima![/]\n")
        
        # Dashboard sederhana
        table = Table(title="Status Sistem")
        table.add_column("Layanan", style="cyan")
        table.add_column("Status", style="green")
        table.add_row("Database", "Online")
        table.add_row("Server", "Active")
        
        console.print(Panel(table, border_style="green", expand=False))
    else:
        console.print("\n[bold red]✘ Username/Password Salah![/]\n")

if __name__ == "__main__":
    console.clear()
    proses_login()