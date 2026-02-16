import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QPushButton, QTableWidget, 
                             QTableWidgetItem, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class KasirPyQt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem Kasir Modern - PyQt6")
        self.resize(800, 600)
        self.total_belanja = 0
        self.database = {
            "101": {"nama": "Kopi Susu", "harga": 5000},
            "102": {"nama": "Roti Bakar", "harga": 12000},
        }
        self.init_ui()

    def init_ui(self):
        # Widget Utama
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Header
        header = QLabel("KASIR DESKTOP")
        header.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Input Area
        input_layout = QHBoxLayout()
        self.input_kode = QLineEdit()
        self.input_kode.setPlaceholderText("Masukkan Kode Barang lalu Enter...")
        self.input_kode.returnPressed.connect(self.tambah_barang) # Event saat Enter
        
        btn_tambah = QPushButton("Tambah")
        btn_tambah.clicked.connect(self.tambah_barang)
        
        input_layout.addWidget(QLabel("Kode:"))
        input_layout.addWidget(self.input_kode)
        input_layout.addWidget(btn_tambah)
        layout.addLayout(input_layout)

        # Table
        self.tabel = QTableWidget(0, 3)
        self.tabel.setHorizontalHeaderLabels(["Nama Barang", "Harga", "Total"])
        layout.addWidget(self.tabel)

        # Total Display
        self.label_total = QLabel("TOTAL: Rp 0")
        self.label_total.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.label_total.setStyleSheet("color: green;")
        self.label_total.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.label_total)

    def tambah_barang(self):
        kode = self.input_kode.text()
        if kode in self.database:
            barang = self.database[kode]
            row = self.tabel.rowCount()
            self.tabel.insertRow(row)
            self.tabel.setItem(row, 0, QTableWidgetItem(barang["nama"]))
            self.tabel.setItem(row, 1, QTableWidgetItem(str(barang["harga"])))
            self.tabel.setItem(row, 2, QTableWidgetItem(str(barang["harga"])))
            
            self.total_belanja += barang["harga"]
            self.label_total.setText(f"TOTAL: Rp {self.total_belanja:,}")
            self.input_kode.clear()
        else:
            self.input_kode.setText("Barang tidak ada!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KasirPyQt()
    window.show()
    sys.exit(app.exec())