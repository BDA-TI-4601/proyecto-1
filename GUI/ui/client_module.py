# -*- coding: utf-8 -*-

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

class Ui_ClientModule(QtGui.QWidget):
    def setupUi(self, ClientModule):
        ClientModule.setObjectName(_fromUtf8("ClientModule"))
        ClientModule.setFixedSize(903, 468)
        self.label_img = QtGui.QLabel(ClientModule)
        self.label_img.setGeometry(QtCore.QRect(720, 280, 161, 161))
        self.label_img.setText(_fromUtf8(""))
        self.label_img.setPixmap(QtGui.QPixmap(_fromUtf8("images/pack.png")))
        self.label_img.setObjectName(_fromUtf8("label_img"))
        self.name_client = QtGui.QLabel(ClientModule)
        self.name_client.setGeometry(QtCore.QRect(720, 160, 171, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.name_client.setFont(font)
        self.name_client.setObjectName(_fromUtf8("name_client"))
        self.id_client = QtGui.QLabel(ClientModule)
        self.id_client.setGeometry(QtCore.QRect(720, 200, 151, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.id_client.setFont(font)
        self.id_client.setObjectName(_fromUtf8("id_client"))
        self.label_package = QtGui.QLabel(ClientModule)
        self.label_package.setGeometry(QtCore.QRect(20, 40, 361, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(26)
        self.label_package.setFont(font)
        self.label_package.setObjectName(_fromUtf8("label_package"))
        self.logout_button = QtGui.QPushButton(ClientModule)
        self.logout_button.setGeometry(QtCore.QRect(730, 40, 141, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName(_fromUtf8("logout_button"))
        self.table_client_packages = QtGui.QTableWidget(ClientModule)
        self.table_client_packages.setGeometry(QtCore.QRect(10, 100, 681, 341))
        self.table_client_packages.setObjectName(_fromUtf8("table_client_packages"))
        self.table_client_packages.setColumnCount(0)
        self.table_client_packages.setRowCount(0)
        self.label = QtGui.QLabel(ClientModule)
        self.label.setGeometry(QtCore.QRect(680, 30, 41, 51))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/user.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ClientModule)
        QtCore.QMetaObject.connectSlotsByName(ClientModule)

    def retranslateUi(self, ClientModule):
        ClientModule.setWindowTitle(_translate("ClientModule", "CourierTEC - Client Session", None))
        self.name_client.setText(_translate("ClientModule", "Nombre", None))
        self.id_client.setText(_translate("ClientModule", "# cliente", None))
        self.label_package.setText(_translate("ClientModule", "Check your Packages", None))
        self.logout_button.setText(_translate("ClientModule", "Log Out", None))

