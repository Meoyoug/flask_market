from db_connect import db
from werkzeug.security import generate_password_hash
_db = db


class User(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: str = _db.Column(_db.String(30), nullable=False ,unique = True)
    username: str = _db.Column(_db.String(80), nullable=False)
    password_hash: str = _db.Column(_db.String(255), nullable=False)

    orders = _db.relationship('Order', back_populates='user', lazy='dynamic')
    carts = _db.relationship('Cart', back_populates='user', lazy='dynamic')
    
    def __init__(self,user_id: str, username: str, password_hash: str):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
    
    @staticmethod
    def from_dto(register_form: dict):
        return User(
            user_id=register_form['user_id'],
            username=register_form['username'],
            password_hash=generate_password_hash(register_form['password'])
        )