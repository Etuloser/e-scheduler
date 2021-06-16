from config import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    createDate = db.Column(db.DateTime)
    editDate = db.Column(db.DateTime, server_default=db.FetchedValue())

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'createDate': self.createDate,
            'editDate': self.editDate,
        }
