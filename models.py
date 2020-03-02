from app import db
from datetime import datetime
class target(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    target_Val = db.Column(db.Integer())
    time_from = db.Column(db.DateTime())
    time_to = db.Column(db.DateTime())
    env_var_id = db.Column(db.String(),db.ForeignKey("env_var.label"))
    env_var = db.relationship('env_var', backref='target')

class user(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

class target_cycle(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    value = db.Column(db.Integer())
    time_of_day = db.Column(db.DateTime())
    env_var_id  = db.Column(db.String(),db.ForeignKey("env_var.label"))
    user_id =  db.Column(db.String(),db.ForeignKey("user.user_id"))
    env_var = db.relationship('env_var', backref='readings')
    user = db.relationship('user', backref='target_cycle')


class env_var(db.Model):
    label = db.Column(db.String(), primary_key=True)
    unit = db.Column(db.String())
    has_targets = db.column(db.Boolean())


class readings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    time = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    var_val = db.Column(db.Integer())
    env_var_id = db.Column(db.String(),db.ForeignKey("env_var.label"))
    env_var = db.relationship(
       'env_var', backref='readings')
    shelf_id = db.Column(db.Integer())
    sensor_id = db.Column(db.Integer())
    arduino_id = db.Column(db.Integer())


    

    