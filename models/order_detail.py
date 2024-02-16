from db_connect import db
_db = db


class OrderDetail(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    order_id: int = _db.Column(_db.Integer, _db.ForeignKey('order.id'))
    product_id: int = _db.Column(_db.Integer, _db.ForeignKey('product.id'))
    quantity: int = _db.Column(_db.Integer, nullable=False)
    
    order = _db.relationship('Order', back_populates='order_details', lazy='select')
    product = _db.relationship('Product', back_populates='order_details', lazy='select')
    def __init__(self, order_id: int, product_id: int,quantity: int):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }