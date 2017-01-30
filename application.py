from collections import Counter

import csv
import sqlite3

from flask import Flask, render_template, request, g
DATABASE = '/var/www/html/flaskapp/AskBronco.db'
app = Flask('application')

app.config.from_object('application')

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
	 db.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

@app.route('/viewdb')
def viewdb():
    rows = execute_query("""SELECT * FROM User""")
    return '<br>'.join(str(row) for row in rows)



@app.route('/')
def webprint():
    return render_template('login.html')


@app.route('/login.html')
def login():
        return render_template('login.html')
@app.route('/blank.html')
def blank():
        return render_template('blank.html')

@app.route('/student_reports.html')
def dash():
	return render_template('student_reports.html')



@app.route('/ticketsummary.html')
def loadtickets():
        return render_template('ticketsummary.html')


@app.route('/createTicket.html')
def createTicket():
	return render_template('createTicket.html')


@app.route('/MyISS.html')
def MYISS():
	return render_template('MyISS.html')


#@app.route('/login.html')
#def login():
#	return render_template('login.html')


if __name__ == '__main__':
  app.run() 
