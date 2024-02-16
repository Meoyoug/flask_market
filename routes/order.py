from flask import jsonify, request, abort
from flask_smorest import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.order import Order
from models.user import User
from models.order_detail import OrderDetail
from models.schemas import OrderHandlerSchema
from models.product import Product
from models.cart import Cart
from db_connect import db
import random

order_bp = Blueprint('order','order', url_prefix='/order', description='주문하기')

@order_bp.route('/<int:order_id>', methods=['POST'])
@order_bp.arguments(OrderHandlerSchema)
@jwt_required()
def order_handler(data, order_id):
    user_id = User.query.filter_by(user_id=get_jwt_identity()).first().id
    # 결제 성공시 장바구니 삭제, 결제완료 업데이트
    if data['is_paid'] == True:
        Cart.query.filter_by(user_id=user_id).delete()
        Order.query.filter_by(id=order_id).first().is_paid = data['is_paid']
        db.session.commit()
        return jsonify({"message": "order success."}), 200
    # 결제 실패시 주문정보삭제 다시 장바구니 페이지로
    else :
        OrderDetail.query.filter_by(order_id=order_id).delete()
        Order.query.filter_by(id=order_id).delete()
        db.session.commit()
        return jsonify({"message": "Order failed because The payment has failed."}), 200
    

@order_bp.route('/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    user_id = User.query.filter_by(user_id=get_jwt_identity()).first().id
    order = Order.query.filter_by(id=order_id, user_id=user_id).first()
    if order is None:
        abort(404, message="order not found.")
    order = order.to_dict()
    order_details = OrderDetail.query.filter_by(id=order_id).all()
    if order_details is None:
        abort(404, message="order detail not found.")
    order_details = [order_detail.to_dict() for order_detail in order_details]
    return jsonify({"order" : order, "order_detail" : order_details}), 200
