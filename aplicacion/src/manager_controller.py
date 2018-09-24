
from tools import *
from database_items import *
from sql_connection import *

def get_total_manager( p_id_branch, p_date_min, p_date_max ):
    query = ("EXEC branchAmount '"+p_id_branch+"', '"+p_date_min+"', '"+p_date_max+"'")
    content = new_query( query ).fetchall()[0][0]
    return content

def get_3_top_clients( p_date_min, p_date_max ):
    clients = []
    query = ("EXEC bestClients '"+p_date_min+"', '"+p_date_max+"'")
    content = new_query( query ).fetchall()
    for i in content:
        clients += [ {"total":i[0], "name":i[1], "lname":i[2]} ]
    return str(clients)

