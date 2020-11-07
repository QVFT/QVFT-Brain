from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timezone


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgres://jlitqmyw:eF1Ju2K3hX9jw-O9iG_NsiHSrSFf3EIb@drona.db.elephantsql.com:5432/jlitqmyw'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

import models #change in python syntax
from models import *
def serialize(obj):
    result = {c.key: getattr(obj, c.key)
              for c in db.inspect(obj).mapper.column_attrs}
    # result.pop("password", None)  # remove password if exists
    # for key in result:  # convert enums to strings
    #     if isinstance(result[key], enum.Enum):
    #         result[key] = str(result[key]).split('.')[-1]
    return result

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/add')
def add():
    return render_template('input.html')


@app.route('/add',methods=['POST'])
def readingadd():
    db.session.flush()
    var_val = request.form.get('var_val')
    env_var_id = request.form.get('env_var_id')
    shelf_id = request.form.get('shelf_id')
    sensor_id = request.form.get('sensor_id')
    arduino_id = request.form.get('arduino_id')
    add_reading =readings(var_val=var_val, env_var_id=env_var_id, shelf_id=shelf_id, sensor_id=sensor_id, arduino_id=arduino_id)
    print(add_reading)
    db.session.add(add_reading)
    db.session.commit()
    print(readings.query.all())
    return "xd"

@app.route('/gucci')
def xd():
    return xd


@app.route('/gucci/<label>')
def see_reading(label):
    xd = label.split(",")
    var_val = xd[0]
    env_var_id = xd[1]
    shelf_id = xd[2]
    sensor_id = xd[3]
    arduino_id = xd[4]
    add_reading =readings(var_val=var_val, env_var_id=env_var_id, shelf_id=shelf_id, sensor_id=sensor_id, arduino_id=arduino_id)
    print(add_reading)
    db.session.add(add_reading)
    db.session.commit()
    print(readings.query.all())
    return "xd"
    return str(xd)

@app.route('/view')
def readings_list():
    readings = db.session.execute("SELECT * FROM readings ORDER BY id")
    return render_template('reading_output.html', readings=readings)
@app.route("/api/readings/<label>", methods=['POST'])
def post_readings(label):
    print (request.is_json)
    content = request.get_json()
    print (content)
    print('JSON posted')
    add_reading = readings(var_val=content['var_val'], env_var_id=content['env_var_id'], shelf_id=content['shelf_id'], sensor_id=content['sensor_id'], arduino_id=content['arduino_id'])
    db.session.add(add_reading)
    db.session.commit()
    print(readings.query.all())
    return "reading posted!"

@app.route("/api/readings/<label>", methods=['GET'])
def get_readings(label):
    start_time = datetime.fromtimestamp(int(request.args.get('start_time')),timezone.utc)
    end_time = datetime.fromtimestamp(int(request.args.get('end_time')),timezone.utc)
    # qry = DBSession.query(User).filter(User.birthday.between('1985-01-17', '1988-01-17'))
    data = db.session.query(readings).filter(readings.time.between(start_time, end_time)).all()
    print(data)
    return jsonify([serialize(reading) for reading in data])

if __name__ == '__main__':
    #app.run(host="127.0.0.1", port='8080',debug=True)
    app.run(host="0.0.0.0", port="80", debug=True)
