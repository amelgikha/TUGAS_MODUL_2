from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import MySQLdb.cursors
import re

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'taikucing'
app.config['MYSQL_DB'] = 'pythonlogin'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    msg = "You Have Not Been Signed Up!"
    if request.method == 'POST': 
    # and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password))
        body = cursor.fetchall()
        print(body)
        if body:
            session['loggedin'] = True
            session['id'] = body['id']
            session['email'] = body['email']
            return 'ok'
        else:
            return render_template('signin.html')
    return render_template('index.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    msg = "If you don't have any account, please register before"
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'email' in request.form:
        email = request.form['email']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', email):
            msg = 'email must contain only characters and numbers!'
        elif not email or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (email, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = %s', [session['id']])
        account = cursor.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='3100')