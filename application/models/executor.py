from application import db
from application.models.base import Base
from application.models.action import Action

from application.utils.helper_functions import boolean_converter
from sqlalchemy import text
from datetime import datetime

association_table = db.Table('executor_action', Base.metadata,
    db.Column('executor_id', db.Integer, db.ForeignKey('executor.id')),
    db.Column('action_id', db.Integer, db.ForeignKey('action.id'))
)

class Executor(Base):
    name = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean)

    
    actions = db.relationship("Action",
                    secondary=association_table,
                    backref="executors")

    def __init__(self, name, title, pword, admin=False):
        self.name = name
        self.title = title
        self.password = pword
        self.admin = admin

    @staticmethod
    def get_all_executors_tasks(id):
        stmt = text("SELECT action.id, action.name, action.desc, action.due, action.done"
                    " FROM executor_action"
                    " LEFT JOIN Action"
                    " ON Action.id = executor_action.action_id"
                    " WHERE executor_action.executor_id = :id"
                    " ORDER BY action.due").params(id = id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"action_id": row[0],
                            "action_name": row[1],
                            "action_desc": row[2],
                            "action_due": datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f') if isinstance(row[3], str) else row[3],
                            "action_done": row[4]})

        return response

    @staticmethod
    def get_amount_of_executors_undone_tasks(id):
        stmt = text("SELECT COUNT(*)"
                    "FROM executor_action"
                    " LEFT JOIN Action"
                    " ON Action.id = executor_action.action_id"
                    " WHERE Action.done = :boolean"
                    " AND executor_action.executor_id = :id").params(id = id, boolean = boolean_converter(False))

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response
    
    @staticmethod
    def get_amount_of_executors_done_tasks(id):
        stmt = text("SELECT COUNT(*)"
                    "FROM executor_action"
                    " LEFT JOIN Action"
                    " ON Action.id = executor_action.action_id"
                    " WHERE Action.done = :boolean"
                    " AND executor_action.executor_id = :id").params(id = id, boolean = boolean_converter(True))
        
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append(row[0])

        return response

    @staticmethod
    def get_amount_of_executors_all_tasks(id):
        stmt = text("SELECT COUNT(*)"
                    "FROM executor_action"
                    " LEFT JOIN Action"
                    " ON Action.id = executor_action.action_id"
                    " WHERE executor_action.executor_id = :id").params(id = id)
        
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append(row[0])

        return response

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_admin(self):
        return self.admin