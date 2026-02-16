from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static, Button
from textual.containers import Container, Horizontal

class DashboardApp(App):
    """Aplikasi Dashboard Interaktif Sederhana."""
    
    # CSS di dalam Python untuk mengatur tampilan (mirip web design)
    CSS = """
    Screen {
        align: center middle;
    }

    #main_container {
        width: 60;
        height: 15;
        border: double $accent;
        padding: 1 2;
        background: $surface;
    }

    Input {
        margin: 1 0;
    }

    .pesan-selamat {
        content-align: center middle;
        color: $success;
        text-style: bold;
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        """Di sini kita menyusun struktur UI-nya."""
        yield Header(show_clock=True)
        
        with Container(id="main_container"):
            yield Static("Halo! Masukkan namamu di bawah ini:", id="label")
            yield Input(placeholder="Ketik nama di sini...", id="input_nama")
            yield Button("Update Dashboard", variant="primary", id="btn_update")
            yield Static("", id="hasil_output", classes="pesan-selamat")
            
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Logika saat tombol diklik."""
        input_widget = self.query_one("#input_nama", Input)
        output_widget = self.query_one("#hasil_output", Static)
        
        if input_widget.value:
            output_widget.update(f"Selamat Datang, {input_widget.value}!")
        else:
            output_widget.update("Silahkan isi nama dulu ya!")

if __name__ == "__main__":
    app = DashboardApp()
    app.run()