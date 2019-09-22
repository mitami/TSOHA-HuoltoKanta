from application import db
from application.models.base import Base

class Location(Base):
    name = db.Column(db.String(30))

    targets = db.relationship("Target", backref='target', lazy=True)

    def __init__(self, name):
        self.name = name