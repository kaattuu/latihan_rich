from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Input, Static, Label
from textual.containers import Container, Horizontal, Vertical

# Data barang sederhana (Anggap saja ini dari Database)
DATABASE_BARANG = {
    "101": {"nama": "Kopi Susu", "harga": 5000},
    "102": {"nama": "Roti Bakar", "harga": 12000},
    "103": {"nama": "Teh Manis", "harga": 3000},
    "104": {"nama": "Susu Jahe", "harga": 7000},
}

class AplikasiKasir(App):
    TITLE = "SISTEM KASIR MODERN"
    BINDINGS = [
        ("f1", "bayar", "Bayar (F1)"),
        ("f2", "clear", "Hapus Semua (F2)"),
        ("q", "quit", "Keluar")
    ]
    
    CSS = """
    Screen {
        background: $surface;
    }
    #layout_utama {
        layout: grid;
        grid-size: 2;
        grid-columns: 3fr 1fr;
    }
    #area_input {
        margin: 1;
        padding: 1;
        border: tall $accent;
    }
    #total_panel {
        background: $primary-darken-2;
        color: white;
        text-align: center;
        text-style: bold;
        height: 5;
        content-align: center middle;
        margin: 1;
        border: heavy $success;
    }
    DataTable {
        height: 1fr;
        margin: 1;
    }
    """

    total_belanja = 0

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="layout_utama"):
            with Vertical():
                # Hapus expand=True di bawah ini
                with Horizontal(id="area_input"): 
                    yield Label("SCAN BARANG: ")
                    yield Input(placeholder="Masukkan kode barang (101-104)...", id="input_kode")
                
                yield DataTable(zebra_stripes=True)
            
            with Vertical():
                yield Static("TOTAL HARGA", id="label_total") # ganti classes jadi id jika perlu
                yield Static("Rp 0", id="total_display")
        
        yield Footer()

    def on_mount(self) -> None:
        """Inisialisasi tabel saat aplikasi dibuka."""
        table = self.query_one(DataTable)
        table.add_columns("Kode", "Nama Barang", "Harga Satuan", "Total")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Aksi saat user menekan ENTER di kolom input."""
        kode = event.value.strip()
        table = self.query_one(DataTable)
        display_total = self.query_one("#total_display", Static)

        if kode in DATABASE_BARANG:
            barang = DATABASE_BARANG[kode]
            # Tambah ke tabel
            table.add_row(
                kode, 
                barang["nama"], 
                f"Rp {barang['harga']:,}", 
                f"Rp {barang['harga']:,}"
            )
            
            # Update Total
            self.total_belanja += barang["harga"]
            display_total.update(f"Rp {self.total_belanja:,}")
            
            # Kosongkan input kembali
            event.input.value = ""
        else:
            self.notify("Barang Tidak Ditemukan!", severity="error")
            event.input.value = ""

    def action_bayar(self):
        """Logika saat tombol F1 ditekan."""
        if self.total_belanja > 0:
            self.notify(f"Pembayaran Berhasil: Rp {self.total_belanja:,}")
            self.action_clear()
        else:
            self.notify("Belum ada barang yang di-scan", severity="warning")

    def action_clear(self):
        """Reset aplikasi (F2)."""
        self.total_belanja = 0
        self.query_one(DataTable).clear()
        self.query_one("#total_display").update("Rp 0")
        self.notify("Data dibersihkan")

if __name__ == "__main__":
    AplikasiKasir().run()