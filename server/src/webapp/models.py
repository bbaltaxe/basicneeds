from flask import Flask, current_app, g
from flask_sqlalchemy import SQLAlchemy

from webapp import db


class UserMixin(object):
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'User {self.id}: {self.username}'

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
        }


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Admin {self.id}: {self.username}'

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
