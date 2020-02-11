from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:farmingfam@localhost:5432/farmingdb'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

import models

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/readings/", methods=['POST']))
def readings():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port='8080',debug=True)