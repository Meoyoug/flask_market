from marshmallow import Schema, fields

class CartSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    user_id = fields.Str(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class OrderDetailSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    order_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    user_id = fields.Str(required=True)
    total_price = fields.Float(required=True)
    is_paid = fields.Bool(required=True)

class ProductSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    productname = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

class UserSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    user_id = fields.Str(required=True)
    username = fields.Str(required=True)
    password_hash = fields.Str(required=True)

class LoginSchema(Schema):
    user_id = fields.Str(required=True)
    password = fields.Str(required=True)

class RegisterSchema(Schema):
    user_id = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

