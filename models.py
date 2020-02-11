from app import db
from datetime import datetime
class target(db.Model):
  #  Env_var_i
    id = db.Column(db.Integer(), primary_key=True)
    target_Val = db.Column(db.Integer())
    time_from = db.Column(db.DateTime())
    time_to = db.Column(db.DateTime())

class user(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

class target_cycle(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
   # Target = 
    time_of_day = db.Column(db.DateTime())
   # account_id = 

class env_var(db.Model):
    label = db.Column(db.String(), primary_key=True)
    unit = db.Column(db.String())

class readings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    time = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    #Env_var_id =
    var_val = db.Column(db.Integer())
    env_var_id = db.Column(db.String(),db.ForeignKey("env_var.label"))
    env_var = db.relationship(
       'env_var', backref='Readings')


    

    