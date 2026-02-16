from textual.app import App, ComposeResult
from textual.widgets import DataTable, Input, Header, Footer, Static

class KasirApp(App):
    BINDINGS = [("f1", "bayar", "Bayar (F1)"), ("f2", "batal", "Batal (F2)")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Scan Barcode / Kode Barang...")
        yield DataTable() # Tabel daftar belanjaan
        yield Static("TOTAL: Rp 0", id="total_display")
        yield Footer()

    def action_bayar(self):
        # Logika ketika tombol F1 ditekan
        self.notify("Memproses Pembayaran...")

if __name__ == "__main__":
    KasirApp().run()