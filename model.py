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
                        nullable=False
                        )
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<User user_id={self.user_id} username={username} email={email}>'


class Event(db.Model):
    """An event."""

    __tablename__ = 'events'

    # Is db.Date() correct?
    # Pattern - Is string the correct usage for the API link
    event_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrment=True,
                        nullable=False
                        )
    event_name = db.Column(db.String(128), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    pattern = db.Column(db.String, nullable=False)
    # Do I need my chat forum running before I can add this?
    # chat = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Event = event_id{event_id} event_name{event_name} start_date={start_date} end_date={end_date} pattern={pattern} >'


class EventOwner(db.Model):
    """Owner of an event."""


class EventAttended(db.Model):
    """Event(s) attended by user."""


class Post(db.Model):
    """A post."""