import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets

from UI.main import Ui_Form
from UI.addEditCoffeeForm import Ui_Dialog


class Coffee(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Кофе")
        self.con = sqlite3.connect("data/main.sqlite3")
        self.table = "coffee"
        self.columns = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки']
        self.tables = ["SORT", "ROAST", "MILLED", "DESCRIPTION", "PRICE", "VOLUME"]
        self.result()
        self.valid = PopUp()
        self.pushButton.clicked.connect(self.add_coffee)
        self.pushButton_2.clicked.connect(self.update_film)
        self.pushButton_3.clicked.connect(self.delete_coffee)

    def update_film(self):
        choose = self.tableWidget.selectedItems()
        if choose:
            items = [self.tableWidget.item(choose[0].row(), i).text() for i in range(7)]
            self.valid.set_values(*items[1:])
            if self.valid.exec():
                query = f"""UPDATE {self.table} SET """ + \
                        ",\n".join(
                            [" = ".join(i if i[1].isdigit() else (i[0], f"'{i[1]}'")) for i in zip(self.tables, [str(i) for i in self.valid.get_values()])]) + \
                        f" WHERE ID = {items[0]}"
                cur = self.con.cursor()
                cur.execute(query)
                self.con.commit()
                self.result()

    def delete_coffee(self):
        choose = self.tableWidget.selectedItems()
        if choose:
            cur = self.con.cursor()
            query = f"""DELETE from coffee 
            WHERE ID = {self.tableWidget.item(choose[0].row(), 0).text()}"""
            cur.execute(query)
            self.con.commit()
            self.result()

    def add_coffee(self):
        self.valid.clear()
        if self.valid.exec():
            sort, roast, type_coffee, desc, price, volume = self.valid.get_values()
            cur = self.con.cursor()
            cur.execute("""INSERT INTO coffee(SORT, ROAST, MILLED, DESCRIPTION, 
            PRICE, VOLUME) VALUES(?, ?, ?, ?, ?, ?)""",
                        (sort, roast, type_coffee, desc, price, volume))
            self.con.commit()
            self.result()

    def result(self):
        try:
            cur = self.con.cursor()
            # Получили результат запроса, который ввели в текстовое поле
            result = cur.execute("SELECT ID, SORT, ROAST, MILLED, DESCRIPTION, PRICE, VOLUME FROM " + self.table).fetchall()
            # Заполнили размеры таблицы
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(self.columns)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        except IndexError:
            pass


class PopUp(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кофе")
        self.setupUi(self)

    def clear(self):
        self.sort_line.clear()
        self.desc_edit.clear()
        self.price_box.clear()
        self.volume_box.clear()

    def set_values(self, sort, roast, milled, desc, price, volume):
        self.sort_line.setText(sort)
        self.roast_box.setValue(int(roast))
        self.type_box.setCurrentIndex(int(milled))
        self.desc_edit.setPlainText(desc)
        self.price_box.setValue(int(price))
        self.volume_box.setValue(int(volume))

    def get_values(self):
        roast = self.roast_box.value()
        volume = self.volume_box.value()
        price = self.price_box.value()
        sort = self.sort_line.text()
        type_coffee = self.type_box.currentIndex()
        desc = self.desc_edit.toPlainText()

        return sort, roast, type_coffee, desc, price, volume


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())