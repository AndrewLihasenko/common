from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from model import RoomsModel, StaffModel
from marshal_structure import rooms_structure, staff_structure
from parcer import staff_parser


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        name = staff_parser.parse_args().get("name")
        if name:
            employee = StaffModel.query.filter(StaffModel.name == name).all()
            return employee, 200
        return StaffModel.query.all(), 200

    @marshal_with(staff_structure)
    def post(self):
        data = json.loads(request.data)
        if StaffModel.query.filter(
                StaffModel.passport_id == data.get('passport_id')).first():
            raise Exception('This passport id exist', 500)
        elif data.get('salary') < 0:
            raise Exception('You entered negative salary', 500)
        employee = StaffModel(**data)
        db.session.add(employee)
        db.session.commit()
        return StaffModel.query.all(), 200

    @marshal_with(staff_structure)
    def patch(self, staff_id):
        data = json.loads(request.data)
        employee = StaffModel.query.get(staff_id)
        if employee:
            employee.salary = data.get('salary')
            employee.position = data.get('position')
            db.session.commit()
            return employee, 200
        raise ValueError("Sorry. Nothing change. Enter correct staff id", 500)

    @marshal_with(staff_structure)
    def delete(self, staff_id):
        employee = StaffModel.query.get(staff_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return "Employee deleted", 200
        raise ValueError("Sorry. Nothing change. Enter correct staff id", 500)


class StaffRoom(Resource):
    def post(self):
        data = json.loads(request.data)
        staff_name = data.get("staff_name")
        room_number = data.get("room_number")
        staff = StaffModel.query.filter_by(name=staff_name).first()
        room = RoomsModel.query.filter_by(number=room_number).first()
        staff.works.append(room)
        db.session.commit()
        return f"Room {room.number} serve {staff.name}", 200

    @marshal_with(rooms_structure)
    def get(self):
        args = staff_parser.parse_args(strict=True)
        staff = StaffModel.query.filter_by(name=args.get("name")).first()
        return staff.works, 200
