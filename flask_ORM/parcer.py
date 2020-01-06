from flask_restful import reqparse

rooms_parser = reqparse.RequestParser()
rooms_parser.add_argument('room_status')
rooms_parser.add_argument('room_num', type=int)
rooms_parser.add_argument('delete', type=int)

staff_parser = reqparse.RequestParser()
staff_parser.add_argument('name')
staff_parser.add_argument('delete')

tenants_parser = reqparse.RequestParser()
tenants_parser.add_argument('passport_id')
tenants_parser.add_argument('delete')
