"""Server for knit-along app."""

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

    # this will most likely not be needed once I complete the above items
    return render_template('homepage.html')

@app.route('/signup')
def signup():
    """Signup user."""

    return render_template('signup.html')

@app.route('/login')
def user_login():
    """Login user."""

    return render_template('login.html')

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