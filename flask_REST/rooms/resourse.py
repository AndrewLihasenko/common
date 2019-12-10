from flask import json, request
from flask_restful import Resource, fields, marshal_with, reqparse

from model import Rooms

rooms = [Rooms(21, 2, "available", 15),
         Rooms(22, 2, "closed", 15),
         Rooms(23, 2, "available", 20),
         Rooms(24, 2, "closed", 20),
         Rooms(25, 2, "available", 20),
         Rooms(26, 2, "closed", 50)]

rooms_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('filter')
parser.add_argument('room', type=int)
parser.add_argument('delete', type=int)


class GetRooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = parser.parse_args()
        for room in rooms:
            if args.get('room') == room.number:
                return room
            if args.get('filter') == 'available':
                return [room for room in rooms if room.status == 'available']
            elif args.get('filter') == 'closed':
                return [room for room in rooms if room.status == 'closed']
            return rooms

    @marshal_with(rooms_structure)
    def patch(self):
        data = json.loads(request.data)
        for room in rooms:
            if room.number == data.get('number'):
                room.status = data.get('status')
                return room, 'Room status updated'
        return 'Room status not updated'

    @marshal_with(rooms_structure)
    def post(self):
        data = json.loads(request.data)
        room = {**data}
        rooms.append(room)
        return rooms

    @marshal_with(rooms_structure)
    def delete(self):
        args = parser.parse_args()
        for room in rooms:
            if args.get('delete') == room.number:
                rooms.remove(room)
                return rooms, 'Rooms deleted'
        return 'Rooms not deleted'
