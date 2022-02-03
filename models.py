"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import backref
import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """cupcakes model"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    flavor = db.Column(db.String, nullable=False)

    size = db.Column(db.String, nullable=False)

    rating = db.Column(db.String, nullable=False)

    image = db.Column(db.String, nullable=False, default='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        """Serialize a cupcake SQLAlchemy obj to dictionary"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image = {self.image}"

