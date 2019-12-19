from flask import Blueprint
from flask_restful import Api

from staff.resource import GetStaff

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)

api.add_resource(GetStaff, '/staff')
