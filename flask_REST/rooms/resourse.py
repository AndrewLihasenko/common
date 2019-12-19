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
parser.add_argument('status')
parser.add_argument('number', type=int)
parser.add_argument('delete', type=int)


class GetRooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = parser.parse_args()
        for room in rooms:
            if args.get('number'):
                return [room for room in rooms if args.get('number') == room.number]
            elif args.get('status'):
                return [room for room in rooms if args.get('status') == room.status]
            return rooms, 200

    @marshal_with(rooms_structure)
    def patch(self):
        data = json.loads(request.data)
        for room in rooms:
            if room.number == data.get('number'):
                room.status = data.get('status')
                return room, 'Room status updated'
        return 'Room status not updated', 500

    @marshal_with(rooms_structure)
    def post(self):
        data = json.loads(request.data)
        numbers = [room.number for room in rooms]
        if data.get('number') in numbers:
            raise Exception('This room number exist', 500)
        elif data.get('level') < 0 or data.get('price') < 0:
            raise Exception('You entered negative number', 500)
        new_room = {**data}
        rooms.append(new_room)
        return rooms, 200

    @marshal_with(rooms_structure)
    def delete(self):
        args = parser.parse_args()
        for room in rooms:
            if args.get('delete') == room.number:
                rooms.remove(room)
                return rooms, 'Rooms deleted'
        return 'Rooms not deleted', 500
