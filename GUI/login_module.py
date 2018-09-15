# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_module.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

###########################   Window Login Class  #####################################

class Ui_Login(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(546, 235)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setBold(True)
        font.setWeight(75)
        Login.setFont(font)
        self.user_data = QtGui.QLineEdit(Login)
        self.user_data.setGeometry(QtCore.QRect(340, 30, 191, 33))
        self.user_data.setObjectName(_fromUtf8("user_data"))
        self.password_data = QtGui.QLineEdit(Login)
        self.password_data.setGeometry(QtCore.QRect(340, 80, 191, 33))
        self.password_data.setObjectName(_fromUtf8("password_data"))
        self.login_button = QtGui.QPushButton(Login)
        self.login_button.setGeometry(QtCore.QRect(340, 140, 90, 35))
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.register_button = QtGui.QPushButton(Login)
        self.register_button.setGeometry(QtCore.QRect(440, 140, 90, 35))
        self.register_button.setObjectName(_fromUtf8("register_button"))
        self.quit_button = QtGui.QPushButton(Login)
        self.quit_button.setGeometry(QtCore.QRect(340, 190, 90, 35))
        self.quit_button.setObjectName(_fromUtf8("quit_button"))
        self.label_username = QtGui.QLabel(Login)
        self.label_username.setGeometry(QtCore.QRect(260, 30, 71, 31))
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.label_password = QtGui.QLabel(Login)
        self.label_password.setGeometry(QtCore.QRect(260, 80, 71, 31))
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.label_logo = QtGui.QLabel(Login)
        self.label_logo.setGeometry(QtCore.QRect(20, 40, 211, 141))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "CourierTEC Platform System", None))
        self.login_button.setText(_translate("Login", "Login", None))
        self.register_button.setText(_translate("Login", "Register", None))
        self.quit_button.setText(_translate("Login", "Quit", None))
        self.label_username.setText(_translate("Login", "Username:", None))
        self.label_password.setText(_translate("Login", "Password:", None))
        self.login_button.clicked.connect(send_login_request)
        self.register_button.clicked.connect(open_register_module)
        self.quit_button.clicked.connect(self.close)


###########################   Window Login Functions  #####################################

# Check the user's credentials & show new window 
# according with the user type 
def send_login_request():
    print "Login request"
    if (login_window.user_data.text() == "" or login_window.password_data.text() == ""):
        show_message("Please insert the required information", "Warning", False)
    else:
        pass
        # Se envia login request con los datos
        # Se parsea json recibido
        #Se carga una nueva ventana (admin, empleado, cliente)

# Show warning/info message to prevent 
# something wrong with the app
def show_message(pmessage, ptitle, pinfo):
    msg_box = QtGui.QMessageBox()
    if (pinfo):
        msg_box.setIcon(QtGui.QMessageBox.Information)
    else:
        msg_box.setIcon(QtGui.QMessageBox.Warning)
    msg_box.setText(pmessage)
    msg_box.setWindowTitle(ptitle)
    msg_box.setStandardButtons(QtGui.QMessageBox.Ok)
    msg_box.exec_()

# Open register window module if the user wants to be part of the platform
def open_register_module():
    pass


###########################   Window Login Init  #####################################


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    login_window = Ui_Login()
    login_window.show()
    sys.exit(app.exec_())

