from datetime import datetime
from cardination import db,login_manager,app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    patient = db.relationship('Patient',backref = 'user',lazy = True)
    doctor = db.relationship('Doctor',backref = 'user',lazy = True)

    def __repr__(self):
        return f"User('{self.id}')"

class Patient(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('user.id'), primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    weight = db.Column(db.Integer, unique = False, nullable = True)
    height = db.Column(db.Integer, unique = False, nullable = True)
    gender = db.Column(db.String(1), unique = False, nullable = False)
    bloodgroup = db.Column(db.String(10), unique = False, nullable = True)
    dob = db.Column(db.String(20), unique = False, nullable = True)

    def __repr__(self):
        return f"Patient('{self.username}', '{self.email}', '{self.image_file}', '{self.weight}', '{self.height}', '{self.gender}', '{self.bloodgroup}', '{self.dob}')"

class Doctor(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    specialization= db.Column(db.String(60), nullable = False)
    degree= db.Column(db.String(60), nullable = False)
    gender= db.Column(db.String(1), nullable = True)
    phone_number= db.Column(db.String(60), nullable = False)
    address= db.Column(db.String(120), nullable = True)

    def __repr__(self):
        return f"Doctor('{self.username}', '{self.email}', '{self.image_file}', '{self.specialization}', '{self.degree}', '{self.gender}', '{self.phone_number}', '{self.address}')"
