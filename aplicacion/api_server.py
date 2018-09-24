
from flask import Flask, jsonify, request, json
from src.branches_controller import *
from src.login_controller import *
from src.packages_controller import *
from src.manager_controller import *
from src.admin_controller import *
from src.register_controller import *
from src.info_controller import *

app = Flask(__name__)

@app.route("/ask_branches", methods=['GET'])
def get_branches_handler():
	response = get_branches()
	return jsonify( response )

@app.route("/branches", methods=['POST'])
def get_branch_handler():
	json_request = request.get_json(force=True)
	branch_name_str = json_request['id']
	response = get_branch( branch_name_str )
	return jsonify( response)

@app.route("/login", methods=['POST'])
def post_login_handler():
	json_request = request.get_json(force=True)
	username_str = json_request['username']
	password_str = json_request['password']
	id_branch_int = json_request['id_branch']
	response = user_login( username_str, password_str )
	response2 = get_branch( id_branch_int )
	response3 = "NONE"
	if( response["status"] == 100 ):
		response3 = get_packages_by_id_client( response["data"]["id"], id_branch_int )
	if( response["status"] == 101 ):
		response3 = get_packages_by_branch( id_branch_int )
	return jsonify( {"status":response["status"], 
					"data":response["data"],
					"branch":response2["data"],
					"packages":response3 } )

@app.route("/manager", methods=['POST'])
def info_manager_total_handler():
	json_request = request.get_json(force=True)
	operation = json_request['operation']
	response = {"status":404,"data":"Operation doesn't exist"}
	if( operation == 1 ):
		id_branch_int = json_request['branch']
		date_min = json_request['date_min']
		date_max = json_request['date_max']
		response = get_total_manager( id_branch_int, date_min, date_max )
		response = {"status":200, "data":response}
	elif( operation == 2 ):
		date_min = json_request['date_min']
		date_max = json_request['date_max']
		response = get_3_top_clients( date_min, date_max )
		response = {"status":200, "data":response}
	return jsonify(response)

@app.route("/admin", methods=['POST'])
def admin_handler():
	json_request = request.get_json(force=True)
	operation = json_request['operation']
	response = {"status":404,"data":"Operation doesn't exist"}
	if( operation == 1 ):
		type_int = json_request['type']
		date_min = json_request['date_min']
		date_max = json_request['date_max']
		response = get_total_by_type( type_int, date_min, date_max )
		response = {"status":200,"data":response}
	elif( operation == 2 ):
		branch = json_request['branch']
		response = get_total_amount( branch )
		response = {"status":200,"data":response}
	elif( operation == 3 ):
		date_min = json_request['date_min']
		date_max = json_request['date_max']
		response = get_packages_per_client( date_min, date_max )
		response = {"status":200,"data":response}
	elif( operation == 4 ):
		date_min = json_request['date_min']
		date_max = json_request['date_max']
		response = get_avg_packages( date_min, date_max )
		response = {"status":200,"data":response}
	return jsonify(response)

@app.route("/register", methods=['POST'])
def register_handler():
	json_request = request.get_json(force=True)
	client_id = json_request['id']
	name = json_request['name']
	lname = json_request['lname']
	telephone = json_request['telephone']
	username = json_request['username']
	password = json_request['password']
	client_type = json_request['type']
	province = json_request['province']
	response = create_user( client_id,
							name,
							lname,
							telephone,
							username,
							password,
							client_type,
							province )
	return jsonify(response)

@app.route("/new_package", methods=['POST'])
def new_package_handler():
	json_request = request.get_json(force=True)
	client_id = json_request['id']
	reception_date = json_request['reception_date']
	type_package = json_request['type']
	weight = json_request['weight']
	description = json_request['description']
	value = json_request['value']
	branch = json_request['branch']
	response = new_package(	client_id,
							reception_date,
							type_package,
							weight,
							description,
							value,
							branch )
	return jsonify(response)

@app.route("/package", methods=['POST'])
def update_package_handler():
	json_request = request.get_json(force=True)
	package = json_request['package_id']
	delivery_date = json_request['delivery_date']
	response = update_package( package, delivery_date )
	return jsonify(response)

@app.route("/ask_types", methods=['GET'])
def ask_types_handler():
	response = get_types()
	return jsonify({"status":200,"data":response})


if __name__ == "__main__":
	#app.debug = True		# Release server
	app.debug = True		# For debugging purposes
	app.run( host = '0.0.0.0', port=8080, processes=True )

