import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QRectF


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeWindow()
    window.show()
    sys.exit(app.exec())