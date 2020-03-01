from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://stef@project1db:Thisisstup1d@project1db.mysql.database.azure.com/proj1db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
        __tablename__ = 'users'
        user_id = db.Column('user_id', db.Integer, primary_key=True)
        password = db.Column('password', db.Unicode)
        email = db.Column('email', db.Unicode, index=True, unique=True)
        book_list_id = db.Column('book_list_id', db.Integer)

class Bookss(db.Model):
        __tablename__ = 'books'
        book_id = db.Column('book_id', db.Integer, primary_key=True)
        title = db.Column('title', db.Unicode)
        author = db.Column('author', db.Unicode)
