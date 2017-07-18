from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

# init database
from .db import init_db, db_session
from .models import User
init_db()

@app.route("/user/<name>")
def user(name=None):
    result = User.query.filter(User.name == name).first()
    return jsonify({
        'name': result.name,
        'email': result.email})

@app.route('/user', methods=['PUT'])
def create_user():
    u = User(request.form['name'], request.form['email'])
    db_session.add(u)
    db_session.commit()
    # todo error handling
    return 'succ'

# todo list all user