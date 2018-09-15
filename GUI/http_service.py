import requests

# Peticiones al servidor API 

IP = "httpbin.org"
PORT = ""
HTTP = "http://"

##########################    LINKS  ########################################

# login request
login_request = HTTP + IP + PORT + "/ip"

#register client request
register_request = HTTP + IP + PORT 


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
#register_json = {}