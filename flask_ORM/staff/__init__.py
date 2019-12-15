from flask import Blueprint
from flask_restful import Api

from staff.resource import GetStaff, StaffRoom

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)

api.add_resource(GetStaff, '/staff', '/staff/<int:staff_id>')
api.add_resource(StaffRoom, '/staff_works')
