from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

from yourapplication.database import init_db
>>> init_db()