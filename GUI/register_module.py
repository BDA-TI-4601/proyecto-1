# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_module.ui'
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

class Ui_RegisterClient(object):
    def setupUi(self, RegisterClient):
        RegisterClient.setObjectName(_fromUtf8("RegisterClient"))
        RegisterClient.resize(446, 282)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        RegisterClient.setFont(font)
        self.register_button = QtGui.QPushButton(RegisterClient)
        self.register_button.setGeometry(QtCore.QRect(250, 210, 151, 35))
        self.register_button.setObjectName(_fromUtf8("register_button"))
        self.name_data = QtGui.QLineEdit(RegisterClient)
        self.name_data.setGeometry(QtCore.QRect(110, 30, 113, 33))
        self.name_data.setText(_fromUtf8(""))
        self.name_data.setObjectName(_fromUtf8("name_data"))
        self.lname_data = QtGui.QLineEdit(RegisterClient)
        self.lname_data.setGeometry(QtCore.QRect(110, 60, 113, 33))
        self.lname_data.setText(_fromUtf8(""))
        self.lname_data.setObjectName(_fromUtf8("lname_data"))
        self.id_data = QtGui.QLineEdit(RegisterClient)
        self.id_data.setGeometry(QtCore.QRect(110, 90, 113, 33))
        self.id_data.setText(_fromUtf8(""))
        self.id_data.setObjectName(_fromUtf8("id_data"))
        self.account_data = QtGui.QLineEdit(RegisterClient)
        self.account_data.setGeometry(QtCore.QRect(110, 120, 113, 33))
        self.account_data.setText(_fromUtf8(""))
        self.account_data.setObjectName(_fromUtf8("account_data"))
        self.tel_data = QtGui.QLineEdit(RegisterClient)
        self.tel_data.setGeometry(QtCore.QRect(110, 150, 113, 33))
        self.tel_data.setText(_fromUtf8(""))
        self.tel_data.setObjectName(_fromUtf8("tel_data"))
        self.type_data = QtGui.QLineEdit(RegisterClient)
        self.type_data.setGeometry(QtCore.QRect(110, 180, 113, 33))
        self.type_data.setObjectName(_fromUtf8("type_data"))
        self.prov_data = QtGui.QLineEdit(RegisterClient)
        self.prov_data.setGeometry(QtCore.QRect(110, 210, 113, 33))
        self.prov_data.setObjectName(_fromUtf8("prov_data"))
        self.label_name = QtGui.QLabel(RegisterClient)
        self.label_name.setGeometry(QtCore.QRect(30, 40, 60, 19))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_lastname = QtGui.QLabel(RegisterClient)
        self.label_lastname.setGeometry(QtCore.QRect(30, 70, 71, 19))
        self.label_lastname.setObjectName(_fromUtf8("label_lastname"))
        self.label_id = QtGui.QLabel(RegisterClient)
        self.label_id.setGeometry(QtCore.QRect(30, 100, 60, 19))
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.label_account = QtGui.QLabel(RegisterClient)
        self.label_account.setGeometry(QtCore.QRect(30, 130, 71, 19))
        self.label_account.setObjectName(_fromUtf8("label_account"))
        self.label_tel = QtGui.QLabel(RegisterClient)
        self.label_tel.setGeometry(QtCore.QRect(30, 160, 71, 20))
        self.label_tel.setObjectName(_fromUtf8("label_tel"))
        self.label_type = QtGui.QLabel(RegisterClient)
        self.label_type.setGeometry(QtCore.QRect(30, 190, 71, 20))
        self.label_type.setObjectName(_fromUtf8("label_type"))
        self.label_prov = QtGui.QLabel(RegisterClient)
        self.label_prov.setGeometry(QtCore.QRect(30, 220, 61, 20))
        self.label_prov.setObjectName(_fromUtf8("label_prov"))
        self.label_img = QtGui.QLabel(RegisterClient)
        self.label_img.setGeometry(QtCore.QRect(270, 50, 101, 111))
        self.label_img.setText(_fromUtf8(""))
        self.label_img.setPixmap(QtGui.QPixmap(_fromUtf8("images/info.png")))
        self.label_img.setObjectName(_fromUtf8("label_img"))

        self.retranslateUi(RegisterClient)
        QtCore.QMetaObject.connectSlotsByName(RegisterClient)

    def retranslateUi(self, RegisterClient):
        RegisterClient.setWindowTitle(_translate("RegisterClient", "CourierTEC - Register Client", None))
        self.register_button.setText(_translate("RegisterClient", "Register as a Client", None))
        self.label_name.setText(_translate("RegisterClient", "Name:", None))
        self.label_lastname.setText(_translate("RegisterClient", "Last Name:", None))
        self.label_id.setText(_translate("RegisterClient", "ID:", None))
        self.label_account.setText(_translate("RegisterClient", "# Account:", None))
        self.label_tel.setText(_translate("RegisterClient", "Telephone:", None))
        self.label_type.setText(_translate("RegisterClient", "Client Type:", None))
        self.label_prov.setText(_translate("RegisterClient", "Province:", None))

