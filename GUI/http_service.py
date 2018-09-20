import requests

# Peticiones al servidor API 
IP = ""
PORT = "8888"
HTTP = "http://"
OK = "200"

##########################    LINKS  ########################################

# login request
login_request = HTTP + IP + PORT + "/login"

#register client request
register_request = HTTP + IP + PORT + "/register"

#new package request
package_request = HTTP + IP + PORT + "/package"

#consult amount branch manager
amount_branch_request = HTTP + IP + PORT + "/branch_amount"

#mensual amount admin
mensual_amount_admin_request = HTTP + IP + PORT + "/mensual_amount"

#amount packages in range date
amount_packages_admin_request =  HTTP + IP + PORT + "/amount_packages"

#averages request
averages_admin_request = HTTP + IP + PORT + "/averages"


##########################    REQUEST FUNCTION   #############################

def send_request(plink, pdata, isPost):
    if (isPost):
        _response = requests.post(plink, json = pdata)
    else:
        _response = requests.get(plink)
    received_data = _response.json()
    return received_data

##########################    JSON PROTOCOL   ###############################

# Login Module
login_json = {"username":"", "password":""}
#Register Module
register_json = {"name":"", "lastname":"", "id":"","account":"",
                "telephone":"","type":"","province":"", "password":""}
#
package_json = {}
#Manager Module
branch_amount_manager_json = {"branch":"","startdate":"","finaldate":"", "type":""}
#Admin Module
mensual_amount_admin_json = {"month":"","type":""}
amount_packages_admin_json = {"startdate":"","finaldate":""}


