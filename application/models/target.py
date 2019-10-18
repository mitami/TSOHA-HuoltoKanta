from application import db
from application.models.base import Base

from sqlalchemy.sql import text
from datetime import datetime

class Target(Base):
    name = db.Column(db.String(50))

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    
    def __init__(self, name, location):
        self.name = name
        self.location_id = location

    @staticmethod
    def find_target_and_its_location(id):
        stmt = text("SELECT target.id, target.name, location.id, location.name FROM Target"
                    " LEFT JOIN Location ON Location.id = target.location_id"
                    " WHERE target.id = :id").params(id = id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"target_id": row[0],
                            "target_name": row[1],
                            "location_id": row[2],
                            "location_name": row[3]})

        return response

    @staticmethod
    def find_target_and_location_and_tasks(id):
        stmt = text("SELECT target.id, target.name, location.id, location.name, action.name, action.due, action.done"
                    " FROM Target"
                    " JOIN Location ON Location.id = target.location_id"
                    " JOIN Action ON Action.target_id = :id").params(id = id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"target_id": row[0],
                            "target_name": row[1],
                            "location_id": row[2],
                            "location_name": row[3],
                            "action_name": row[4],
                            "action_due": datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f') if isinstance(row[5], str) else row[5],
                            "action_done": row[6]})

        return response

    @staticmethod
    def find_related_actions(id):
        stmt = text("SELECT action.id, action.name, action.desc, action.due, action.done"
                    " FROM Action"
                    " WHERE Action.target_id = :id"
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