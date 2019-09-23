from application import db
from application.models.base import Base

from sqlalchemy import text

class Action(Base):
    name = db.Column(db.String(255))
    due = db.Column(db.DateTime, default=db.func.current_timestamp())
    desc = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('target.id'))


    def __init__(self, name, desc, due, done, target):
        self.desc = desc
        self.done = done
        if due:
            self.due = due
        if name:
            self.name = name
        if target:
            self.target_id = target

    @staticmethod
    def find_one_with_target_and_user(id):
        #Voiko SQL -kyselyä optimoida?
        stmt = text("SELECT action.id, action.name, action.desc, action.done, action.due, target.name, location.name, executor.name"
                    " FROM Action JOIN executor_action ON executor_action.action_id = action.id"
                    " JOIN Executor ON Executor.id = executor_action.executor_id"
                    " JOIN Target ON Target.id = action.target_id"
                    " JOIN Location ON Location.id = target.location_id"
                    " WHERE action.id = :id").params(id = id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"action_id": row[0],
                            "action_name": row[1],
                            "action_desc": row[2],
                            "action_done": row[3],
                            "action_due": row[4],
                            "target_name": row[5],
                            "location_name": row[6],
                            "executor_name": row[7]})

        return response