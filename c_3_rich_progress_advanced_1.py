from tools import clear_view, jarak
clear_view()
jarak(4)


import time
from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("Downloading...", total=100)
    task2 = progress.add_task("Processinng...", total=100)
    task3 = progress.add_task("Installiing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)

jarak(4)
