from flask import json, request
from flask_restful import Resource, marshal_with

from db import db
from marshal_structure import rooms_structure
from parcer import rooms_parser
from model import RoomsModel


class GetRooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        room_number = rooms_parser.parse_args().get("room_num")
        room_status = rooms_parser.parse_args().get("room_status")
        if room_number:
            room = RoomsModel.query.filter(
                RoomsModel.number == room_number).first()
            return room, 200
        if room_status:
            room = RoomsModel.query.filter(
                RoomsModel.status == room_status).all()
            return room, 200
        return RoomsModel.query.all(), 200

    @marshal_with(rooms_structure)
    def patch(self, room_id):
        data = json.loads(request.data)
        room = RoomsModel.query.get(room_id)
        if room:
            room.status = data.get('status')
            db.session.commit()
            return room, 200
        raise ValueError("Sorry. Nothing change. Enter correct room id", 500)

    @marshal_with(rooms_structure)
    def post(self):
        data = json.loads(request.data)
        if RoomsModel.query.filter(
                RoomsModel.number == data.get('number')).first():
            raise Exception('This room number exist', 500)
        elif data.get('level') < 0 or data.get('price') < 0:
            raise Exception('You entered negative number', 500)
        room = RoomsModel(**data)
        db.session.add(room)
        db.session.commit()
        return RoomsModel.query.all(), 200

    @marshal_with(rooms_structure)
    def delete(self, room_id):
        room = RoomsModel.query.get(room_id)
        if room:
            db.session.delete(room)
            db.session.commit()
            return "Room deleted", 200
        raise ValueError("Sorry. Nothing change. Enter correct room id", 500)