
import pyodbc
from users_model import *
from info_model import *

def user_login( p_username, p_password ):
    user_client = get_client_by_username( p_username )
    user_worker = get_worker_by_username( p_username )
    if( user_client != 0 and user_client['password'] == p_password ):
        return create_login_response( user_client, "client" )
    elif( user_worker != 0 and user_worker['password'] == p_password ):
        return create_login_response( user_worker, "worker" )
    else:
        return create_login_response( None, "failed" )

def create_login_response( p_user, p_type ):
    secure_user = "Username or password incorrect!"
    status = 404
    if( p_type == "client" ):
        client_province = get_province_by_id( p_user['province'] )
        client_type = get_client_type_by_id( p_user['type'] )
        secure_user = {
            'id' : p_user['id'],
            'account' : p_user['account'],
            'name' : p_user['name'],
            'lname' : p_user['lname'],
            'telephone' : p_user['telephone'],
            'type' : client_type['name'],
            'province' : client_province['name']    
        }
        status = 100        
    elif( p_type == "worker" ):
        worker_job = get_worker_job_by_id( p_user['id'] )
        secure_user = {
            'id' : p_user['id'],
            'name' : p_user['name'],
            'lname' : p_user['lname'],
            'telephone' : p_user['telephone'],
            'type' : worker_job
        }
        status = 101
    return send_response( status, secure_user )

def send_response( p_status, p_data ):
    response = {"status":p_status,"data":p_data}
    return response