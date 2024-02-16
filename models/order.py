from db_connect import db
_db = db


class Order(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: int = _db.Column(_db.Integer, _db.ForeignKey('user.id'))
    total_price: float = _db.Column(_db.Float, nullable=False, default=0)
    is_paid: bool = _db.Column(_db.Boolean, nullable=False)
    
    user = _db.relationship('User', back_populates='orders', lazy='select')
    order_details = _db.relationship('OrderDetail', back_populates='order', lazy='dynamic')
    def __init__(self, user_id: int, total_price: float,is_paid: bool):
        self.user_id = user_id
        self.total_price = total_price
        self.is_paid = is_paid
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_price": self.total_price,
            "is_paid": self.is_paid
        }
