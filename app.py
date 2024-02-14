from flask import Flask
from flask_smorest import Api
from db import db

app = Flask(__name__)
db.init_app(app)

# OpenAPI 관련 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:0000@localhost:3306/ shop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)