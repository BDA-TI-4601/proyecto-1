import requests

# Peticiones al servidor API 
IP = ""
PORT = "8080"
HTTP = "http://"
OK = "200"

##########################    LINKS  ######################################################
#LOGIN
ask_branches = HTTP + IP + PORT + "/branches" #ask for branches 
login_request = HTTP + IP + PORT + "/login" # login request

#REGISTER
register_request = HTTP + IP + PORT + "/register" #register client request

#CLIENT
# --------------------------------- #

#EMPLOYEE
new_package_request = HTTP + IP + PORT + "/new_package" #new package request
delete_package_request = HTTP + IP + PORT + "/del_package" #delete package request

#MANAGER
amount_branch_request = HTTP + IP + PORT + "/branch_amount" #consult amount branch manager
top3_request = HTTP + IP + PORT + "/top3" #consult top 3 clients 

#ADMINISTRATOR
raised_money_admin_request = HTTP + IP + PORT + "/raised_money" # consult raised money 
mensual_amount_admin_request = HTTP + IP + PORT + "/mensual_amount" #mensual amount admin
amount_packages_admin_request =  HTTP + IP + PORT + "/amount_packages" #amount packages in range date
averages_admin_request = HTTP + IP + PORT + "/averages" #averages packages request


##########################    JSON PROTOCOL   ##############################################

# Login Module
login_json = {"username":"", "password":"", "id_branch":""}

#Register Module
register_json = {"name":"", "lastname":"", "id":"","account":"",
                "telephone":"","type":"","province":"", "password":""}

#Client Module 
#    ------------------------------------------   #

#Employee Module 
delete_package_json = {"id_package":""}
new_package_json = {"id_client":"", "reception_date":"","category":"","type":"","description":"",
                    "weight":"", "value":""}

#Manager Module
amount_branch_json = {"branch":"","startdate":"","finaldate":"", "type":""}

#Admin Module
mensual_amount_admin_json = {"month":"","type":""}
amount_packages_admin_json = {"startdate":"","finaldate":""}


##########################    REQUEST FUNCTION   ##############################################

def send_request(plink, pdata, isPost):
    if (isPost):
        _response = requests.post(plink, json = pdata)
    else:
        _response = requests.get(plink)
    received_data = _response.json()
    return received_data