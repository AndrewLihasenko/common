from flask import Blueprint
from flask_restful import Api

from tenants.resource import GetTenants

tenants_bp = Blueprint('tenants', __name__)
api = Api(tenants_bp)

api.add_resource(GetTenants, '/tenants')