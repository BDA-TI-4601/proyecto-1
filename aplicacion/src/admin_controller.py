from sql_connection import *

def get_total_by_type( p_type, p_date_min, p_date_max ):
    query = ("SELECT pt_id FROM PACKAGE_TYPE WHERE pt_name='"+p_type+"'")
    content = new_query( query ).fetchall()[0][0]
    query = ("EXEC packageTypeAmount "+str(content)+", '"+p_date_min+"', '"+p_date_max+"'")
    content = new_query( query ).fetchall()
    return content[0][1]

def get_total_amount( p_branch ):
    query = ("EXEC branchTotalAmount '"+p_branch+"'")
    content = new_query( query ).fetchall()
    return content[0][0]

def get_packages_per_client( p_date_min, p_date_max ):
    query = ("EXEC packagesPerClient '"+p_date_min+"', '"+p_date_max+"'")
    content = new_query( query ).fetchall()
    orders = []
    for i in content:
        orders += [{"id_client":i[0],
                    "name":i[1],
                    "lname":i[2],
                    "id_package_branch":i[3],
                    "reception_date":i[4] }]
    return str(orders)

def get_avg_packages( p_date_min, p_date_max ):
    query = ("EXEC averageAmountPerClient '"+p_date_min+"', '"+p_date_max+"'")
    content = new_query( query ).fetchall()
    clients = []
    for i in content:
        clients += [{"name":i[0],"lname":i[1],"average":i[2]}]
    return str(clients)