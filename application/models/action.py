from application import db

class Action(db.model):
  id = db.Column(db.Integer, primary_key=True)
  created = db.Column(db.DateTime, default=db.func.current_timestamp())
  due = db.Column(db.DateTime, default=db.func.current_timestamp())
  desc = db.Column(db.String(), nullable=False)
