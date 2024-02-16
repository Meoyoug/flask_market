from db_connect import db
_db = db


class Product(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    product_name: str = _db.Column(_db.String(81), nullable=False)
    price: float = _db.Column(_db.Float, nullable=False, default=0)
    description: str = _db.Column(_db.String(200), nullable=True)

    carts = _db.relationship('Cart', back_populates='product', lazy='dynamic')
    order_details = _db.relationship('OrderDetail', back_populates='product', lazy='dynamic')

    def __init__(self, product_name: str, price: float,description: str):
        self.product_name = product_name
        self.price = price
        self.description = description

    def dict_to(self, product):
        return {
            "id" : product.id,
            "product_name": product.product_name,
            "price": product.price,
            "description": product.description
        }
