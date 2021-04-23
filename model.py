from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    # Is nullable needed? 
    # Should email character limit be 64 or 320?
        # The [user] section can be a maximum of 64 characters, 
        # and the [mysite] section can be a maximum of 255. 
        # The “@” symbol counts as the final character
    # Is the image correct? Would the string be a link?
    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrment=True, 
                        nullable=False)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)


class Event(db.Model):
    """An event."""


class EventOwner(db.Model):
    """Owner of an event."""


class EventAttended(db.Model):
    """Event(s) attended by user."""


class Post(db.Model):
    """A post."""