# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_module2.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EmployeeModule2(object):
    def setupUi(self, EmployeeModule2):
        EmployeeModule2.setObjectName(_fromUtf8("EmployeeModule2"))
        EmployeeModule2.resize(655, 343)
        self.logo = QtGui.QLabel(EmployeeModule2)
        self.logo.setGeometry(QtCore.QRect(500, 120, 151, 161))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("images/newpack.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.label_2 = QtGui.QLabel(EmployeeModule2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(EmployeeModule2)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 71, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(EmployeeModule2)
        self.label_4.setGeometry(QtCore.QRect(280, 100, 81, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(EmployeeModule2)
        self.label_5.setGeometry(QtCore.QRect(280, 150, 60, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_date = QtGui.QLabel(EmployeeModule2)
        self.label_date.setGeometry(QtCore.QRect(20, 150, 111, 19))
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.label_7 = QtGui.QLabel(EmployeeModule2)
        self.label_7.setGeometry(QtCore.QRect(280, 200, 60, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(EmployeeModule2)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 60, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(EmployeeModule2)
        self.label_9.setGeometry(QtCore.QRect(280, 250, 60, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(EmployeeModule2)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 60, 19))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.goback_button = QtGui.QPushButton(EmployeeModule2)
        self.goback_button.setGeometry(QtCore.QRect(530, 40, 111, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.goback_button.setFont(font)
        self.goback_button.setObjectName(_fromUtf8("goback_button"))
        self.register_new_package_button = QtGui.QPushButton(EmployeeModule2)
        self.register_new_package_button.setGeometry(QtCore.QRect(20, 300, 211, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.register_new_package_button.setFont(font)
        self.register_new_package_button.setObjectName(_fromUtf8("register_new_package_button"))
        self.owner_data = QtGui.QLineEdit(EmployeeModule2)
        self.owner_data.setGeometry(QtCore.QRect(140, 90, 91, 33))
        self.owner_data.setText(_fromUtf8(""))
        self.owner_data.setObjectName(_fromUtf8("owner_data"))
        self.weight_data = QtGui.QLineEdit(EmployeeModule2)
        self.weight_data.setGeometry(QtCore.QRect(370, 140, 101, 33))
        self.weight_data.setObjectName(_fromUtf8("weight_data"))
        self.reception_date_data = QtGui.QLineEdit(EmployeeModule2)
        self.reception_date_data.setGeometry(QtCore.QRect(142, 140, 91, 33))
        self.reception_date_data.setObjectName(_fromUtf8("reception_date_data"))
        self.amount_data = QtGui.QLineEdit(EmployeeModule2)
        self.amount_data.setGeometry(QtCore.QRect(370, 240, 101, 33))
        self.amount_data.setObjectName(_fromUtf8("amount_data"))
        self.value_data = QtGui.QLineEdit(EmployeeModule2)
        self.value_data.setGeometry(QtCore.QRect(370, 190, 101, 33))
        self.value_data.setObjectName(_fromUtf8("value_data"))
        self.description_data = QtGui.QLineEdit(EmployeeModule2)
        self.description_data.setGeometry(QtCore.QRect(370, 90, 101, 33))
        self.description_data.setObjectName(_fromUtf8("description_data"))
        self.type_data = QtGui.QComboBox(EmployeeModule2)
        self.type_data.setGeometry(QtCore.QRect(140, 240, 91, 33))
        self.type_data.setObjectName(_fromUtf8("type_data"))
        self.category_data = QtGui.QComboBox(EmployeeModule2)
        self.category_data.setGeometry(QtCore.QRect(140, 190, 91, 33))
        self.category_data.setObjectName(_fromUtf8("category_data"))

        self.retranslateUi(EmployeeModule2)
        QtCore.QMetaObject.connectSlotsByName(EmployeeModule2)

    def retranslateUi(self, EmployeeModule2):
        EmployeeModule2.setWindowTitle(_translate("EmployeeModule2", "CourierTEC - Employee Session", None))
        self.label_2.setText(_translate("EmployeeModule2", "Create New Package", None))
        self.label_3.setText(_translate("EmployeeModule2", "Belongs To:", None))
        self.label_4.setText(_translate("EmployeeModule2", "Description:", None))
        self.label_5.setText(_translate("EmployeeModule2", "Weight:", None))
        self.label_date.setText(_translate("EmployeeModule2", "Reception Date:", None))
        self.label_7.setText(_translate("EmployeeModule2", "Value:", None))
        self.label_8.setText(_translate("EmployeeModule2", "Category:", None))
        self.label_9.setText(_translate("EmployeeModule2", "Amount:", None))
        self.label_10.setText(_translate("EmployeeModule2", "Type:", None))
        self.goback_button.setText(_translate("EmployeeModule2", "<- Go Back", None))
        self.register_new_package_button.setText(_translate("EmployeeModule2", "Register New Package", None))

