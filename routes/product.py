from models.product import Product
from models.cart import Cart
from models.user import User
from flask import abort, jsonify
from flask_smorest import Blueprint
from models.schemas import AddToCartSchema, CreateProductSchema
from db_connect import db
from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint('product', 'product', url_prefix='/products', description='제품 정보')

@product_bp.route('/list/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    product = product.dict_to(product)
    if product is None:
        abort(404, message="제품이 존재하지 않습니다.")
    return jsonify({"product": product}), 200

@product_bp.route('/list', methods=['GET'])
def update_product():
    products = Product.query.all()
    products = [product.dict_to(product) for product in products]
    print(products)
    return jsonify({"product": products}), 200

@product_bp.route('/add', methods=['POST'])
@product_bp.arguments(CreateProductSchema)
def create_product(product_data):
    product = Product(
        product_name = product_data['productname'],
        price = product_data['price'],
        description = product_data['description']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"msg":"Success add product."}), 200

@product_bp.route('/add-to-cart', methods=['POST'])
@product_bp.arguments(AddToCartSchema)
@jwt_required()
def add_to_cart(data):
    user_id = User.query.filter_by(user_id=get_jwt_identity()).first().id
    cart = Cart(
        user_id = user_id,
        product_id = data['product_id'],
        quantity = data['quantity']
    )
    db.session.add(cart)
    db.session.commit()
    return jsonify({"msg":"Success add to cart."}), 200
