from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgres://vpqfujcg:dsQ1MyhV-Yux8uDp4WH7CKJQHKBaOLVv@drona.db.elephantsql.com:5432/vpqfujcg'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

import models

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/api/readings/<label>", methods=['POST'])
def readings(label):
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
    add_reading = models.readings(var_val=content['var_val'], env_var_id=content['env_var_id'], shelf_id=content['shelf_id'], sensor_id=content['sensor_id'], arduino_id=content['arduino_id'])
    db.session.add(add_reading)
    db.session.commit()
    print(models.readings.query.all())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='8080',debug=True)