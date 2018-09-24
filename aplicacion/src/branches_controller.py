
from tools import *
from database_items import *
from sql_connection import *

def get_branches():
    branches = []
    query = (   "SELECT * FROM BRANCH")
    db_data = new_query( query )
    content = db_data.fetchall()
    for i in content:
        branches += [parse_branch(  i[0],
                                    i[1],
                                    i[2],
                                    i[3],
                                    i[4],
                                    i[5] )]
    for i in branches:
        i["ubication"] = get_ubication_name(i["ubication"])
        i["type"] = get_branch_type_name(i["type"])

    return send_response( branches )

def get_ubication_name( p_id_ubication ):
    name = 0
    query = ("SELECT u_place FROM UBICATION WHERE u_id="+str(p_id_ubication))
    db_data = new_query( query )
    content = db_data.fetchall()
    return content[0][0] 

def get_branch_type_name( p_id ):
    name = 0
    query = ("SELECT bt_name FROM BRANCH_TYPE WHERE bt_id="+str(p_id))
    db_data = new_query( query )
    content = db_data.fetchall()
    return content[0][0] 

def send_response( p_branches ):
    data = {"status":200, "data":p_branches}
    return data

def get_branch( p_id ):
    branch = 0
    query = ("SELECT * FROM BRANCH WHERE b_id="+str(p_id))
    content = new_query( query ).fetchall()
    branch = parse_branch(  content[0][0],
                            content[0][1],
                            content[0][2],
                            content[0][3],
                            content[0][4],
                            content[0][5] )
    branch["ubication"] = get_ubication_name( branch["ubication"] )
    branch["type"] = get_branch_type_name(branch["type"])
    return send_response( branch )