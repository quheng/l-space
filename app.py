from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# variable
@app.route("/id/<id>")
def variable(id=None):
    return id

# key-value
@app.route("/key-value")
def key_value():
    return jsonify(request.args)

# form-data can not use in GET method
@app.route('/form-data', methods=['POST'])  #default methods is GET
def form_data():
    return jsonify(request.form)
