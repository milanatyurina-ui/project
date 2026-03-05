from extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=True)
    priority = db.Column(db.Integer, nullable=False)
    term = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
