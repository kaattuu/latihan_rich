from tools import clear_view, jarak
clear_view()
jarak(5)


from rich import print

data1 = "Halo Dunia!"
data2 = "Sedang belajar..."
data3 = "Rich"

cetak = f"[bold red]{data1}[/] {data2} [green]{data3}[/]"

print(cetak)

jarak(5)

data_user = {
    "id"    : 1,
    "nama"  : "AbuCom",
    "aktif" : True,
    "skor"  : [10, 20, 30]
}

print(data_user)

jarak(5)
