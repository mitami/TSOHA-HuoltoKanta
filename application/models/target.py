from application import db
from application.models.base import Base

from sqlalchemy.sql import text

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