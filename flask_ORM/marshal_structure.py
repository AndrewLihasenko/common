from flask_restful import fields

rooms_structure = {
    "id": fields.Integer,
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer
}

staff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer,
    "works": fields.Nested(rooms_structure)
}

tenants_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    'city': fields.String,
    'street': fields.String,
    "rooms": fields.Nested(rooms_structure)
}
