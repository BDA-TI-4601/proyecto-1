# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from http_service import *
from data_manager import *
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


###########################   Window Manager Class  ###################################

class Ui_ManagerModule(object):
    def setupUi(self, ManagerModule):
        ManagerModule.setObjectName(_fromUtf8("ManagerModule"))
        ManagerModule.setFixedSize(917, 479)
        self.label_branch = QtGui.QLabel(ManagerModule)
        self.label_branch.setGeometry(QtCore.QRect(30, 100, 71, 31))
        ManagerModule.move(200, 100)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_branch.setFont(font)
        self.label_branch.setObjectName(_fromUtf8("label_branch"))
        self.branch_data = QtGui.QComboBox(ManagerModule)
        self.branch_data.setGeometry(QtCore.QRect(100, 100, 83, 33))
        self.branch_data.setObjectName(_fromUtf8("branch_data"))
        self.start_date = QtGui.QDateEdit(ManagerModule)
        self.start_date.setGeometry(QtCore.QRect(330, 100, 110, 33))
        self.start_date.setObjectName(_fromUtf8("start_date"))
        self.final_date = QtGui.QDateEdit(ManagerModule)
        self.final_date.setGeometry(QtCore.QRect(580, 100, 110, 33))
        self.final_date.setObjectName(_fromUtf8("final_date"))
        self.label_start = QtGui.QLabel(ManagerModule)
        self.label_start.setGeometry(QtCore.QRect(220, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_start.setFont(font)
        self.label_start.setObjectName(_fromUtf8("label_start"))
        self.label_finsl = QtGui.QLabel(ManagerModule)
        self.label_finsl.setGeometry(QtCore.QRect(470, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_finsl.setFont(font)
        self.label_finsl.setObjectName(_fromUtf8("label_finsl"))
        self.consult_amount_button = QtGui.QPushButton(ManagerModule)
        self.consult_amount_button.setGeometry(QtCore.QRect(520, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.consult_amount_button.setFont(font)
        self.consult_amount_button.setObjectName(_fromUtf8("consult_amount_button"))
        self.amount_data = QtGui.QLineEdit(ManagerModule)
        self.amount_data.setGeometry(QtCore.QRect(330, 170, 141, 41))
        self.amount_data.setObjectName(_fromUtf8("amount_data"))
        self.label_4 = QtGui.QLabel(ManagerModule)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 241, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Serif Myanmar"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(ManagerModule)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 191, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Serif Myanmar"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.logout_button = QtGui.QPushButton(ManagerModule)
        self.logout_button.setGeometry(QtCore.QRect(790, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.logout_button.setFont(font)
        self.logout_button.setObjectName(_fromUtf8("logout_button"))
        self.top3_table = QtGui.QTableWidget(ManagerModule)
        self.top3_table.setGeometry(QtCore.QRect(30, 290, 651, 101))
        self.top3_table.setObjectName(_fromUtf8("top3_table"))
        self.top3_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.top3_table.setDragDropOverwriteMode(False)
        self.top3_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.top3_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.top3_table.setWordWrap(False)
        self.top3_table.setSortingEnabled(False)
        self.top3_table.setColumnCount(TOP3_COLS)
        self.top3_table.setRowCount(0)
        self.top3_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|
                                                          QtCore.Qt.AlignCenter)
        self.top3_table.horizontalHeader().setHighlightSections(False)
        self.top3_table.horizontalHeader().setStretchLastSection(True)
        self.top3_table.verticalHeader().setVisible(False)
        self.top3_table.setAlternatingRowColors(True)
        self.top3_table.verticalHeader().setDefaultSectionSize(20)
        self.top3_table.setHorizontalHeaderLabels(top3_columns)            
        for i, width in enumerate((130, 290), start=0):
            self.top3_table.setColumnWidth(i, width)


        self.label_logo = QtGui.QLabel(ManagerModule)
        self.label_logo.setGeometry(QtCore.QRect(760, 300, 131, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_logo.setFont(font)
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("images/manager.png")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.consult_top3_button = QtGui.QPushButton(ManagerModule)
        self.consult_top3_button.setGeometry(QtCore.QRect(30, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.consult_top3_button.setFont(font)
        self.consult_top3_button.setObjectName(_fromUtf8("consult_top3_button"))
        self.label_info1 = QtGui.QLabel(ManagerModule)
        self.label_info1.setGeometry(QtCore.QRect(760, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_info1.setFont(font)
        self.label_info1.setObjectName(_fromUtf8("label_info1"))
        self.label_info2 = QtGui.QLabel(ManagerModule)
        self.label_info2.setGeometry(QtCore.QRect(760, 160, 190, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_info2.setFont(font)
        self.label_info2.setObjectName(_fromUtf8("label_info2"))
        self.label_info3 = QtGui.QLabel(ManagerModule)
        self.label_info3.setGeometry(QtCore.QRect(760, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_info3.setFont(font)
        self.label_info3.setObjectName(_fromUtf8("label_info3"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.retranslateUi(ManagerModule)
        QtCore.QMetaObject.connectSlotsByName(ManagerModule)
        self.login_tmp = None
        self.amount_data.setReadOnly(True)
        fill_boxes(self.branch_data, provinces)

    def retranslateUi(self, ManagerModule):
        ManagerModule.setWindowTitle(_translate("ManagerModule", "CourierTEC - Manager Session", None))
        self.label_branch.setText(_translate("ManagerModule", "Branch:", None))
        self.label_start.setText(_translate("ManagerModule", "Start Date:", None))
        self.label_finsl.setText(_translate("ManagerModule", "Final Date:", None))
        self.consult_amount_button.setText(_translate("ManagerModule", "Consult ", None))
        self.label_4.setText(_translate("ManagerModule", "Branch\'s Amount", None))
        self.label_5.setText(_translate("ManagerModule", "Top 3 Clients", None))
        self.logout_button.setText(_translate("ManagerModule", "Log Out", None))
        self.consult_top3_button.setText(_translate("ManagerModule", "Consult", None))
        self.label_info1.setText(_translate("ManagerModule", "Info Manager 1", None))
        self.label_info2.setText(_translate("ManagerModule", "Info Manager 2", None))
        self.label_info3.setText(_translate("ManagerModule", "Info Manager 3", None))
        self.logout_button.clicked.connect(lambda: self.logout_action(ManagerModule))
        self.consult_amount_button.clicked.connect(lambda: self.consult_manager(1) )
        self.consult_top3_button.clicked.connect(lambda: self.consult_manager(2) )

    #Consult the amount of some type of package in some branch within an 
    # specific date range
    def consult_manager(self, poperation):
        # make json with data 
        manager_json["date_min"] = serialize_date( self.start_date.text(), "/", "-" )
        manager_json["date_max"] = serialize_date( self.final_date.text(), "/", "-" )
        manager_json["operation"] = poperation
        manager_json["branch"] = unicode(self.branch_data.currentText())
        
        # http request 
        response = send_request(manager_request, manager_json, True)

        if (response["status"] == int(OK) ):
            if (poperation == 1):
                self.amount_data.setText( str(response["data"]) )
            elif (poperation == 2):    # Consult top 3 clients according to the amount by each one 
                serialize_table(response["data"], ["name","lname","total"], TOP3_COLS, top3_clients)
                fill_table(self.top3_table, top3_clients, TOP3_COLS)
        else:
            show_message("Couldn't consult","Alert",False)
        
    # Sign out 
    def logout_action(self, module):
        module.hide()
        self.login_tmp.show()

    #Set manager information
    def set_manager_data(self, pname, plname, ptype):
        self.label_info1.setText("Name: " + pname)
        self.label_info2.setText(plname)
        self.label_info3.setText(ptype)

    # Helps closing the login window and starts session
    def set_tmp_login(self, module):
        self.login_tmp = module

