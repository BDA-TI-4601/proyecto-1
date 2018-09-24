# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from employee_module2 import *
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


###########################   Window Employee Class  ###################################


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
        self.all_packages_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.all_packages_table.setDragDropOverwriteMode(False)
        self.all_packages_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.all_packages_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.all_packages_table.setWordWrap(False)
        self.all_packages_table.setSortingEnabled(False)
        self.all_packages_table.setColumnCount(PACKAGE_EMP_COLS)
        self.all_packages_table.setRowCount(0)
        self.all_packages_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|
                                                          QtCore.Qt.AlignCenter)
        self.all_packages_table.horizontalHeader().setHighlightSections(False)
        self.all_packages_table.horizontalHeader().setStretchLastSection(True)
        self.all_packages_table.verticalHeader().setVisible(False)
        self.all_packages_table.setAlternatingRowColors(True)
        self.all_packages_table.verticalHeader().setDefaultSectionSize(20)
        self.all_packages_table.setHorizontalHeaderLabels(packages_emp)            
        for i, width in enumerate((90, 120, 160, 200, 210, 220, 230), start=0):
            self.all_packages_table.setColumnWidth(i, width)

        self.label_name = QtGui.QLabel(EmployeeModule1)
        self.label_name.setGeometry(QtCore.QRect(750, 120, 150, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_employee = QtGui.QLabel(EmployeeModule1)
        self.label_employee.setGeometry(QtCore.QRect(750, 210, 150, 50))
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
        self.label_id.setGeometry(QtCore.QRect(750, 160, 200, 40))
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
        self.login_tmp = None
        self.retranslateUi(EmployeeModule1)
        QtCore.QMetaObject.connectSlotsByName(EmployeeModule1)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.pack_types = None

    def retranslateUi(self, EmployeeModule1):
        EmployeeModule1.setWindowTitle(_translate("EmployeeModule1", "CourierTEC - Employee Session", None))
        self.label.setText(_translate("EmployeeModule1", "All Packages", None))
        self.label_name.setText(_translate("EmployeeModule1", "", None))
        self.label_employee.setText(_translate("EmployeeModule1", "", None))
        self.new_package_button.setText(_translate("EmployeeModule1", "New Package...", None))
        self.logout_button.setText(_translate("EmployeeModule1", "Log Out", None))
        self.label_id.setText(_translate("EmployeeModule1", "", None))
        self.new_package_button.clicked.connect(self.open_package_form)
        self.logout_button.clicked.connect(lambda: self.logout_action(EmployeeModule1))
        self.all_packages_table.cellDoubleClicked.connect(self.show_confirm_delete)  

    # Function that handles the confirmation about delete some package
    def show_confirm_delete(self, prow, pcolumn):
        ret = question_message(self, 'Delete', "Are you sure you want to delete package?")
        if (ret == QtGui.QMessageBox.Yes):
            #http request para eliminar paquetes
            print("Row %d and Column %d was deleted" % (prow, pcolumn))
            print unicode(self.all_packages_table.item(prow, pcolumn).text())
            del_json = {"package_id":"","delivery_date":""}
            del_json["package_id"] = unicode(self.all_packages_table.item(prow, pcolumn).text())
            del_json["delivery_date"] = unicode(self.all_packages_table.item(prow, pcolumn).text())
            if (del_json["package_id"] == "" or del_json["delivery_date"] == ""):
                pass
            else:
                response = send_request(delete_package_request, del_json, True)
                if (response["status"] == int(OK)):
                    delete_row(packages_data, prow)
                    fill_table(self.all_packages_table, all_packages, PACKAGE_EMP_COLS)
                else: 
                    show_message("Coudn't delete package, try again..", "Alert", False)
        else:
            pass



    def fill_employee_table(self, ppackages):
        ["ID Pack","ID Client","Last Name","Type","Category","Value","Reception Date","Delivery Date"]
        serialize_table(ppackages, ["id_package","id_client","client_lname","type","category","value","reception_date", "delivery_date"], PACKAGE_EMP_COLS, all_packages)
        fill_table(self.all_packages_table, all_packages, PACKAGE_EMP_COLS)

     # Helps closing the login window and starts session
    def set_tmp_login(self, plogin):
        self.login_tmp = plogin

    # Open package form in order to create a new package
    def open_package_form(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_EmployeeModule2()
        self.ui.setupUi(self.window)
        self.ui.set_types2(self.pack_types)
        self.window.show()

    # Sign Out
    def logout_action(self, module):
        module.hide()
        self.login_tmp.show()

    #Set employee information
    def set_employee_data(self, pname, plname, pid):
        self.label_name.setText("Name: " + pname)
        self.label_id.setText(plname)
        self.label_employee.setText("ID: " + pid)

    def set_types(self, ptypes):
        self.pack_types = ptypes
