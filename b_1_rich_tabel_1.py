from tools import clear_view, jarak, inspectt
clear_view()
jarak(4)

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

console = Console()

tabel   = Table(
    title   = "Daftar Inventaris Gadget", 
    box     = box.SQUARE,
    border_style = "bright_yellow"
    ) 

tabel.add_column(Text("Nama Barang", justify="center"), style="cyan", no_wrap=True)
tabel.add_column(Text("Kategori", justify="center"), style="magenta")
tabel.add_column(Text("Harga", justify="center"), justify="right", style="green", header_style="bold white")

tabel.add_row("MackBook Pro M2", "Laptop", "25.000.000")
tabel.add_row("iPhone 15 Pro", "Smartphone", "21.000.000")
tabel.add_row("Logitech MX Master", "Aksesoris", "1.500.000")

console.print(tabel)

jarak(4)


# Pilihan Gaya Garis (box) yang Tersedia:
# Nama              Box,Deskripsi
# box.HEAVY,        Garis tebal (Bold)
# box.DOUBLE,       Garis ganda/double
# box.SQUARE,       Garis tipis dengan sudut siku
# box.ROUNDED,      Garis tipis dengan sudut tumpul/bulat
# box.ASCII,        "Menggunakan karakter jadul (+, -,"
# box.HEAVY_HEAD,   Garis tebal hanya di bagian Header saja
# box.MINIMAL,      "Tanpa garis luar, hanya garis pemisah kolom"

# inspectt(tabel)

jarak(4)
