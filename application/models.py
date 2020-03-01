from application import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
        __tablename__ = 'users'
        user_id = db.Column('user_id', db.Integer, primary_key=True)
        email = db.Column('email', db.Unicode,nullable=False, unique=True)
        password = db.Column('password', db.Unicode, nullable=False)
        book_list_id = db.Column('book_list_id', db.Integer)
        def __repr__(self):
            return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])

class Bookss(db.Model):
        __tablename__ = 'books'
        book_id = db.Column('book_id', db.Integer, primary_key=True)
        title = db.Column('title', db.Unicode)
        author = db.Column('author', db.Unicode)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
