from ast import Try
from enum import unique
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Departments(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    employees = db.relationships('Employees', backref='department', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)