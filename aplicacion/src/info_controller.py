
from sql_connection import *

def get_types():
    types = []
    query = "SELECT pt_name FROM PACKAGE_TYPE"
    content = new_query(query).fetchall()
    for i in content:
        types += [i[0]]
    return str(types)
