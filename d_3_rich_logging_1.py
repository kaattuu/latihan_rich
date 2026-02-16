from tools import clear_view, jarak
clear_view()
jarak(4)


import logging
from rich.logging import RichHandler

logging.basicConfig(
    level    = "NOTSET",
    format   = "%(message)s",
    datefmt  = "[%X]",
    handlers = [RichHandler()]
)

log = logging.getLogger("rich")

log.debug("detail informasi spesifik")
log.info("server berhasil dijalankan")
log.warning("koneksi internet tidak stabil")
log.error("gagal menyambung ke database!")
log.critical("ini pesan benar benar genting!")