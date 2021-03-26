from webapp import app, db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import enum

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    pw = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Student( '{self.id}', '{self.name}', '{self.email}' )"
    

class StudentServiceList(db.Model):
    pkey = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('Student.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('Service.id'))

    def __repr__(self):
        return f"('{self.student_id}', '{self.service_id}')"
    
#https://www.michaelcho.me/article/using-python-enums-in-sqlalchemy-models
class IntEnum (db.TypeDecorator):
    """
    Enables passing in a python enum and storing the enum's *value*
    in the db. 

    The Default would have sotred the enum's *name*(string)
    """
    impl = db.Integer

    def __init__(self, enumtype, *args, **kwargs):
        super(IntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value
        return value.value
    
    def process_result_value(self, value, dialect):
        return self._enumtype(value)

class Schools(enum.IntEnum):
    UCB = 1
    UCD = 2
    UCI = 3
    UCLA = 4
    UCM = 5
    UCR = 6
    UCSD = 7
    UCSF = 8
    UCSB = 9
    UCSC = 10

class Service(db.Model):
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    campus = db.Column(IntEnum(Schools))
    category = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Service('{self.name}', )"

