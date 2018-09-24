import requests

# Peticiones al servidor API 
IP = "192.168.1.100"
PORT = "8080"
HTTP = "http://"
OK = "200"

##########################    LINKS  ######################################################
#LOGIN
ask_branches = HTTP + IP + ":" + PORT + "/ask_branches" #ask for branches 
ask_types = HTTP + IP + ":" + PORT + "/ask_types" #Ask for packages types
login_request = HTTP + IP + ":" + PORT + "/login" # login request

#REGISTER
register_request = HTTP + IP +":" + PORT + "/register" #register client request

#CLIENT
# --------------------------------- #

#EMPLOYEE
new_package_request = HTTP + IP +":" + PORT + "/new_package" #new package request
delete_package_request = HTTP + IP +":" + PORT + "/package" #delete package request

#MANAGER
manager_request = HTTP + IP + ":" + PORT + "/manager" #consult amount branch manager and top 3 clients

#ADMINISTRATOR
admin_request = HTTP + IP +":" + PORT +  "/admin"  #consultas


##########################    JSON PROTOCOL   ##############################################

# Login Module
login_json = {"username":"", "password":"", "id_branch":""}

#Register Module
register_json = {"name":"", "lname":"", "id":"","username":"",
                "telephone":"","type":"","province":"", "password":""}

#Client Module 
#    ------------------------------------------   #

#Employee Module 
delete_package_json = {"id_package":""} ####################
new_package_json = {"id":"", "reception_date":"","category":"","type":"","description":"",
                    "weight":"", "value":"", "branch":2}

#Manager Module
raised_money_json = {"operation":"","branch":"","date_min":"", "date_max":""}

#Admin Module
admin_json = {"operation":"","branch":"", "date_min":"", "date_max":"", "type":""}



##########################    REQUEST FUNCTION   ##############################################

def send_request(plink, pdata, isPost):
    if (isPost):
        _response = requests.post(plink, json = pdata)
    else:
        _response = requests.get(plink)
    received_data = _response.json()
    return received_data