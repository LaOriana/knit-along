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
    
    if session['user']:
    # if 'user_id' in session:
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

    if get_user_by_email(email) == email:
        flash('That email is already in use. Please use another email.')
    
    else:
        create_user(username, email, password, #image)
        flash('Your account has been created. Please log in.')

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

# @app.route('/logout')
# def user_login():
#     """Login user."""

# app routes go here
# Create account
# Login
# Account
# Homepage
# Bookshelf
# Create Event
# Event Info
# Forum


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)