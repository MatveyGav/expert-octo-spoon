import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QRectF
import sqlite3


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_change)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.load_coffe()

    def load_coffe(self):
        self.cur.execute("SELECT name FROM coffee")
        categories = self.cur.fetchall()

        for category in categories:
            self.comboBox.addItem(category[0])

    def on_combobox_change(self, index):
        self.load_description()

    def load_description(self):
        data = self.cur.execute("SELECT * FROM coffee WHERE name = ?", (self.comboBox.currentText(),)).fetchall()[0]
        self.label_2.setText("ID: " + str(data[0]))
        self.label_3.setText("Название сорта: " + str(data[2]))
        self.label_4.setText("Степень обжарки: " + str(data[3]))
        self.label_5.setText("Молотый/в зёрнах: " + str(data[4]))
        self.label_6.setText(str(data[5]))
        self.label_7.setText("Цена: " + str(data[6]))
        self.label_8.setText("Объём: " + str(data[7]))
        print(data)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeWindow()
    window.show()
    sys.exit(app.exec())