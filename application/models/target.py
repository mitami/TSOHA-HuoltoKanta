from application import db
from application.models.base import Base

class Target(Base):
    name = db.Column(db.String(50))

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    
    def __init__(self, name):
        self.name = name