from db import db
_db = db


class order(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: str = _db.Column(_db.String(30), _db.ForeignKey('user.user_id'))
    total_price: float = _db.Column(_db.Float, nullable=False, default=0)
    is_paid: bool = _db.Column(_db.Bool, nullable=False)
    
    def __init__(self, user_id: int, total_price: float,is_paid: bool):
        self.user_id = user_id
        self.total_price = total_price
        self.is_paid = is_paid