from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    tel = db.Column(db.String(20), nullable=False, unique=True)
    piva = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, surname, tel, piva, email, password):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.piva = piva
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Durata în minute

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idCustomer = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    idService = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    notes = db.Column(db.String(255))
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    recapito = db.Column(db.String(20), nullable=False)
    noteStaff = db.Column(db.String(255))

    duration = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(20), default='New', nullable=False)

    customer = db.relationship('Customer', backref='appointments')
    service = db.relationship('Service', backref='appointments')

    def __init__(self, idCustomer, idService, notes, datetime, duration, recapito, noteStaff, state='new'):
        self.idCustomer = idCustomer
        self.idService = idService
        self.notes = notes
        self.datetime = datetime
        self.duration = duration
        self.state = state
        self.recapito = recapito
        self.noteStaff = noteStaff