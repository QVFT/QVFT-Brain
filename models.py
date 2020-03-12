from app import db
from datetime import datetime
class target(db.Model):
    # attributes
    id = db.Column(db.Integer(), primary_key=True)
    target_Val = db.Column(db.Integer())
    time_from = db.Column(db.DateTime())
    time_to = db.Column(db.DateTime())
    env_var_id = db.Column(db.String(),db.ForeignKey("env_var.label"))


class user(db.Model):
    #attributes 
    user_id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))
    #relationships
    target_cycle = db.relationship('target_cycle', backref='user')

class target_cycle(db.Model):
    #attributes
    id = db.Column(db.Integer(), primary_key=True)
    value = db.Column(db.Integer())
    time_of_day = db.Column(db.DateTime())
    env_var_id  = db.Column(db.String(),db.ForeignKey("env_var.label"))
    user_id =  db.Column(db.Integer(),db.ForeignKey("user.user_id"))




class env_var(db.Model):
    #attributes
    label = db.Column(db.String(), primary_key=True)
    unit = db.Column(db.String())
    has_targets = db.Column(db.Boolean())

    #relationships
    readings = db.relationship(
       'readings', backref='env_var')
    target = db.relationship('target', backref='env_var')
    target_cycle = db.relationship('target_cycle', backref='env_var')
    


class readings(db.Model):
    # attributes
    id = db.Column(db.Integer(), primary_key=True)
    time = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    var_val = db.Column(db.Integer())
    env_var_id = db.Column(db.String(),db.ForeignKey("env_var.label"))
    shelf_id = db.Column(db.Integer())
    sensor_id = db.Column(db.Integer())
    arduino_id = db.Column(db.Integer())


    

    