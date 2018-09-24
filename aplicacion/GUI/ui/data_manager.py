# coding=utf-8
from PyQt4 import QtGui
import ast

#Comboboxes information
provinces = []
total_provinces = [u"San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas",u"Limón"]
type_client_data = ["Gold","Platinum","Bronze"]
type_package_data = [ ]
category_package_data = ["Regular", "Special"]
months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]

# STATUS CODES
ERROR = 404
CLIENT = 100
WORKER = 101

#NUMBER COLUMNS 
PACKAGE_EMP_COLS = 8
PACKAGE_COLS = 7
TOP3_COLS = 3
MENSUAL_COLS = 2
AVERAGE_COLS = 6

#################   TABLE COLUMNS     ########################################################### 

package_columns = ["ID","Weight","Reception Date", "Delivered","Type","Category","Total"]
packages_emp = ["ID Pack","ID Client","Last Name","Type","Category","Value","Reception Date","Delivery Date"]
top3_columns = ["Name","Lastname","Total"]
amount_packages_columns  = ["ID Package","ID Client","Last Name","Name", "Reception Date", "Average"]


#################   TABLE DATA     ############################################################## 

packages_data = [ ]
all_packages = [ ]
top3_clients = [ ]

amount_packages_bydate = []

#Fill combo boxes with data
def fill_boxes( pbox, pdata ):
    for i in range(len(pdata)):
        pbox.addItem(pdata[i])

# Fill table with the corresponding data
def fill_table( ptable, ptuples, pcols ):
    ptable.clearContents()
    _row = 0
    for i in ptuples:
        ptable.setRowCount(_row + 1)    
        for j in range (pcols):
            ptable.setItem(_row, j, QtGui.QTableWidgetItem(i[j]))
        _row += 1

#Delete some row in table
def delete_row( data, prow ):
    del data[prow]

#Add column into the table
def add_column_table( pcolumn, ptable, pamount ):
    print len(ptable)
    for i in range(len(ptable)):
        for j in range (pamount):
            if (j == (pamount-1)):
                ptable[i][j] = pcolumn[i]
            

def serialize_date( pdate, pchar1, pchar2 ):
    _date = str(pdate)
    date_decomp = _date.split(pchar1)
    parsed_date = ( "20"+date_decomp[2]+pchar2+date_decomp[1]+pchar2+date_decomp[0] )
    return parsed_date 
    

def serialize_table(ppackages, pspaces, pcols, packages_arr ):
    _packages = ast.literal_eval(ppackages)
    for i in range ( len(_packages) ):
        new_package = []
        for j in range( pcols ):
            new_package.append( unicode(_packages[i][pspaces[j]]) )   
        packages_arr.append( new_package)



def set_package_types( types_arr ):
    global type_package_data
    type_package_data = types_arr

