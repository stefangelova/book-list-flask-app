from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://stef@project1db:Thisisstup1d@project1db.mysql.database.azure.com/proj1db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
