"""CRUD operations"""

from model import db, User, Event, EventOwner, EventAttended, Post, connect_to_db

# add images to static file
def create_user(username, email, password, image):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password, image=image)

    db.session.add(user)
    db.session.commit()

    return user

def create_event(event_name, start_date, end_date, pattern):
    """Create and return a new event."""

    event = Event(event_name=event_name, start_date=start_date, end_date=end_date, pattern=pattern)

    db.session.add(event)
    db.session.commit()

    return event