
from tools import *
from database_items import *
from sql_connection import *

def get_province_by_id( p_id ):
    province = 0
    query_province = "SELECT * FROM PROVINCE WHERE p_id='"+str(p_id)+"'"
    database_info = new_query( query_province )
    content = database_info.fetchall()
    if( len_database_info( content ) == 1 ):
        province = parse_province(  content[0][0],
                                    content[0][1])
    return province


def get_client_type_by_id( ct_id ):
    client_type = 0
    query_client_type = "SELECT * FROM CLIENT_TYPE WHERE ct_id='"+str(ct_id)+"'"
    database_info = new_query( query_client_type )
    content = database_info.fetchall()
    if( len_database_info( content ) == 1 ):
        client_type = parse_client_type(    content[0][0],
                                            content[0][1])
    return client_type

