# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(457, 382)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.roast_box = QtWidgets.QSpinBox(Dialog)
        self.roast_box.setObjectName("roast_box")
        self.horizontalLayout_2.addWidget(self.roast_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.volume_box = QtWidgets.QSpinBox(Dialog)
        self.volume_box.setMinimum(10)
        self.volume_box.setMaximum(2000)
        self.volume_box.setProperty("value", 10)
        self.volume_box.setObjectName("volume_box")
        self.horizontalLayout_5.addWidget(self.volume_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.price_box = QtWidgets.QSpinBox(Dialog)
        self.price_box.setMinimum(50)
        self.price_box.setMaximum(100000)
        self.price_box.setObjectName("price_box")
        self.horizontalLayout_4.addWidget(self.price_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sort_line = QtWidgets.QLineEdit(Dialog)
        self.sort_line.setObjectName("sort_line")
        self.horizontalLayout.addWidget(self.sort_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.type_box = QtWidgets.QComboBox(Dialog)
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.verticalLayout_2.addWidget(self.type_box)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.desc_edit = QtWidgets.QTextEdit(Dialog)
        self.desc_edit.setObjectName("desc_edit")
        self.verticalLayout.addWidget(self.desc_edit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "?????????????? ?????????????? (%)"))
        self.label_5.setText(_translate("Dialog", "?????????? (??)"))
        self.label_4.setText(_translate("Dialog", "???????? (????)"))
        self.label.setText(_translate("Dialog", "????????"))
        self.type_box.setItemText(0, _translate("Dialog", "??????????????"))
        self.type_box.setItemText(1, _translate("Dialog", "?? ????????????"))
        self.label_6.setText(_translate("Dialog", "????????????????"))
