from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Job %r>' % self.id