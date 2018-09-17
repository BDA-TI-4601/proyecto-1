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


##########################    REQUEST FUNCTION   #############################

def send_request(plink, pdata, isPost):
    if (isPost):
        _response = requests.post(plink, json = pdata)
    else:
        _response = requests.get(plink)
    received_data = _response.json()
    return received_data



##########################    JSON PROTOCOL   ###############################

# Login JSON
login_json = {"username":"", "password":""}
register_json = {"name":"", "lastname":"", "id":"","account":"","telephone":"","type":"","province":""}
package_json = {}


