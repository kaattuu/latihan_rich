from tools import clear_view, jarak
clear_view()
jarak(4)

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text

console = Console()

table   = Table(
    title   = "Daftar Inventaris Gadget", 
    box     = box.SQUARE,
    border_style = "bright_yellow"
    ) 

table.add_column(Text("Nama Barang", justify="center"), style="cyan", no_wrap=True)
table.add_column(Text("Kategori", justify="center"), style="magenta")
table.add_column(Text("Harga", justify="center"), justify="right", style="green", header_style="bold white")

table.add_row("MackBook Pro M2", "Laptop", "25.000.000")
table.add_row("iPhone 15 Pro", "Smartphone", "21.000.000")
table.add_row("Logitech MX Master", "Aksesoris", "1.500.000")

console.print(table)

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
