# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_module.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from http_service import *
from filler import *

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


###########################   Window Admin Class  ###################################

class Ui_AdminModule(object):

    def setupUi(self, AdminModule):
        AdminModule.setObjectName(_fromUtf8("AdminModule"))
        AdminModule.setFixedSize(945, 554)
        AdminModule.move(200,100)
        self.label = QtGui.QLabel(AdminModule)
        self.label.setGeometry(QtCore.QRect(10, 50, 161, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AdminModule)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 311, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(AdminModule)
        self.label_3.setGeometry(QtCore.QRect(340, 50, 201, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tableWidget = QtGui.QTableWidget(AdminModule)
        self.tableWidget.setGeometry(QtCore.QRect(240, 360, 511, 171))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setColumnCount(AVERAGE_COLS)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|
                                                          QtCore.Qt.AlignCenter)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.setHorizontalHeaderLabels(amount_packages_columns)            
        for i, width in enumerate((50, 90, 115, 150), start=0):
            self.tableWidget.setColumnWidth(i, width)

        self.tableWidget_2 = QtGui.QTableWidget(AdminModule)
        self.tableWidget_2.setGeometry(QtCore.QRect(550, 70, 201, 211))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setWordWrap(False)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setColumnCount(MENSUAL_COLS)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|
                                                          QtCore.Qt.AlignCenter)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_2.setHorizontalHeaderLabels(mensual_amount_columns)            
        for i, width in enumerate((50, 100), start=0):
            self.tableWidget_2.setColumnWidth(i, width)
        
        self.dateEdit = QtGui.QDateEdit(AdminModule)
        self.dateEdit.setGeometry(QtCore.QRect(120, 370, 110, 33))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(AdminModule)
        self.dateEdit_2.setGeometry(QtCore.QRect(120, 420, 110, 33))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.pushButton = QtGui.QPushButton(AdminModule)
        self.pushButton.setGeometry(QtCore.QRect(20, 490, 91, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.months = QtGui.QComboBox(AdminModule)
        self.months.setGeometry(QtCore.QRect(450, 120, 83, 33))
        self.months.setObjectName(_fromUtf8("months"))
        self.type_package = QtGui.QComboBox(AdminModule)
        self.type_package.setGeometry(QtCore.QRect(450, 170, 83, 33))
        self.type_package.setObjectName(_fromUtf8("type_package"))
        self.pushButton_2 = QtGui.QPushButton(AdminModule)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 230, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(AdminModule)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 490, 101, 35))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(AdminModule)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 30, 101, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(AdminModule)
        self.label_5.setGeometry(QtCore.QRect(800, 128, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(AdminModule)
        self.label_8.setGeometry(QtCore.QRect(800, 390, 141, 161))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("images/administrator.png")))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(AdminModule)
        self.label_6.setGeometry(QtCore.QRect(800, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(AdminModule)
        self.label_7.setGeometry(QtCore.QRect(800, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(AdminModule)
        self.label_9.setGeometry(QtCore.QRect(20, 380, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(AdminModule)
        self.label_10.setGeometry(QtCore.QRect(20, 420, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit = QtGui.QLineEdit(AdminModule)
        self.lineEdit.setGeometry(QtCore.QRect(10, 110, 191, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_5 = QtGui.QPushButton(AdminModule)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 160, 121, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_11 = QtGui.QLabel(AdminModule)
        self.label_11.setGeometry(QtCore.QRect(370, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(AdminModule)
        self.label_12.setGeometry(QtCore.QRect(310, 170, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.retranslateUi(AdminModule)
        QtCore.QMetaObject.connectSlotsByName(AdminModule)
        self.login_tmp = None
        self.lineEdit.setReadOnly(True)
        fill_boxes(self.months, months)
        fill_boxes(self.type_package, type_package_data)

    def retranslateUi(self, AdminModule):
        AdminModule.setWindowTitle(_translate("AdminModule", "CourierTEC - Admin Session", None))
        self.label.setText(_translate("AdminModule", "Raised Money", None))
        self.label_2.setText(_translate("AdminModule", "Average Amount Packages", None))
        self.label_3.setText(_translate("AdminModule", "Mensual Amount", None))
        self.pushButton.setText(_translate("AdminModule", "Calculate", None))
        self.pushButton_2.setText(_translate("AdminModule", "Consult", None))
        self.pushButton_3.setText(_translate("AdminModule", "Add Average", None))
        self.pushButton_4.setText(_translate("AdminModule", "Log Out", None))
        self.label_5.setText(_translate("AdminModule", "admin info 1", None))
        self.label_6.setText(_translate("AdminModule", "admin info 2", None))
        self.label_7.setText(_translate("AdminModule", "admin info 3", None))
        self.label_9.setText(_translate("AdminModule", "Start Date:", None))
        self.label_10.setText(_translate("AdminModule", "Final Date:", None))
        self.pushButton_5.setText(_translate("AdminModule", "Refresh", None))
        self.label_11.setText(_translate("AdminModule", "Month:", None))
        self.label_12.setText(_translate("AdminModule", "Type Package:", None))
        self.pushButton.clicked.connect(self.amount_packages_bydate) #amount packages
        self.pushButton_2.clicked.connect(self.mensual_amount) #mensual amount
        self.pushButton_3.clicked.connect(self.add_averages) #amount packages
        self.pushButton_4.clicked.connect(lambda: self.logout_action(AdminModule)) #logout
        self.pushButton_5.clicked.connect(self.refresh_raised_money) #refresh

    def add_averages(self):
        #Http request
       # response = send_request(averages_admin_request, {"average":"ok"}, True)
       # Save average in array
        add_column_table(average_bydate, amount_packages_bydate, AVERAGE_COLS)
        fill_table(self.tableWidget, amount_packages_bydate, AVERAGE_COLS)

    def amount_packages_bydate(self):
        #Create json
        amount_packages_admin_json["startdate"] = serialize_date( self.dateEdit.text() )
        amount_packages_admin_json["finaldate"] = serialize_date( self.dateEdit_2.text() )
      #Send request
      #  response = send_request(amount_packages_admin_request, amount_packages_admin_json, True)
      #fill table
        fill_table(self.tableWidget, amount_packages_bydate, AVERAGE_COLS)

    def mensual_amount(self):
        mensual_amount_admin_json["month"] = str(self.months.currentText() ) 
        mensual_amount_admin_json["type"] = str(self.type_package.currentText() )
      #  response = send_request(mensual_amount_admin_request, mensual_amount_admin_json, True)
      # fill table 
        fill_table(self.tableWidget_2, mensual_amount, MENSUAL_COLS)  

    def refresh_raised_money(self):
        #http request
        self.lineEdit.setText("300000")

    def set_admin_data(self, pname, pid):
        self.label_5.setText(pname)
        self.label_6.setText(pid)
        self.label_7.setText("Algun otro dato")

    def set_tmp_login(self, module):
        self.login_tmp = module

    def logout_action(self, module):
        module.hide()
        self.login_tmp.show()