from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    # Is nullable needed for primary key? 
        # No, bc it's already not nullable
    # Should email character limit be 64 or 320?
        # The [user] section can be a maximum of 64 characters, 
        # and the [mysite] section can be a maximum of 255. 
        # The “@” symbol counts as the final character
    # Is the image correct? Would the string be a link?
        # yes
    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True
                        )
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    password = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)

    owned_events = db.relationship('Event', secondary='event_owner')
    attended_events = db.relationship('Event', secondary='event_attended')

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username} email={self.email}>'


class Event(db.Model):
    """An event."""

    __tablename__ = 'events'

    # Is db.Date() correct?
    # Pattern - Is string the correct usage for the API link
    # Yes, can also use rav ID if available?
    event_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True
                        )
    event_name = db.Column(db.String(128), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    pattern = db.Column(db.String, nullable=False)
    # Do I need my chat forum running before I can add this?
    # chat = db.Column(db.String, nullable=False)

    owners = db.relationship('User', secondary='event_owner')
    attendees = db.relationship('User', secondary='event_attended')

    def __repr__(self):
        return f'<Event = event_id{self.event_id} event_name{self.event_name} start_date={self.start_date} end_date={self.end_date} pattern={self.pattern}>'
        # return f'<Event {self.event_name} #{self.event_id}>'


class EventOwner(db.Model):
    """Owner of an event."""

    __tablename__ = 'event_owner'

    owner_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True
                        )
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)

    # Should I be using self.user_id or self.users.user_id (same for event_id)
    # How I have it is fine
    def __repr__(self):
        return f'<EventOwner = user_id{self.user_id} event_id{self.event_id}>'


class EventAttended(db.Model):
    """Event(s) attended by user."""

    __tablename__ = 'event_attended'

    attendee_id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True
                    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)

    # Same question as EventOwner class
    # Move relationship to user and event classes 
    # Many to many demo code
    #secondary ref


    # Same question as EventOwner class
    def __repr__(self):
        return f'<EventOwner = user_id{self.user_id} event_id{self.event_id}>'


class Post(db.Model):
    """A post."""

    __tablename__ = 'posts'

    post_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,
                        nullable=False
                        )
    post_date = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)

    # Same question as EventOwner class
    #backref can be named anything it's not the name of the table
    user = db.relationship('User', backref='posts')
    event = db.relationship('Event', backref='posts')

    # change echo to True to see thing in console
def connect_to_db(flask_app, database='knitalong', echo=False):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{database}"
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)