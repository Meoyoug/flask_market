from models.cart import Cart
from models.user import User
from flask import abort, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.order_detail import OrderDetail
from models.order import Order
from models.schemas import EditCartSchema
from db_connect import db

cart_bp = Blueprint('cart', 'cart', url_prefix='/cart', description='장바구니')

@cart_bp.route('/', methods=['GET'])
@jwt_required()
def get_cart():
    user_id= User.query.filter_by(user_id=get_jwt_identity()).first().id
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    if cart_items is None:
        abort(404, message="장바구니가 존재하지 않습니다.")
    cart_items = [item.to_dict() for item in cart_items]
    
    return jsonify({"cart": cart_items}), 200

@cart_bp.route('/', methods=['POST'])
@jwt_required()
def cart_to_order():
    user_id= User.query.filter_by(user_id=get_jwt_identity()).first().id
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    if cart_items is None:
        abort(404, message="장바구니가 존재하지 않습니다.")
    order = Order(
        user_id=user_id,
        total_price=0,
        is_paid=False,
    )
    db.session.add(order)
    db.session.flush()
    for item in cart_items:
        order_detail = OrderDetail(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
        )
        db.session.add(order_detail)
        order.total_price += item.quantity * item.product.price
    db.session.commit()

    return jsonify({"message": "order created", "order_id" : order.id}), 200

@cart_bp.route('/<int:product_id>', methods=['PUT'])
@cart_bp.arguments(EditCartSchema)
@jwt_required()
def update_cart(edit_num, product_id):
    user_id = User.query.filter_by(user_id=get_jwt_identity()).first().id
    cart = Cart.query.filter_by(user_id=user_id, product_id = product_id).first()
    if cart is None:
        abort(404, message="장바구니에 해당하는 상품이 존재하지 않습니다.")
    cart.quantity = edit_num['quantity']
    db.session.commit()

    return jsonify({"message": "product updated in cart"}), 200

@cart_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_cart(product_id):
    user_id = User.query.filter_by(user_id=get_jwt_identity()).first().id
    cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if cart is None:
        abort(404, message="장바구니에 해당하는 상품이 존재하지 않습니다.")
    db.session.delete(cart)
    db.session.commit()

    return jsonify({"message": "product deleted in cart"}), 200




