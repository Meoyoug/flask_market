from db import db
_db = db


class product(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    product_name: str = _db.Column(_db.String(81), nullable=False)
    price: float = _db.Column(_db.Float, nullable=False, default=0)
    description: str = _db.Column(_db.String(200))
    
    def __init__(self, product_name: str, price: float,description: str):
        self.product_name = product_name
        self.price = price
        self.description = description