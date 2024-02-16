from flask import Flask, render_template
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from config.constants import SQLALCHEMY_DATABASE_URI
from db_connect import db
from routes.user import user_bp
from models.user import User
from models.product import Product
from models.cart import Cart
from models.order import Order
from models.order_detail import OrderDetail

app = Flask(__name__)
jwt = JWTManager(app)

#db 연결
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# OpenAPI 관련 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # SQLALCHEMY 에서 사용할 db url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # SQLALCHEMY 이벤트를 처리하는 옵션
app.config["SQLALCHEMY_ECHO"] = True  # ddl을 볼 수 있는 옵션
app.config['DEBUG'] = True  # debug모드 옵션

app.config['SECRET_KEY'] = 'secret1@2#4%'

_db=db
_db.init_app(app)
api = Api(app)
api.register_blueprint(user_bp)

if __name__ == '__main__':
    with app.app_context():
        _db.create_all()

    app.run(host='localhost', port=5000, debug=True)