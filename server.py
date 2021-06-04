"""Server for knit-along app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import model

app = Flask(__name__)

@app.route('/')
def hompage():
    """View homepage."""

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