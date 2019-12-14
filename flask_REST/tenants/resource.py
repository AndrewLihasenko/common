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
    "sex": fields.String,
    "address": fields.Nested(address_structure),
    "room_number": fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('passport_id')
parser.add_argument('sex')
parser.add_argument('delete')


class GetTenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        args = parser.parse_args()
        for tenant in tenants:
            if args.get('passport_id'):
                return [tenant for tenant in tenants if args.get('passport_id') == tenant.passport_id]
            elif args.get('sex'):
                return [tenant for tenant in tenants if args.get('sex') == tenant.sex]
        return tenants, 200

    @marshal_with(tenants_structure)
    def post(self):
        data = json.loads(request.data)
        oll_passport_id = [tenant.passport_id for tenant in tenants]
        if data.get('passport_id') in oll_passport_id:
            raise Exception('This passport_id exist', 500)
        elif data.get('room_number') < 0 or data.get('age') < 0:
            raise Exception('You entered negative number', 500)
        new_tenant = {**data}
        tenants.append(new_tenant)
        return tenants, 200

    @marshal_with(tenants_structure)
    def patch(self):
        data = json.loads(request.data)
        for tenant in tenants:
            if tenant.passport_id == data.get('passport_id'):
                tenant.room_number = data.get('room_number')
                return tenant, 'Room number updated'
        return 'Room number not updated', 500

    @marshal_with(tenants_structure)
    def delete(self):
        args = parser.parse_args()
        for tenant in tenants:
            if args.get('delete') == tenant.passport_id:
                tenants.remove(tenant)
                return tenants, 'Tenant deleted'
        return 'Tenant not deleted', 500
