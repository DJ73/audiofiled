from re import T
from app import db
from datetime import datetime

class Audio(db.Model):
    """
    A table to ensure each record is unique
    """
    __tablename__ = "audio"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), index=True)

    def __init__(self, type) -> None:
        super().__init__()
        self.type = type


class Song(db.Model):
    """
    A table containing Song metadata
    """
    id = db.Column(db.Integer, db.ForeignKey('audio.id'), primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, name, duration) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.duration = duration
        self.upload_time = datetime.utcnow()

    def __repr__(self) -> str:
        return f"[SONG] ({self.id}) {self.name}"


class Podcast(db.Model):
    """
    A table containing Podcast metadata
    """
    id = db.Column(db.Integer, db.ForeignKey('audio.id'), primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False)
    host = db.Column(db.String(100), index=True, nullable=False)
    participants = db.Column(db.ARRAY(db.String(100)), index=True, nullable=False)

    def __init__(self, id, name, duration, host, participants) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.duration = duration
        self.upload_time = datetime.utcnow()
        self.host = host
        self.participants = participants

    def __repr__(self) -> str:
        return f"[PODCAST] ({self.id}) {self.name} by {self.host}"


class Audiobook(db.Model):
    """
    A table containing Audiobook metadata
    """
    id = db.Column(db.Integer, db.ForeignKey('audio.id'), primary_key=True)
    title = db.Column(db.String(100), index=True, nullable=False)
    author = db.Column(db.String(100), index=True, nullable=False)
    narrator = db.Column(db.String(100), index=True, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, title, author, narrator, duration) -> None:
        super().__init__()
        self.id = id
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.upload_time = datetime.utcnow()

    def __repr__(self) -> str:
        return f"[AUDIOBOOK] ({self.id}) {self.title} written by {self.author} narrated by {self.narrator}"


MODELS = {"song": Song, "podcast": Podcast, "audiobook": Audiobook}