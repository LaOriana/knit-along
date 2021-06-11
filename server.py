"""Server for knit-along app."""

from crud import get_user_by_email
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import model

app = Flask(__name__)

@app.route('/')
def homepage():
    """View homepage."""
    
    # check to see if user is logged in
    # if the user is logged in
        #redirect to bookshelf 
    # else redirect to login/sign up
        #need to decide if this redirect is actually the homepage
    
    input_email = request.form.get('email')
    input_password = request.form.get('password')
    user = get_user_by_email(input_email)

    if user and user.password == input_password:
        session['user'] = user.user_id
        flash('Logged in.')
        return redirect('/bookshelf')
    else:
        flash('Incorrect login')
        return redirect('/')

    # this will most likely not be needed once I complete the above items
    return render_template('homepage.html')

# Might delete /signup and /login
# @app.route('/signup')
# def signup():
#     """Signup user."""

#     return render_template('signup.html')

# @app.route('/login')
# def user_login():
#     """Login user."""

#     return render_template('login.html')

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
    app.run(host='0.0.0.0', debug=True)