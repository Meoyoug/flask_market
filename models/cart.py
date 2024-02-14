from db import db
_db = db


class cart(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: str = _db.Column(_db.String(30), _db.ForeignKey('user.user_id'))
    product_id: int = _db.Column(_db.Integer, _db.ForeignKey('product.id'))
    quantity: int = _db.Column(_db.Integer, nullable=False)
    
    def __init__(self, user_id: str, product_id: int,quantity: int):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity