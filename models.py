from app import db

vid_list = []


def get_last_id():
    if vid_list:
        last_vid = vid_list[-1]
    else:
        return 1
    return last_vid.id + 1


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))
    description = db.Column(db.String(150))
    released_year = db.Column(db.Datetime())
    num_of_amounts = db.Column(db.Integer())
    is_available = db.Column(db.Boolean())

    def __repr__(self):
        return {
            "id": get_last_id(),
            "title": self.title,
            "genre": self.genre,
            "description": self.description,
            "released_year": self.released_year,
        }
