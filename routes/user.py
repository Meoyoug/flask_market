from flask import jsonify, request, abort, render_template
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import check_password_hash
from models.user import User
from db_connect import db
from blocklist import BLOCKLIST, add_to_blocklist
from models.schemas import LoginSchema, RegisterSchema

user_bp = Blueprint('user','user', url_prefix='/users', description='User info')


# 로그인 - POST 메소드 사용, jwt 인증방식
@user_bp.route('/login', methods=['POST'])
@user_bp.arguments(LoginSchema)
def login_user(form):
    user_id = form['user_id']
    password = form['password']

    if not user_id or not password:
        abort(400, description="Missing user_id or password")

    user = User.query.filter_by(user_id=user_id).first()

    if not user or not check_password_hash(user.password_hash, password):
        abort(401, description="Invalid user_id or password")

    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

# 회원가입 - POST 메소드 사용
@user_bp.route('/register', methods=['POST'])
@user_bp.arguments(RegisterSchema)
def register_user(form):
    user_id = form['user_id']
    username = form['username']
    password = form['password']


    if not user_id or not username or not password:
        abort(400, message="Missing user_id, username or password")
    
    user = User.from_dto(form)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg":"successfully registered"}), 200

# 사용자 컨트롤러 - 로그아웃, 사용자 정보 조회, 사용자 삭제
@user_bp.route('/my-page', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    user = User.query.filter_by(user_id=current_user).first()

    return jsonify({"user_id": current_user, "username": user.username}), 200

@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout_user():  
    jti = get_jwt()["jti"]
    add_to_blocklist(jti)  # 토큰을 블랙리스트에 추가합니다.
    print(BLOCKLIST)
    return jsonify({'message': 'Logged out successfully'}), 200

@user_bp.route('/delete-account', methods=['DELETE'])
@jwt_required()
def delete_user(): 
    user = User.query.filter_by(user_id=get_jwt_identity()).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200