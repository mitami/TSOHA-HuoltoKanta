from application import db
from application.models.base import Base

class Action(Base):
    name = db.Column(db.String(255))
    due = db.Column(db.DateTime, default=db.func.current_timestamp())
    desc = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, nullable=False)


    def __init__(self, name, desc, due, done):
        self.desc = desc
        self.done = done
        if due:
            self.due = due
        if name:
            self.name = name
