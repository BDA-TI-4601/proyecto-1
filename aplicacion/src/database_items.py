
def parse_province(     p_id, 
                        p_name ):
    province = {
        'id' : p_id,
        'name' : p_name
    }
    return province

def parse_client_type(  ct_id,
                        ct_name ):
    client_type = {
        'id' : ct_id,
        'name' : ct_name
    }
    return client_type

def parse_client(   c_id, 
                    c_account, 
                    c_name, 
                    c_lname, 
                    c_telephone, 
                    c_username, 
                    c_password, 
                    c_type, 
                    c_province ):
    client = {
        'id' : c_id,
        'account' : c_account,
        'name' : c_name,
        'lname' : c_lname,
        'telephone' : c_telephone,
        'username' : c_username,
        'password' : c_password,
        'type' : c_type,
        'province' : c_province
    }
    return client

def parse_package_branch(   pb_id,
                            pb_total,
                            pb_delivery_date,
                            pb_id_package,
                            pb_id_client,
                            pb_id_branch ):
    package_branch = {
        'id' : pb_id,
        'total' : pb_total,
        'delivery_date' : pb_delivery_date,
        'id_package' : pb_id_package,
        'id_client' : pb_id_client,
        'id_branch' : pb_id_branch
    }
    return package_branch

def parse_package(  p_id,
                    p_reception_date,
                    p_value,
                    p_weight,
                    p_type ):
    package = {
        'id' : p_id,
        'reception_date' : p_reception_date,
        'value' : p_value,
        'weight' : p_weight,
        'type' : p_type
    }
    return package

def parse_package_type( pt_id,
                        pt_name,
                        pt_price_kg,
                        pt_category ):
    package_type = {
        'id' : pt_id,
        'name' : pt_name,
        'price_kg' : pt_price_kg,
        'category' : pt_category
    }
    return package_type

def parse_category( ca_id,
                    ca_name ):
    category = {
        'id' : ca_id,
        'name' : ca_name
    }
    return category

def parse_ubication(    u_id,
                        u_place,
                        u_address ):
    ubication = {
        'id' : u_id,
        'place' : u_place,
        'address' : u_address
    }
    return ubication

def parse_branch(   b_id,
                    b_telephone,
                    b_schedule,
                    b_email,
                    b_type,
                    b_ubication ):
    branch = {
        'id' : b_id,
        'telephone' : b_telephone,
        'schedule' : b_schedule,
        'email' : b_email,
        'type' : b_type,
        'ubication' : b_ubication
    }
    return branch

def parse_works_on( wo_worker,
                    wo_branch,
                    wo_job ):
    works_on = {
        'worker' : wo_worker,
        'branch' : wo_branch,
        'job' : wo_job
    }
    return works_on

def parse_branch_type(  bt_id,
                        bt_name ):
    branch_type = {
        'id' : bt_id,
        'name' : bt_name,
    }
    return branch_type

def parse_worker(   w_id,
                    w_name,
                    w_lname,
                    w_telephone,
                    w_username,
                    w_password ):
    worker = {
        'id' : w_id,
        'name' : w_name,
        'lname' : w_lname,
        'telephone' : w_telephone,
        'username' : w_username,
        'password' : w_password
    }
    return worker
        