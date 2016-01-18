# blog.py - controller

# imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
import os

# Configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xad\xd7\x8b\xabez\x8a\x909\x12)\x07\xd3\x12nh\x02K\xab{\x9c\x19\x0b\n'

app = Flask(__name__)

# pulls in app configs by looks for UPPERCASE variables
app.config.from_object(__name__)


# function used for connection the the DB
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = "Invalid Credentials. Please Try Again."
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html',error=error)


@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash("You were logged out")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
