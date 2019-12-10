from flask import json, request
from flask_restful import Resource, marshal_with, fields, reqparse

from model import Tenants

tenants = [Tenants("John", "BA1111", 25, "male", {'city': 'Kyiv', 'street': 'Poshtova'},  21),
           Tenants("Andrew", "BA2222", 35, "male", {'city': 'Zaporizhzhia', 'street': 'Kuybisheva'}, 25),
           Tenants("Juliya", "BA3333", 28, "female", {'city': 'Kharkiv', 'street': 'Tolstova'}, 22),
           Tenants("Tom", "BA4444", 40, "male", {'city': 'Rivne', 'street': 'Mokraja'}, 29),
           Tenants("Margo", "BA5555", 35, "female", {'city': 'Lviv', 'street': 'Mazepi'}, 24),
           Tenants("Andrew", "BA6666", 39, "male", {'city': 'Kyiv', 'street': 'Franko'}, 28)]

address_structure = {
    'city': fields.String(attribute='city'),
    'street': fields.String(attribute='street')
}

tenants_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "address": fields.Nested(address_structure),
    "room_number": fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('passport_id')
parser.add_argument('delete')


class GetTenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        args = parser.parse_args()
        for tenant in tenants:
            if args.get('passport_id') == tenant.passport_id:
                return tenant
        return tenants

    @marshal_with(tenants_structure)
    def post(self):
        data = json.loads(request.data)
        tenant = {**data}
        tenants.append(tenant)
        return tenants

    @marshal_with(tenants_structure)
    def patch(self):
        data = json.loads(request.data)
        for tenant in tenants:
            if tenant.passport_id == data.get('passport_id'):
                tenant.room_number = data.get('room_number')
                return tenant, 'Room number updated'
        return 'Room number not updated'

    @marshal_with(tenants_structure)
    def delete(self):
        args = parser.parse_args()
        for tenant in tenants:
            if args.get('delete') == tenant.passport_id:
                tenants.remove(tenant)
                return tenants, 'Tenant deleted'
        return 'Tenant not deleted'
