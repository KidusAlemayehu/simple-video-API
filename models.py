from app import db

class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))
    description = db.Column(db.String(150))
    released_year = db.Column(db.Datetime())
