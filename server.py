"""Server for knit-along app."""

from flask import (Flask, render_template, request, flash, session, redirect)

app = Flask(__name__)


# app routes go here



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')