from db import db
_db = db


class user(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: str = _db.Column(_db.String(30), nullable=False ,unique = True)
    username: str = _db.Column(_db.String(80), nullable=False)
    password_hash: str = _db.Column(_db.String(255), nullable=False)
    def __init__(self,user_id: str, username: str, password_hash: str):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        