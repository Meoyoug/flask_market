from db_connect import db
_db = db


class Cart(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id: int = _db.Column(_db.Integer, _db.ForeignKey('user.id'))
    product_id: int = _db.Column(_db.Integer, _db.ForeignKey('product.id'))
    quantity: int = _db.Column(_db.Integer, nullable=False)
    
    user = _db.relationship('User', back_populates='carts', lazy='select')
    product = _db.relationship('Product', back_populates='carts', lazy='select')
    
    def __init__(self, user_id : int, product_id: int,quantity: int):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
        }