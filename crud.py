"""CRUD operations"""

from model import db, User, Event, EventOwner, EventAttended, Post, connect_to_db

# add images to static file
def create_user(username, email, password, image)
    """Create and return a new user."""

    user = User(username=username, email=email, password=password, image=image)

    db.session.add(user)
    db.session.commit()

    return user