import json

from app.extensions import db

Column = db.Column
Integer = db.Integer
Float = db.Float
String = db.String
ForeignKey = db.ForeignKey
relationship = db.relationship
Boolean = db.Boolean
Date = db.Date
DateTime = db.DateTime
Text = db.Text
PickleData = db.PickleType

class Model(db.Model):

    _id = Column(Integer, primary_key=True)

    __tablename__ = "options"

    def __init__(self, **kwargs):
        print(f"{kwargs}")

        for k, v in kwargs.items():
            setattr(self, k, v)

        if not self.id_exists(self.id):
            # Saves the object anyway
            self.save()


    def id_exists(self, id):
        exists = self.query.filter_by(id=id).first()
        if exists:
            return exists
        return False


    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

    def all(self):
        return self.query.all()
