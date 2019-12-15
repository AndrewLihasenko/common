from flask import Blueprint
from flask_restful import Api

from tenants.resource import GetTenants, TenantRooms

tenants_bp = Blueprint('tenants', __name__)
api = Api(tenants_bp)

api.add_resource(GetTenants, '/tenants', '/tenants/<int:tenant_id>')
api.add_resource(TenantRooms, '/tenant_rooms/<int:tenant_id>')
