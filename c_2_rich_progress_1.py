from tools import clear_view, jarak
clear_view()
jarak(4)


import time
from rich.progress import track

proses_belajar = ["Fondasi", "Struktur Data", "Progress Bar", "Advanced"]

for materi in track(proses_belajar, description="[bright_green]Belajar Rich..."):
    time.sleep(5)

jarak(4)
