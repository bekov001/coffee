import sqlite3
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QHeaderView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("main.sqlite3")
        self.con.create_function("rev", 1, lambda s: s[::-1])
        self.titles = None
        self.show_table()

    def show_table(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM coffee").fetchall()

        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if val and j == 3:
                    val = "Молотый"
                elif not val and j == 3:
                    val = "В зернах"
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())


# import sqlite3
#
# con = sqlite3.connect("main.sqlite3")
# cur = con.cursor()
# cur.execute("INSERT INTO coffee VALUES(1, 'EXPRESS', 70, TRUE, 'вкусный кофе', 400, 500)")
# con.commit()