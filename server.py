"""Server for knit-along app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from crud import (get_user_by_email, create_user)
import model
import os
import crud

app = Flask(__name__)
# need to run source secrets.sh for this to work
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def homepage():
    """View homepage."""
    
    # if session['user']:
    if 'user' in session:
        # wasn't redirecting with code above. When switched to if session['user']: it worked
        flash('Logged in.')
        return redirect('/bookshelf')

    # this will most likely not be needed once I complete the above items
    return render_template('homepage.html')


@app.route('/signup', methods=['POST'])
def signup():
    """Signup user."""

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    image = 'https://tinyurl.com/2ujz8nxb'

    if get_user_by_email(email):
        flash('That email is already in use. Please login or use another email.')
    
    else:
        user = create_user(username, email, password, image)
        session['user'] = user.user_id
        flash('Your account has been created and you\'re logged in.')
        return redirect('/bookshelf')
        
    return redirect('/')


@app.route('/login', methods=["POST"])
def user_login():
    """Login user."""

    input_email = request.form.get('email')
    print(f'input_email {input_email}')
    input_password = request.form.get('password')
    user = get_user_by_email(input_email)

    if user and user.password == input_password:
        session['user'] = user.user_id
        flash('Logged in.')
        return redirect('/bookshelf')
    else:
        flash('Incorrect login')
        return redirect('/')


@app.route('/bookshelf')
def bookshelf():
    """View bookshelf."""
    
    return render_template('bookshelf.html')

@app.route('/logout')
def logout():
    """Logout user."""
    
    session.pop('user')
    return redirect('/')

@app.route('/createeventpage')
def create_event_page():
    """Create event page."""

    return render_template('createeventpage.html')

@app.route('/createeventaction', methods=['POST'])
def create_event_action():
    """Creating event and adding it to the database."""

    '''use crud function (create_event) to create event. 
    This will return an event object. 
    From this object can get eventid.
    Pass eventID to event.html'''

    input_title = request.form.get('title')
    print(input_title)

    return redirect('/event')

# Is this a get or post?
@app.route('/event', methods=['POST'])
def event():
    """Event information."""

    # return will use event ID to get event information 
    # and then pass this using jinja


# app routes go here
# Create account - complete
# Login - complete
# Logout - complete
# Homepage - complete
# Account
# Bookshelf
# Create Event
    # similar to login
    # create fields for API/user - use database fields
    # timeframe - look up on google if there is a type='date'?
    # use crud function create_event
    # redirect to event page and give eventID to event info
# Event Info
# Forum
# Option to edit event


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)