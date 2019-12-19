from flask import Blueprint
from flask_restful import Api

from rooms.resourse import GetRooms

rooms_bp = Blueprint("rooms", __name__)
api = Api(rooms_bp)

api.add_resource(GetRooms, '/rooms')
