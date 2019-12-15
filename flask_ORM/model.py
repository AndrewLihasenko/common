from db import db


class RoomsModel(db.Model):
    __tablename__ = "rooms_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    level = db.Column(db.Integer)
    status = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants_table.id'))


staff_works = db.Table(
    "staff_works",
    db.Column("staff_id", db.Integer, db.ForeignKey("staff_table.id")),
    db.Column("room_id", db.Integer, db.ForeignKey("rooms_table.id"))
)


class StaffModel(db.Model):
    __tablename__ = "staff_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    passport_id = db.Column(db.String(80), unique=True, nullable=False)
    position = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Integer)
    works = db.relationship("RoomsModel", secondary=staff_works, backref="staff_ref")


class TenantsModel(db.Model):
    __tablename__ = "tenants_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    passport_id = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    street = db.Column(db.String(80), nullable=False)
    rooms = db.relationship('RoomsModel', backref='tenant_ref')
