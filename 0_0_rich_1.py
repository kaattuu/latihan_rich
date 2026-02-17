from tools import clear_view, jarak
clear_view()
jarak(4)

# link materi :
# https://gemini.google.com/app/4c9a7e0ce71603b1?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all


# from rich import print
# from rich.console import Console
# from rich.panel import Panel
# from rich.columns import Columns
# import time
# from rich.progress import track
# from rich.progress import Progress
# from rich import inspect
# from rich.traceback import install
# import logging
# from rich.logging import RichHandler
# from rich.layout import Layout




# TAHAP 1 FONDASI & DASAR RICH

# # 1. rich print

# from rich import print

# # Mencetak string dengan warna

# print("[bold red]Halo Dunia![/bold red] Sedang belajar [green]Rich[/green].")

# jarak(2)





# # Mencetak struktur data (otomatis rapi dan berwarna)

# data_user = {
#     "id"    : 1, 
#     "nama"  : "Budi", 
#     "aktif" : True, 
#     "skor"  : [10, 20, 30]
#     }

# print(data_user)

# jarak(2)





# # 2. Objek Console (Pusat Kontrol)

# from rich.console import Console

# console = Console()

# # Menggunakan gaya yang lebih spesifik

# console.print("Teks ini rata tengah", style="bold white on blue", justify="center")

# jarak(2)





# # 3. Text Styling & Markup

# from rich.console import Console

# console = Console()

# console.print("Ini [bold italic yellow]penting[/]!")

# jarak(2)





# # Mari Kita Coba!

# from rich.console import Console
# from rich.panel import Panel

# console = Console()

# # Membuat tampilan penyambutan

# console.print(
#     Panel(
#         "[bold cyan]INSTALASI BERHASIL![/]\n[italic]Selamat datang di dunia terminal yang penuh warna.[/]",
#         title="[bold green]Sistem Konfirmasi[/]",
#         subtitle="v1.0"
#     )
# )

# jarak(2)





# # 2. Struktur Data & Kontainer

# # 1. Tables (Tabel)

# from rich.console import Console
# from rich.table import Table

# console = Console()

# # 1. Inisialisasi Tabel
# table = Table(title="Daftar Inventaris Gadget")

# # 2. Tambah Kolom (bisa diatur gaya teksnya)
# table.add_column("Nama Barang", style="cyan", no_wrap=True)
# table.add_column("Kategori", style="magenta")
# table.add_column("Harga", justify="right", style="green")

# # 3. Tambah Baris Data
# table.add_row("MacBook Pro M2", "Laptop", "Rp 25.000.000")
# table.add_row("iPhone 15 Pro", "Smartphone", "Rp 21.000.000")
# table.add_row("Logitech MX Master", "Aksesoris", "Rp 1.500.000")

# # 4. Tampilkan!
# console.print(table)

# jarak(2)





# # 2. Columns (Kolom)

# from rich.console import Console
# from rich.columns import Columns
# from rich.panel import Panel

# console = Console()

# # Daftar data contoh
# users = ["Budi Utama", "Siska Amanda", "Andi Wijaya", "Rina Rose", "Tono Jati"]

# # Kita bungkus tiap nama di dalam Panel kecil agar rapi
# user_renderables = [Panel(user, expand=False) for user in users]

# # Tampilkan secara berdampingan
# console.print(Columns(user_renderables))

# jarak(2)





# # 3. Panels (Panel)

# from rich.console import Console
# from rich.panel import Panel

# console = Console()

# pesan = "[bold yellow]PENGUMUMAN![/]\n\nServer akan maintenance pada jam [red]23:00 WIB[/]."

# # Panel dengan judul dan border yang berbeda-beda
# console.print(Panel(pesan, title="Sistem", subtitle="Info Penting", border_style="blue"))

# jarak(2)





# # 3. Visualisasi Progres & Status

# # 1. Status (Spinners)

# import time
# from rich.console import Console

# console = Console()

# # Menggunakan 'with' agar status otomatis berhenti jika kode selesai/error
# with console.status("[bold green]Sedang mengunduh data...[/]", spinner="dots"):
#     # Simulasi proses berat
#     time.sleep(10) 
#     console.log("Data berhasil diambil!")

# with console.status("[bold red]Menyimpan ke database...[/]", spinner="earth"):
#     time.sleep(10)
#     console.log("Database diperbarui.")

# jarak(2)





# # 2. Progress Bar (Loading Bar)

# import time
# from rich.progress import track

# # Cara paling sederhana menggunakan 'track'
# proses_belajar = ["Fondasi", "Struktur Data", "Progress Bar", "Advanced"]

# for materi in track(proses_belajar, description="[cyan]Belajar Rich..."):
#     time.sleep(5) # Simulasi waktu belajar tiap materi

# jarak(2)





# # 3. Advanced Progress (Custom Columns)

# from rich.progress import Progress
# import time

# with Progress() as progress:
#     task1 = progress.add_task("[red]Downloading...", total=100)
#     task2 = progress.add_task("[green]Processing...", total=100)
#     task3 = progress.add_task("[cyan]Installing...", total=100)

#     while not progress.finished:
#         progress.update(task1, advance=0.5)
#         progress.update(task2, advance=0.3)
#         progress.update(task3, advance=0.9)
#         time.sleep(0.02)

# jarak(2)





# 4. Alat Bantu Pengembangan (Dev Tools)

# # 1. Rich Inspect (Melihat Isi Objek)

# from rich import inspect

# # Misal kita punya daftar angka
# angka = [1, 2, 3]

# # Lihat atribut dan metode apa saja yang tersedia untuk list ini
# inspect(angka, methods=True)

# jarak(2)





# # 2. Rich Traceback (Error yang Cantik)

# from rich.traceback import install

# # Cukup panggil fungsi ini sekali di awal script kamu
# install(show_locals=True)

# # Mari kita buat error sengaja
# def bagi_nol():
#     angka = 10
#     pembagi = 0
#     return angka / pembagi

# bagi_nol()

# jarak(2)





# # 3. Rich Logging (Log Berwarna)

# import logging
# from rich.logging import RichHandler

# # Konfigurasi logging agar menggunakan RichHandler
# logging.basicConfig(
#     level="NOTSET",
#     format="%(message)s",
#     datefmt="[%X]",
#     handlers=[RichHandler()]
# )

# log = logging.getLogger("rich")

# log.info("Server berhasil dijalankan!")
# log.warning("Koneksi internet tidak stabil.")
# log.error("Gagal menyambung ke database!")

# jarak(2)





5. Fitur Lanjutan (Advanced)

# 1. Layout (Membangun Dashboard)

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()
layout = Layout()

# Membagi layar menjadi 3 bagian utama
layout.split_column(
    Layout(name="header", size=3),
    Layout(name="main"),
    Layout(name="footer", size=3)
)

# Membagi bagian 'main' menjadi kiri dan kanan
layout["main"].split_row(
    Layout(name="sidebar"),
    Layout(name="body", ratio=2) # Body lebih lebar 2x dari sidebar
)

# Mengisi konten
layout["header"].update(Panel("[bold yellow]DASHBOARD ADMIN v2.0[/]", style="blue"))
layout["sidebar"].update(Panel("Menu:\n1. Home\n2. Settings", title="Navigasi"))
layout["body"].update(Panel("Selamat datang di sistem utama.", title="Main View"))
layout["footer"].update(Panel("Status: [green]Online[/]", title="System Info"))

console.print(layout)

# jarak(2)





# # 2. Markdown (Membaca Dokumen)

# from rich.console import Console
# from rich.markdown import Markdown

# console = Console()

# markdown_text = """
# # Belajar Rich Python
# Rich adalah library Python untuk tulisan *rich* dan format visual di terminal.

# ## Fitur Unggulan:
# * **Tables**
# * **Progress Bars**
# * **Syntax Highlighting**

# > "Terminal tidak harus membosankan!"
# """

# md = Markdown(markdown_text)
# console.print(md)

# jarak(2)





# # 3. Syntax Highlighting (Pewarnaan Kode)

# from rich.console import Console
# from rich.syntax import Syntax

# console = Console()

# kode_python = """
# def sapa_dunia():
#     print("Halo dari Rich!")
# """

# # Memberi warna pada kode Python menggunakan tema 'monokai'
# syntax = Syntax(kode_python, "python", theme="monokai", line_numbers=True)
# console.print(syntax)

# jarak(2)





