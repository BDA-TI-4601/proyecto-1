
from sql_connection import *

def create_user(    p_id,
                    p_name,
                    p_lname,
                    p_telephone,
                    p_username,
                    p_password,
                    p_type,
                    p_province ):
    query = (   " INSERT INTO CLIENT VALUES "
                " ('"+p_id+"', "
                " '"+p_name+"', "
                " '"+p_lname+"', "
                " '"+p_telephone+"', "
                " '"+p_username+"', "
                " '"+p_password+"', "
                " '"+str(p_type)+"', "
                " '"+str(p_province)+"', " 
                " NEWID() )" )
    new_query( query )
    commit_changes()
    return {"status":200}

def update_package( p_id, p_date ):
    query = (   "UPDATE PACKAGE_BRANCH "
                " SET pb_delivery_date='"+p_date+"' "
                " WHERE pb_id_package='"+str(p_id)+"'" )
    new_query( query )
    commit_changes()
    return {"status":200}

def new_package(    p_id_client,
                    p_reception_date,
                    p_type,
                    p_weight,
                    p_description,
                    p_value,
                    p_branch ):
    id_category = get_id_type_by_name( p_type )
    query = (   "INSERT INTO PACKAGE VALUES "
                "( '"+p_reception_date+"',"
                " "+str(p_value)+", "
                " "+str(p_weight)+", "
                " "+str(id_category)+", "
                " NEWID() )" )
    new_query( query )
    query = "SELECT TOP 1 p_id FROM PACKAGE ORDER BY p_id DESC"
    id_package = new_query( query ).fetchall()[0][0]
    query = ("SELECT pt_price_kg FROM PACKAGE_TYPE WHERE pt_id="+str(id_category))
    price = new_query( query ).fetchall()[0][0]
    total = price * p_weight
    query = (   "INSERT INTO PACKAGE_BRANCH VALUES "
                " ("+str(total)+", NULL, "+str(id_package)+", '"+p_id_client+"', "
                " "+str(p_branch)+", NEWID() )" )
    new_query( query )
    commit_changes()
    return {"status":200}

def get_id_type_by_name( p_type ):
    query = ("SELECT pt_id FROM PACKAGE_TYPE WHERE pt_name='"+p_type+"'")
    content = new_query( query ).fetchall()[0][0]
    return content
