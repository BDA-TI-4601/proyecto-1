
import pyodbc

sql_connection = pyodbc.connect(    'Driver={SQL SERVER};'
                                    'Server=DESKTOP-DHKUA5V\OCHESTO_SERVER;'
                                    'Database=COURIERTEC_HEREDIA;'
                                    'Trusted_Connection=yes;')

database_pointer = sql_connection.cursor()

def new_query( str_query ):
    database_pointer.execute( str_query )
    return database_pointer
