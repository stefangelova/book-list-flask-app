from application import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
        __tablename__ = 'users'
        user_id = db.Column('user_id', db.Integer, primary_key=True)
        first_name = db.Column(db.String(30), nullable=False)
        last_name = db.Column(db.String(30), nullable=False)
       	email = db.Column('email',db.String(150), nullable=False, unique=True)
        password = db.Column('password', db.String(500), nullable=False)

        book_list_id = db.Column('book_list_id', db.Integer, db.ForeignKey('booklist.book_list_id'), nullable=False)

        def get_id(self):
            return self.user_id

        def __repr__(self):
            return ''.join([
                           'UserID:' , str(self.id), '\r\n',
                           'Email:' , self.email
                           ])

class Bookss(db.Model):
        __tablename__ = 'books'
        book_id = db.Column('book_id', db.Integer, primary_key=True)
        title = db.Column('title', db.String(250))
        author = db.Column('author', db.String(250))
        rating = db.Column('average_rating', db.Unicode(10))

        def get_id(self):
            return self.book_id

        def __repr__(self):
            return ''.join([
		'Titles:', self.title, '\r\n',
	        'Authors:', self.author, '\r\n',
                'Ratings:', self.average_rating, '\r\n'
                ])
class Booklist(db.Model):
        __tablename__ = 'booklist'
        book_list_id = db.Column('book_list_id', db.Integer, primary_key=True)

        book_id = db.Column('book_id', db.Integer, db.ForeignKey('books.book_id'), nullable=False)
        user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), nullable=False)

        def get_id(self):
            return self.book_list_id


   # def __repr__(self):
    #    return ''.join([
     #               ])


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
