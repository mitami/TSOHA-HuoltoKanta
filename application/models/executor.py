from application import db

class Executor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    def __init__(self, name, title, pword):
        self.name = name
        self.title = title
        self.password = pword