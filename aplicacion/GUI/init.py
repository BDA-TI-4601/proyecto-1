from PyQt4 import QtCore, QtGui
import ast
import sys, os
from http_service import *
from messages import *
sys.path.insert(0, os.getcwd() + "/ui")
from register_module import *
from client_module import *
from employee_module1 import *
from employee_module2 import *
from manager_module import *
from admin_module import *
from data_manager import *

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

###########################   Window Login Class  ###################################

class Ui_Login(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setFixedSize(546, 235)
        Login.move(400, 200) 
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
        self.password_data.setEchoMode(QtGui.QLineEdit.Password)
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
        self.label_ubication = QtGui.QLabel(Login)
        self.label_ubication.setGeometry(QtCore.QRect(20, 10, 71, 31))
        self.label_ubication.setObjectName(_fromUtf8("label_ubication"))
        self.label_logo = QtGui.QLabel(Login)
        self.label_logo.setGeometry(QtCore.QRect(40, 60, 211, 141))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.province = QtGui.QComboBox(Login)
        self.province.setGeometry(QtCore.QRect(100, 10, 113, 33))
        self.province.setObjectName(_fromUtf8("province"))
        self.types = None

        #Ask for branches 
        branches = send_request(ask_branches, None, False)
        if (branches["status"] == int(OK)):
            for i in range (len(branches["data"])):
                provinces.append( branches["data"][i]["ubication"] )
            fill_boxes(self.province, provinces)
        else: 
            show_message("Server out of service", "Error", False)

        types = send_request(ask_types, None, False)  
        if (types["status"] == int(OK)):
            self.types = types["data"]
            self.types = ast.literal_eval(self.types)   
        else: 
            show_message("Server out of service", "Error", False)


    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "CourierTEC Platform System", None))
        self.login_button.setText(_translate("Login", "Login", None))
        self.register_button.setText(_translate("Login", "Register", None))
        self.quit_button.setText(_translate("Login", "Quit", None))
        self.label_username.setText(_translate("Login", "Username:", None))
        self.label_password.setText(_translate("Login", "Password:", None))
        self.label_ubication.setText(_translate("Login", "Ubication:", None))
        self.login_button.clicked.connect(lambda: self.send_login_request(Login))
        self.register_button.clicked.connect(self.open_register_module)
        self.quit_button.clicked.connect(Login.close)

    
    # Check the user's credentials & show new window 
    # according with the user type 
    def send_login_request(self, module):
        if (self.user_data.text().isEmpty() or self.password_data.text().isEmpty()):
            show_message("Please insert the required information", "Warning", False)
        else:
            #Send login request to server API
            login_json["username"] = str(self.user_data.text())
            login_json["password"] = str(self.password_data.text())
            login_json["id_branch"] = self.get_id_branch(self.province.currentText()) 
            login_response = send_request(login_request, login_json, True) 
            if (login_response["status"] == ERROR):
                show_message("User doesn't exist, try again...", "Alert", False)
            elif (login_response["status"] == CLIENT): #client
               #Open client session
               self.open_module(module, Ui_ClientModule(), "client", login_response) 
            elif (login_response["status"] == WORKER): #worker
                if (login_response["data"]["type"] == "Gerente"):
                    self.open_module(module, Ui_ManagerModule(), "manager", login_response)
                elif (login_response["data"]["type"] == "Administrador"):
                    self.open_module(module, Ui_AdminModule(), "admin", login_response)
                elif (login_response["data"]["type"] == "Empleado"):
                    self.open_module(module, Ui_EmployeeModule1(), "employee", login_response)

    def get_id_branch(self, pname):
        if (pname == "Heredia"):
            return 1
        elif (pname == "Cartago"):
            return 3
        else: 
            return 2
    
    # Open register window module if the user 
    # wants to be part of the platform
    def open_register_module(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_RegisterClient()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_module(self, login, module, type, pdata):
        self.window = QtGui.QMainWindow()
        self.ui = module
        self.ui.setupUi(self.window)
        if (type == "client"):
            self.ui.set_client_data(pdata["data"]["name"] + " " + pdata["data"]["lname"] , pdata["branch"]["type"],
                                     pdata["branch"]["ubication"], pdata["branch"]["telephone"], pdata["branch"]["email"] ) 
            self.ui.fill_client_table( pdata["packages"])

        elif (type == "employee"):
            self.ui.set_employee_data(pdata["data"]["name"], pdata["data"]["lname"], pdata["data"]["id"])
            self.ui.fill_employee_table( pdata["packages"] )
            self.ui.set_types(self.types)

        elif (type == "manager"):
            self.ui.set_manager_data(pdata["data"]["name"], pdata["data"]["lname"], pdata["data"]["type"])

        elif (type == "admin"):
            self.ui.set_admin_data(pdata["data"]["name"], pdata["data"]["lname"], pdata["data"]["type"])
            self.ui.set_types(self.types)


        self.ui.set_tmp_login(login)
        self.window.show()
        self.hide()

        
###########################   Window Login Init  #####################################


 #   Init frontend application
def main():
    app = QtGui.QApplication(sys.argv)
    login_window = Ui_Login()
    login_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

