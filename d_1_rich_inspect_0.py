from tools import clear_view, jarak
clear_view()
jarak(4)

from rich import inspect

# angka = [1, 2, 3]

# # Lihat atribut dan metode apa saja yang tersedia untuk list ini
# inspect(angka, methods=True)

# jarak(4)

# # Tip: Tambahkan help=True jika ingin melihat penjelasan singkat dari setiap fungsi di dalam objek tersebut.
# inspect(angka, methods=True, help=True)

jarak(4)

data1 = (1, 2, 3, 4, 3, 5, 3, 6, 3, 3, "abu", "abu")
data2 = {1, 2, 3}
data3 = [1, 2, 3]
data4 = {"nama": "AbuCom", "status": "developer pemula"}
data5 = "Abucom"
data6 = 1

# inspect(data1, methods=True)
# inspect(data1, methods=True, help=True)

# jarak(1)
# print(f"count: {data1.count(3)}")
# print(f"index: {data1.index(3)}")

# inspect(data2, methods=True)
inspect(data3, methods=True)
# inspect(data4, methods=True)
# inspect(data5, methods=True)
# inspect(data6, methods=True)


jarak(4)
