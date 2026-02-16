from tools import clear_view, jarak
clear_view()
jarak(4)

import time
from rich.console import Console

console = Console()

data1 = "Sedang mengunduh data...."
data2 = "Data berhasil diambil!"
data3 = "Menyimpan ke database...."
data4 = "Database diperbaharui."

with console.status(f"[bold green]{data1}[/]", spinner_style="bold bright_yellow", spinner="dots"):     # dots, moon, clock, bouncingBall, heart.
    time.sleep(5)
    console.log(f"{data2}")

with console.status(f"[bold red]{data3}[/]", spinner_style="bold bright_green", spinner="dots"):      # dots, moon, clock, bouncingBall, heart.
    time.sleep(5)
    console.log(f"{data4}")


jarak(4)



# 1. Kategori "Waktu & Proses"
# Cocok untuk simulasi proses loading yang memakan waktu.
# clock           : Jarum jam yang berputar.
# earth           : Animasi bumi berputar (keren untuk proses download/upload).
# moon            : Fase-fase bulan.

# 2. Kategori "Bentuk Geometris"
# Cocok untuk tampilan dashboard yang bersih.
# bouncingBar     : Batang yang memantul ke kiri dan kanan.
# bouncingBall    : Bola yang memantul.
# pipe            : Garis vertikal yang berputar.
# simpleDots      : Versi titik yang lebih sederhana dari dots.

# 3. Kategori "Unik & Menarik"
# hearts          : Simbol hati yang berdetak.
# monkey          : Animasi monyet (lucu untuk aplikasi yang santai).
# aesthetic       : Garis-garis yang bergerak halus.
# runner          : Karakter yang terlihat seperti sedang berlari.

# Cara Mengecek Semua Daftar Spinner
# python -m rich.spinner
# 'aesthetic'    ▰▰▰▱▱▱▱ 
# 'aesthetic'    ▰▰▱▱▱▱▱ 
# 'aesthetic'    ▰▰▰▱▱▱▱ 
# 'aesthetic'    ▰▰▰▰▱▱▱ 
# 'aesthetic'    ▰▰▰▰▰▰▱ 
# 'aesthetic'    ▰▰▰▰▰▰▰ 
# 'aesthetic'    ▰▱▱▱▱▱▱ 
# 'aesthetic'    ▰▱▱▱▱▱▱ 
# 'aesthetic'    ▰▱▱▱▱▱▱ 
# 'aesthetic'    ▰▱▱▱▱▱▱ 
# 'aesthetic'    ▰▰▱▱▱▱▱ 
# 'aesthetic'    ▰▰▰▰▱▱▱ 
# 'aesthetic'    ▰▰▰▰▰▰▱ 
# 'aesthetic'    ▰▰▰▰▰▱▱ 
# 'aesthetic'    ▰▰▰▰▰▰▰ 
# 'aesthetic'    ▰▰▰▰▰▰▱ 
# 'aesthetic'    ▰▰▰▰▰▰▰ 
# 'arc'           ◟ 
# 'arrow'         ↗ 
# 'arrow2'       ⬅️  
# 'arrow3'       ▸▹▹▹▹ 
# 'balloon'      . 
# 'balloon2'     ° 
# 'betaWave'     βββββρβ 
# 'bounce'            ⠂ 
# 'bouncingBall'     (     ●) 
# 'bouncingBar'      [=   ] 
# 'boxBounce'         ▘ 
# 'boxBounce2'       ▄ 
# 'christmas'         🌲 
# 'circle'            ⊙ 
# 'circleHalves'     ◒ 
# 'circleQuarters'   ◷ 
# 'clock'             🕚  
# 'dots'              ⠼ 
# 'dots10'            ⡐ 
# 'dots11'            ⡀ 
# 'dots12'       ⠀    ⢀ 
# 'dots2'             ⣯ 
# 'dots3'             ⠖ 
# 'dots4'             ⠇ 
# 'dots5'             ⠚ 
# 'dots6'             ⠴ 
# 'dots7'             ⠦ 
# 'dots8'             ⠒ 
# 'dots8Bit'          ⠶ 
# 'dots9'             ⡗ 
# 'dqpb'              b 
# 'earth'             🌍  
# 'flip'              ' 
# 'grenade'          
# 'growHorizontal'    ▎ 
# 'growVertical'      ▃ 
# 'hamburger'         ☴ 
# 'hearts'            💙  
# 'layer'             - 
# 'line'              | 
# 'line2'             - 
# 'material'          ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█████ 
# 'monkey'            🙊  
# 'moon'              🌗  
# 'noise'             ░ 
# 'pipe'              └ 
# 'point'             ∙∙● 
# 'pong'              ▐       ⠂▌ 
# 'runner'            🏃  
# 'shark'             ▐______/|______▌ 
# 'simpleDots'        ... 
# 'simpleDotsScrolling'          
# 'smiley'            😝  
# 'squareCorners'    ◳ 
# 'squish'            ╪ 
# 'star'              ✶ 
# 'star2'             * 
# 'toggle'            ⊶ 
# 'toggle10'          ㊁ 
# 'toggle11'          ⧆ 
# 'toggle12'          ☖ 
# 'toggle13'          - 
# 'toggle2'           ▫ 
# 'toggle3'           ■ 
# 'toggle4'           ▫ 
# 'toggle5'           ▯ 
# 'toggle6'           ၀ 
# 'toggle7'           ⦾ 
# 'toggle8'           ◌ 
# 'toggle9'           ◎ 
# 'triangle'          ◥ 
# 'weather'           🌨  

