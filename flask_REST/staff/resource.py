from flask import json, request
from flask_restful import Resource, reqparse, fields, marshal_with

from model import Staff

staff = [Staff("Jack", "AA1111", "waiter", 100),
         Staff("Julia", "AA2222", "cook", 120),
         Staff("Mike", "AA3333", "security", 80),
         Staff("Wilma", "AA4444", "chambermaid", 80),
         Staff("Kate", "AA5555", "reception", 150)]

staff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('passport_id')
parser.add_argument('position')
parser.add_argument('delete')


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = parser.parse_args()
        for employee in staff:
            if args.get('passport_id'):
                return [employee for employee in staff if args.get('passport_id') == employee.passport_id]
            if args.get('position'):
                return [employee for employee in staff if args.get('position') == employee.position]
            return staff, 200

    @marshal_with(staff_structure)
    def post(self):
        data = json.loads(request.data)
        oll_passport_id = [employee.passport_id for employee in staff]
        if data.get('passport_id') in oll_passport_id:
            raise Exception('This passport_id exist', 500)
        elif data.get('salary') < 0:
            raise Exception('You entered negative salary number', 500)
        new_employee = {**data}
        staff.append(new_employee)
        return staff, 200

    @marshal_with(staff_structure)
    def patch(self):
        data = json.loads(request.data)
        for employee in staff:
            if employee.passport_id == data.get('passport_id'):
                employee.salary = data.get('salary')
                return employee, 'Salary updated'
        return 'Salary not updated', 500

    @marshal_with(staff_structure)
    def delete(self):
        args = parser.parse_args()
        for employee in staff:
            if args.get('delete') == employee.passport_id:
                staff.remove(employee)
                return staff, 'Info about employee deleted'
        return 'Info about employee not deleted', 500
