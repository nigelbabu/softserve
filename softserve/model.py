from softserve import db
from datetime import datetime

class User(db.Model):
        __tablename__ = 'User'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(100), unique=True, nullable=False)
        token = db.Column(db.String(1000))
        email = db.Column(db.String(100), unique=True)
        name = db.Column(db.String(100))
        vm = db.relationship('Vm', backref='user', lazy='dynamic')
        def __repr__(self):
            return '<user {}>'.format(self.username)

class Node_request(db.Model):
    __tablename__ = 'Node_request'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    node_name = db.Column(db.String(100), unique=True, nullable=False)
    node_counts = db.Column(db.Integer, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    pubkey = db.Column(db.VARCHAR(1024), nullable=False)
    vms = db.relationship('Vm', backref='details', lazy='dynamic')
    def as_dict(self):
        return{
        "node_name" : self.node_name,
        "node_counts" : self.nodes,
        "hours" : self.hours
        }

class Vm(db.Model):
    __tablename__ = 'Vm'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip_address = db.Column(db.VARCHAR(45), unique=True)
    vm_name = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    details_id = db.Column(db.Integer, db.ForeignKey('Node_request.id'))
    created_at = db.Column(db.DateTime default=datetime.now)
    state = db.Column(db.String(10))
    def __init__(self, ip_address, vm_name, created_at, state):
        self.ip_address = ip_address
        self.vm_name = vm_name
        self.created_at = datetime.now()
        self.state = state
