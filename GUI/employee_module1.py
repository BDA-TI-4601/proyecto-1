# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_module1.ui'
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

class Ui_EmployeeModule1(object):
    def setupUi(self, EmployeeModule1):
        EmployeeModule1.setObjectName(_fromUtf8("EmployeeModule1"))
        EmployeeModule1.resize(912, 512)
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

