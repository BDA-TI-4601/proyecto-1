
from flask import Flask, jsonify, request
from src.login_controller import *

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def post_login_handler():
	username_str = request.form['username']
	password_str = request.form['password']
	login_response = user_login( username_str, password_str )
	return jsonify( login_response )

if __name__ == "__main__":
	app.run()

