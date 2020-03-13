from app import db

class Certification(db.Model):
    __tablename__ = "certification"
    id = db.Column(db.String(40), primary_key=True)

    def __init__(self, get_id):
        self.id = get_id

    def __repr__(self):
        return '<Certification %s>' % (self.id)