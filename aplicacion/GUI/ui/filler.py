# coding=utf-8
from PyQt4 import QtGui

#Comboboxes information
provinces = ["Heredia", "San Jose", "Cartago"]
type_client_data = ["Gold","Platinum","Bronze"]
type_package_data = ["Electronic", "Clothes", "Toys", "Home Furniture", "Food", "Batteries", "Chemicals", "Tools"]
category_package_data = ["Regular", "Special"]
months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]

#Columns 
PACKAGE_COLS = 7
TOP3_COLS = 3
MENSUAL_COLS = 2
AVERAGE_COLS = 5

#################   Temporal data      ########################### 
package_columns = ["ID","Owner","Reception Date", "Delivered","Type","Category","Total"]
top3_columns = ["Name","Lastname","Amount"]
mensual_amount_columns = ["ID","Month's Amount"]
amount_packages_columns  = ["Name","Lastname","ID Package","Amount","Average"]

packages_data = [["1", "Andres", "Niño", "Masculino", "06/12/2019", "Colombia",""],
                 ["2", "Donald", "Trump", "Masculino", "06/12/1950", "Estados Unidos",""],
                 ["3", "María Fernanda", "Espinosa", "Femenino", "06/10/1980", "Ecuador",""],
                 ["4", "Alberto", "Canosa", "Masculino", "04/05/1876", "España",""],
                 ["5", "Virtud", "Pontes", "Femenino", "23/18/1965", "España",""],
                 ["6", "Elon", "Musk", "Masculino", "06/12/1960", "Estados Unidos",""],
                 ["7", "Richard", "Branson", "Masculino", "14/12/1956", "Reino Unido",""],
                 ["8", "Gabriel", "Garcia Marquez", "Masculino", "19/11/1948", "Colombia",""],
                 ["9", "Valentina", "Tereshkova", "Femenino", "06/03/1937", "Rusia",""],
                 ["10", "Artur", "Fischer", "Masculino", "31/12/1919", "Alemania",""],
                 ["11", "Grace", "Murray Hopper", "Femenino", "09/12/1906", "Estados Unidos",""],
                 ["12", "Guido van", "Rossum", "Masculino", "31/01/1956", "Países Bajos",""]]

top3_clients = [["Fabian","Astorga","200000"],
                ["Ernesto","Ulate","1000000"],
                ["Sebastian","Viquez","356000"]]

mensual_amount = [["1","20000"],["2","3059930"],["3","4567888"],
                 ["4","90000"],["5","4000"],["6","780100"]]

amount_packages_bydate = [["Luis","Sancho","12","20000",""],
                            ["Jairo","Mendez","34","9000",""],
                            ["Fabio","Moya","22","12500",""],
                            ["Enrique","Quiros","40","230000",""]]

average_bydate = ["12.46%","30.00%","15.75%","90.12%"]


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
    for i in range(len(ptable)):
        for j in range (pamount):
            if (j == (pamount-1)):
                ptable[i][j] = pcolumn[i]
            

def serialize_date( pdate ):
    try:
        line = pdate.readline()
        data = line.split("/")
        print data
    except:
        print ("Sorry, couldn't load file...")