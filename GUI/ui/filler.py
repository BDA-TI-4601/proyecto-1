# coding=utf-8
from PyQt4 import QtGui

provinces = ["Heredia", "San Jose", "Cartago"]
type_client_data = ["Gold","Platinum","Bronze"]
type_package_data = ["Electronic", "Clothes", "Toys", "Home Furniture", "Food", "Batteries", "Chemicals", "Tools"]
category_package_data = ["Regular", "Special"]

PACKAGE_COLS = 6
package_columns = ["ID","Owner","Date","Type","Category","Description"]

packages_data = [("1", "Andres", "Niño", "Masculino", "06/12/2019", "Colombia"),
                 ("2", "Donald", "Trump", "Masculino", "06/12/1950", "Estados Unidos"),
                 ("3", "María Fernanda", "Espinosa", "Femenino", "06/10/1980", "Ecuador"),
                 ("4", "Alberto", "Canosa", "Masculino", "04/05/1876", "España"),
                 ("5", "Virtud", "Pontes", "Femenino", "23/18/1965", "España"),
                 ("6", "Elon", "Musk", "Masculino", "06/12/1960", "Estados Unidos"),
                 ("7", "Richard", "Branson", "Masculino", "14/12/1956", "Reino Unido"),
                 ("8", "Gabriel", "Garcia Marquez", "Masculino", "19/11/1948", "Colombia"),
                 ("9", "Valentina", "Tereshkova", "Femenino", "06/03/1937", "Rusia"),
                 ("10", "Artur", "Fischer", "Masculino", "31/12/1919", "Alemania"),
                 ("11", "Grace", "Murray Hopper", "Femenino", "09/12/1906", "Estados Unidos"),
                 ("12", "Guido van", "Rossum", "Masculino", "31/01/1956", "Países Bajos")]

def fill_boxes(pbox, pdata):
    for i in range(len(pdata)):
        pbox.addItem(pdata[i])


def fill_table(ptable, ptuples, pcols):
    ptable.clearContents()
    _row = 0
    for i in ptuples:
        ptable.setRowCount(_row + 1)    
        for j in range (pcols):
            ptable.setItem(_row, j, QtGui.QTableWidgetItem(i[j]))
        _row += 1


def delete_row(data, prow):
    del data[prow]