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
parser.add_argument('delete')


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        args = parser.parse_args()
        for employee in staff:
            if args.get('passport_id') == employee.passport_id:
                return employee
        return staff

    @marshal_with(staff_structure)
    def post(self):
        data = json.loads(request.data)
        employee = {**data}
        staff.append(employee)
        return staff

    @marshal_with(staff_structure)
    def patch(self):
        data = json.loads(request.data)
        for employee in staff:
            if employee.passport_id == data.get('passport_id'):
                employee.salary = data.get('salary')

    @marshal_with(staff_structure)
    def delete(self):
        args = parser.parse_args()
        for employee in staff:
            if args.get('delete') == employee.passport_id:
                staff.remove(employee)
                return staff
