from flask import Flask
from flask import request
from flask import jsonify

# init database
from .db import init_db, db_session
init_db()

u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()

print(User.query.all())
print(User.query.filter(User.name == 'admin').first())