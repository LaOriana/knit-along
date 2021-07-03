"""CRUD operations."""

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


def create_post(post_date, content):
    """Create and return a new post."""

    post = Post(post_date=post_date, content=content)

    db.session.add(post)
    db.session.commit()

    return post


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return user with ID."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user with email."""

    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)