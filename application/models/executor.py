from application import db
from application.models.base import Base
from application.models.action import Action

from sqlalchemy import text

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
                    " WHERE executor_action.executor_id = :id").params(id = id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"action_id": row[0],
                            "action_name": row[1],
                            "action_desc": row[2],
                            "action_due": row[3],
                            "action_done": row[4]})

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