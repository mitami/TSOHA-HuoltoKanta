from application import db

class Executor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    title = db.Column(db.String(30))

    def __init__(self, name, title):
        self.name = name
        self.title = title