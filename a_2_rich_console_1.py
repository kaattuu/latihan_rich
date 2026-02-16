from tools import clear_view, jarak
clear_view()
jarak(4)


from rich.console import Console

console = Console()

data1 = "Hallo dunia...!"
data2 = "Sedang belajar..."
data3 = "Rich"
data4 = "Hallo dunia....! saya sedang belajar rich"
data5 = "Ini adalah teks percobaan saya...!"

console.print(f"{data1}", style="bold white on red", justify="center")
jarak(2)
console.print(f"{data2}", style="bold white on blue", justify="center")
jarak(2)
console.print(f"{data3}", style="bold white on yellow", justify="center")
jarak(2)
console.print(f"{data4}", style="bold", justify="center")
jarak(2)
console.print(f"{data4}", style="underline", justify="center")
jarak(2)
console.print(f"{data4}", style="reverse", justify="center")
jarak(2)
console.print(f"{data4}", style="italic", justify="center")
jarak(2)

console.print(
    f"{data5}", 
    style   = "bold red", 
    justify = "center"
    )



jarak(4)


