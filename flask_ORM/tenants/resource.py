from flask import json, request, current_app
from flask_restful import Resource, marshal_with

from db import db
from model import RoomsModel, TenantsModel
from marshal_structure import tenants_structure, rooms_structure
from parcer import tenants_parser


class GetTenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        passport_id = tenants_parser.parse_args().get("passport_id")
        if passport_id:
            tenant = TenantsModel.query.filter(
                TenantsModel.passport_id == passport_id).first()
            return tenant, 200
        return TenantsModel.query.all(), 200

    @marshal_with(tenants_structure)
    def post(self):
        data = json.loads(request.data)

        try:
            room_id = data.pop("room_id")
            room = RoomsModel.query.get(room_id)
            data["rooms"] = room
        except KeyError:
            current_app.logger.info("Room not created")

        if TenantsModel.query.filter(
                TenantsModel.passport_id == data.get('passport_id')).first():
            return 'This passport id exist', 400
        elif data.get('age') < 0:
            return 'You entered negative age number', 400
        tenant = TenantsModel(**data)
        try:
            db.session.add(tenant)
            db.session.commit()
        except (ConnectionError, PermissionError) as err:
            return err, 400
        return tenant, 201

    @marshal_with(tenants_structure)
    def patch(self, tenant_id):
        data = json.loads(request.data)
        tenant = TenantsModel.query.get(tenant_id)
        if tenant:
            tenant.name = data.get('name')
            try:
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return tenant, 201
        return "Sorry. Nothing change. Enter correct tenant id", 400

    @marshal_with(tenants_structure)
    def delete(self, tenant_id):
        tenant = TenantsModel.query.get(tenant_id)
        if tenant:
            try:
                db.session.delete(tenant)
                db.session.commit()
            except (ConnectionError, PermissionError) as err:
                return err, 400
            return "Employee deleted", 200
        return "Sorry. Nothing change. Enter correct tenant id", 400


class TenantRooms(Resource):
    @marshal_with(rooms_structure)
    def get(self, tenant_id):
        tenant = TenantsModel.query.get(tenant_id)
        return tenant.rooms, 200
