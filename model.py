from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy

class User(db.Model):
    """A user."""


class Event(db.Model):
    """An event."""


class EventOwner(db.Model):
    """Owner of an event."""


class EventAttended(db.Model):
    """Event(s) attended by user."""


class Post(db.Model):
    """A post."""