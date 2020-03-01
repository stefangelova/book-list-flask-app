from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://stef@project1db:Thisisstup1d@project1db.mysql.database.azure.com"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'YOU_SECRET_KEY'
#db = SQLAlchemy(app)

from application import routes

