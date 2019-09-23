from application import db
from application.models.base import Base

class Action(Base):
    due = db.Column(db.DateTime, default=db.func.current_timestamp())
    desc = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, nullable=False)


    def __init__(self, desc, due, done):
        self.desc = desc
        self.done = done
        if due:
            self.due = due
