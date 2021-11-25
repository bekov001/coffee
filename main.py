import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets


class Coffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Кофе")
        self.con = sqlite3.connect("main.sqlite3")
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
                            [" = ".join(i if i[1].isdigit() else (i[0], f"'{i[1]}'")) for i in zip(self.tables, items)]) + \
                        f" WHERE ID = {items[0]}"
                print(query)
                cur = self.con.cursor()
                cur.execute(query)
                self.con.commit()

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
        if self.valid.exec():
            roast, volume, price, sort, type_coffee, desc = self.valid.get_values()
            cur = self.con.cursor()
            cur.execute("""INSERT INTO coffee(SORT, ROAST, MILLED, DESCRIPTION, 
            PRICE, VOLUME) VALUES(?, ?, ?, ?, ?, ?)""",
                        (sort, roast, type_coffee, desc, price, volume))
            self.con.commit()
            self.result()

    def run(self, data=False):
        try:
            if data:
                self.valid.lineEdit.setText(data[0])
                self.valid.lineEdit_2.setText(data[1])
                self.valid.lineEdit_3.setText(data[2])
                self.valid.box.setCurrentText(data[3])
                print(data)
            if self.valid.exec():
                if not self.valid.lineEdit_2.text() or 1000 > int(
                        self.valid.lineEdit_2.text()) or int(
                        self.valid.lineEdit_2.text()) > 2021:
                    self.valid.label_5.setText("Некорректный год")
                    self.run(data)
                elif not self.valid.lineEdit.text() or int(self.valid.lineEdit.text()) < 10:
                    self.valid.label_5.setText("Неправильное продолжительность фильма")
                    self.run(data)
                else:
                    cur = self.con.cursor()
                    query = f"""INSERT INTO films (title, year, genre, duration)
                    VALUES('{self.valid.lineEdit_3.text()}', 
                    {self.valid.lineEdit_2.text()}, 
                    (select id from genres where title = '{self.valid.box.currentText()}'), 
                    {self.valid.lineEdit.text()})"""
                    if data:
                        query = f"""UPDATE films SET title = '{self.valid.lineEdit_3.text()}', year = {self.valid.lineEdit_2.text()}, genre = (select id from genres where title = '{self.valid.box.currentText()}'),
                        duration =  {self.valid.lineEdit.text()}
                                    WHERE ID = {data[-1]}"""
                    print(query)
                    cur.execute(query)
                    self.con.commit()
                    self.result("films", ["ID", "Название", "Год", "Жанр",
                                          "Продолжиельность"], True)
        except Exception as ex:
            self.valid.label_5.setText("Неверная форма")
            print(ex)
            self.run(data)

    def result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM " + self.table).fetchall()

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


class PopUp(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кофе")
        uic.loadUi("addEditCoffeeForm.ui", self)

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

        return roast, volume, price, sort, type_coffee, desc


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
