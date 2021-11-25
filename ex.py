import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, \
    QAction, QTabWidget, QVBoxLayout, QLabel, QTableWidgetItem, QDialog, \
    QLineEdit

# Creating the main window
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Изменить"))
        self.pushButton_3.setText(_translate("Form", "Удалить"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 174)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.box = QtWidgets.QComboBox(Dialog)
        self.box.setObjectName("box")
        self.horizontalLayout_4.addWidget(self.box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Название"))
        self.label_2.setText(_translate("Dialog", "Год выпуска"))
        self.label.setText(_translate("Dialog", "Длина"))
        self.label_4.setText(_translate("Dialog", "Жанр"))


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTabWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()


# Creating tab widgets
class MyTabWidget(QWidget):
    def __init__(self, parent):
        self.con = sqlite3.connect("files/media/films_db.sqlite")
        # self.con.create_function("rev", 1, lambda s: s[::-1])

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = Films(self.con)
        self.tab2 = Genres(self.con)
        self.tabs.resize(400, 300)

        # Add tabs
        self.tabs.addTab(self.tab1, "Фильмы")
        self.tabs.addTab(self.tab2, "Жанры")

        # Create first tab

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class Base(QWidget, Ui_Form):
    def __init__(self, con):
        super().__init__()
        # self.layout = QVBoxLayout(self)
        # self.l = QLabel()
        # uic.loadUi("untitled.ui", self)
        self.setup_ui(self)
        self.con = con
        # self.l.setText("This is the s tab")
        # self.layout.addWidget(self.l)
        # self.setLayout(self.layout)

    def result(self, table, title, genre=False):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM " + table).fetchall()
        if genre:
            result = cur.execute(
                "SELECT id, title, year, (select title from genres where genre=id), duration FROM " + table).fetchall()

        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(title)
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


class Films(Base, Ui_Dialog):
    def __init__(self, con):
        super().__init__(con)
        self.result("coffee",
                    ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'],
                    True)
        self.pushButton.clicked.connect(self.run)
        self.valid = PopUp(self.con)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.update_film)
        self.pushButton_3.clicked.connect(self.delete_genre)

    def update_film(self):
        choose = self.tableWidget.selectedItems()
        if choose:
            self.run(data=[self.tableWidget.item(choose[0].row(), 4).text(), self.tableWidget.item(choose[0].row(), 2).text(), self.tableWidget.item(choose[0].row(), 1).text(), self.tableWidget.item(choose[0].row(), 3).text(), self.tableWidget.item(choose[0].row(), 0).text()])


    def delete_genre(self):
        choose = self.tableWidget.selectedItems()
        if choose:
            cur = self.con.cursor()
            query = f"""DELETE from coffee
            WHERE ID = {self.tableWidget.item(choose[0].row(), 0).text()}"""
            cur.execute(query)
            self.con.commit()
            self.result("coffee", ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'], True)

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
                    self.result("coffee", ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'], True)
        except Exception as ex:
            self.valid.label_5.setText("Неверная форма")
            print(ex)
            self.run(data)


class PopUp(QDialog, Ui_Dialog):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        lst = [i[0] for i in con.cursor().execute(
            "SELECT title FROM genres").fetchall()]
        self.box.addItems(lst)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
