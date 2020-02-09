from app import db

class Target():
  #  Env_var_i
    Target_Val = db.Column(db.Integer())
    Time_from = db.Column(db.DateTime())
    Time_to = db.Column(db.DateTime())

class User():
    user_id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

class Target_cycle():
    ID = db.Column(db.Integer(), primary_key=True)
   # Target = 
    time_of_day = db.Column(db.DateTime())
   # account_id = 

class Readings():
    time = db.Column(db.DateTime())
    #Env_var_id =
    var_val = db.Column(db.Integer())
