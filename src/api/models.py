from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    user_favourites = db.relationship("UserFavourite", backref="user")

    def __repr__(self):
        return f"{self.username}"

    def serialize(self):
        return {
            "user id": self.id,
            "email": self.email,
            "username": self.username
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    species = db.Column(db.String(80), nullable=False)
    favourites = db.relationship("UserFavourite", backref="character")

    def __repr__(self):
        return f"{self.name}"
    
    def serialize(self):
        return {
            "character id": self.id,
            "name": self.name,
            "species": self.species
        }


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80))
    favourites = db.relationship("UserFavourite", backref="location")

    def __repr__(self):
        return f"{self.name}"
    
    def serialize(self):
        return {
            "lcoation id": self.id,
            "name": self.name,
            "type": self.type
        }


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    air_date = db.Column(db.String(50))
    favourites = db.relationship("UserFavourite", backref="episode")

    def __repr__(self):
       return f"{self.name}"
    
    def serialize(self):
        return {
            "episode id": self.id,
            "name": self.name,
            "air_date": self.air_date
        }


class UserFavourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=True)
    episode_id = db.Column(db.Integer, db.ForeignKey("episode.id"), nullable=True)

    def __repr__(self):
        return f"UserFavourite(user_id={self.user_id}, character_id={self.character_id}, location_id={self.location_id}, episode_id={self.episode_id})"

    def serialize(self):
        serialized = {
            "favourite id": self.id,
            "user_id": self.user_id,
        }
        
        if self.character:
            serialized["character"] = {
                "character id": self.character.id,
                "name": self.character.name,
                "species": self.character.species
            }
            
        if self.location:
            serialized["location"] = {
                "location id": self.location.id,
                "name": self.location.name,
                "type": self.location.type
            }
            
        if self.episode:
            serialized["episode"] = {
                "episode id": self.episode.id,
                "name": self.episode.name,
                "air_date": self.episode.air_date
            }
        
        return serialized

