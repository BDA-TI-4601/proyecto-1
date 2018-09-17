# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
from http_service import *
from messages import *

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
        self.login_button.clicked.connect(lambda: self.send_login_request(Login))
        self.register_button.clicked.connect(self.open_register_module)
        self.quit_button.clicked.connect(Login.close)

    
    # Check the user's credentials & show new window 
    # according with the user type 
    def send_login_request(self, module):
        if (self.user_data.text().isEmpty() or self.password_data.text().isEmpty() ):
            show_message("Please insert the required information", "Warning", False)
        else:
            #Send login request to server API
            login_json["username"] = self.user_data.text()
            login_json["password"] = self.password_data.text()
        #   login_response = send_request(login_request, login_json, 0) ####
        #   print login_response
            self.open_session_module(module)
            # Parsing received json data
            #Open user's session (admin, employee, client)
    
    # Open register window module if the user 
    # wants to be part of the platform
    def open_register_module(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_RegisterClient()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_session_module(self, module):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_ClientModule() ######
        self.ui.setupUi(self.window)
        self.ui.set_client_data(self.user_data.text(), "15789655") # Pedir nombre, id cliente y datos de los paquetes 
        self.ui.set_tmp_login(module)
        self.window.show()
        self.hide()

#_____________________________________________________________________________________

class Ui_ClientModule(QtGui.QWidget):

    def setupUi(self, ClientModule):
        ClientModule.setObjectName(_fromUtf8("ClientModule"))
        ClientModule.setFixedSize(903, 468)
        ClientModule.move(200, 100)
        self.label_img = QtGui.QLabel(ClientModule)
        self.label_img.setGeometry(QtCore.QRect(720, 280, 161, 161))
        self.label_img.setText(_fromUtf8(""))
        self.label_img.setPixmap(QtGui.QPixmap(_fromUtf8("images/pack.png")))
        self.label_img.setObjectName(_fromUtf8("label_img"))
        self.name_client = QtGui.QLabel(ClientModule)
        self.name_client.setGeometry(QtCore.QRect(720, 160, 171, 26))
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
        self.login_tmp = None
        self.retranslateUi(ClientModule) 
        QtCore.QMetaObject.connectSlotsByName(ClientModule)

    def retranslateUi(self, ClientModule):
        ClientModule.setWindowTitle(_translate("ClientModule", "CourierTEC - Client Session", None))
        self.name_client.setText(_translate("ClientModule", "Nombre", None))
        self.id_client.setText(_translate("ClientModule", "# cliente", None))
        self.label_package.setText(_translate("ClientModule", "Check your Packages", None))
        self.logout_button.setText(_translate("ClientModule", "Log Out", None))
        #self.connect(self.logout_button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.logout_button.clicked.connect(lambda: self.log_out_action(ClientModule))
    
    def set_tmp_login(self, plogin):
        self.login_tmp = plogin

    def log_out_action(self, module):
        module.hide()
        self.login_tmp.show()

    def set_client_data(self, pname, pid):
        self.name_client.setText(pname)
        self.id_client.setText(pid)

    def fill_table(self):
        #self.table_client_packages.
        pass

#_____________________________________________________________________________________

class Ui_RegisterClient(QtGui.QWidget):

    def setupUi(self, RegisterClient):
        RegisterClient.setObjectName(_fromUtf8("RegisterClient"))
        RegisterClient.setFixedSize(446, 282)
        RegisterClient.move(400, 200)
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
        self.register_button.clicked.connect(lambda: self.send_register_request(RegisterClient))

    def set_register_json(self):
        register_json["name"] = self.name_data.text()
        register_json["lastname"] = self.lname_data.text()
        register_json["id"] = self.id_data.text()
        register_json["account"] = self.account_data.text()
        register_json["telephone"] = self.tel_data.text()
        register_json["type"] = self.type_data.text()
        register_json["province"] = self.prov_data.text()


    def send_register_request(self, module):
        if (self.name_data.text().isEmpty() or self.lname_data.text().isEmpty() or self.id_data.text().isEmpty() or
         self.account_data.text().isEmpty() or self.tel_data.text().isEmpty() or self.type_data.text().isEmpty() or 
         self.prov_data.text().isEmpty()):
            show_message("Please insert the required information", "Warning", False)
        else:
            #Send register request to server API
           # self.set_register_json()
           # register_response = send_request(register_request, register_json, 1) ####
           # if (register_response["status"] == OK):
           #     self.open_session_module()   
            # else:
            #    show_message("Can't register user, try again.", "Failed", False)
            show_message("User has been registered successfully!", "Done", True)
            module.hide()
           
#_____________________________________________________________________________________

class Ui_EmployeeModule1(QtGui.QWidget):

    def setupUi(self, EmployeeModule1):
        EmployeeModule1.setObjectName(_fromUtf8("EmployeeModule1"))
        EmployeeModule1.setFixedSize(912, 512)
        EmployeeModule1.move(200, 100)
        self.label = QtGui.QLabel(EmployeeModule1)
        self.label.setGeometry(QtCore.QRect(80, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.all_packages_table = QtGui.QTableWidget(EmployeeModule1)
        self.all_packages_table.setGeometry(QtCore.QRect(20, 120, 691, 321))
        self.all_packages_table.setObjectName(_fromUtf8("all_packages_table"))
        self.all_packages_table.setColumnCount(0)
        self.all_packages_table.setRowCount(0)
        self.label_name = QtGui.QLabel(EmployeeModule1)
        self.label_name.setGeometry(QtCore.QRect(750, 120, 60, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_employee = QtGui.QLabel(EmployeeModule1)
        self.label_employee.setGeometry(QtCore.QRect(750, 210, 121, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_employee.setFont(font)
        self.label_employee.setObjectName(_fromUtf8("label_employee"))
        self.new_package_button = QtGui.QPushButton(EmployeeModule1)
        self.new_package_button.setGeometry(QtCore.QRect(20, 460, 151, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.new_package_button.setFont(font)
        self.new_package_button.setObjectName(_fromUtf8("new_package_button"))
        self.logout_button = QtGui.QPushButton(EmployeeModule1)
        self.logout_button.setGeometry(QtCore.QRect(750, 40, 151, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName(_fromUtf8("logout_button"))
        self.label_img = QtGui.QLabel(EmployeeModule1)
        self.label_img.setGeometry(QtCore.QRect(750, 270, 131, 191))
        self.label_img.setText(_fromUtf8(""))
        self.label_img.setPixmap(QtGui.QPixmap(_fromUtf8("images/employee.png")))
        self.label_img.setObjectName(_fromUtf8("label_img"))
        self.label_id = QtGui.QLabel(EmployeeModule1)
        self.label_id.setGeometry(QtCore.QRect(750, 160, 60, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_id.setFont(font)
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.label_6 = QtGui.QLabel(EmployeeModule1)
        self.label_6.setGeometry(QtCore.QRect(290, 30, 71, 61))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("images/pack_little.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(EmployeeModule1)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 51, 61))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("images/pack_little.png")))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(EmployeeModule1)
        QtCore.QMetaObject.connectSlotsByName(EmployeeModule1)

    def retranslateUi(self, EmployeeModule1):
        EmployeeModule1.setWindowTitle(_translate("EmployeeModule1", "CourierTEC - Employee Session", None))
        self.label.setText(_translate("EmployeeModule1", "All Packages", None))
        self.label_name.setText(_translate("EmployeeModule1", "Name", None))
        self.label_employee.setText(_translate("EmployeeModule1", "Employee", None))
        self.new_package_button.setText(_translate("EmployeeModule1", "New Package...", None))
        self.logout_button.setText(_translate("EmployeeModule1", "Log Out", None))
        self.label_id.setText(_translate("EmployeeModule1", "ID", None))
#_____________________________________________________________________________________

class Ui_EmployeeModule2(QtGui.QWidget):
    def setupUi(self, EmployeeModule2):
        EmployeeModule2.setObjectName(_fromUtf8("EmployeeModule2"))
        EmployeeModule2.setFixedSize(655, 343)
        EmployeeModule2.move(200, 100)
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


        
###########################   Window Login Init  #####################################


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    login_window = Ui_Login()
    login_window.show()
    sys.exit(app.exec_())

