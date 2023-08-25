from myproject import login_manager, app, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

##UserMixin is a tool within flask_login which will help in login management of a user

## we will also create another method that will get a user which is logged in to it's own page

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String)
    username=db.Column(db.String)
    password=db.Column(db.String)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f"Hello user {self.username}. Welcome to your homepage. You are logged in with {self.email}."

    def check_hash_password(self,password):
        return check_password_hash(self.password_hash,password)

