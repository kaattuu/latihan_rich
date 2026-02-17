from tools import clear_view, jarak
clear_view()
jarak(4)



"""
3. Text Styling & Markup
Rich menggunakan sistem markup yang mirip dengan tag HTML sederhana di dalam kurung siku [].
Warna   : [red], [blue], [hex code seperti #ff00ff]
Gaya    : [bold], [italic], [underline], [reverse] (tukar warna teks dan background).
Penutup : Gunakan [/] untuk mengakhiri gaya.
"""

from rich.console import Console

console = Console()

console.print("ini [bold italic yellow]penting[/]")

jarak(4)
