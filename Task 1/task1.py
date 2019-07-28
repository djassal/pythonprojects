from flask import Flask, session, redirect, url_for, escape, request, render_template
from hashlib import md5
import pymysql

app = Flask(__name__)

if __name__ == '__main__':
    db = pymysql.connect(host="localhost", user="root", password="sudo", database="credentials")
    cur = db.cursor()
    app.secret_key = 'A0Zr98j/3yXR~XHH!jmdcdsvcdsvdsvdsT'

class ServerError(Exception):
    pass
    
@app.route('/')
def index():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        try:
            if not username_session == 'Test':
                db = pymysql.connect(host = 'localhost', user = 'root', password = 'sudo',database = "real_estate")
                cursor = db.cursor()
                query = "select * from cust_info where city = 'SACRAMENTO' and price > 100000 order by price"
                data = cursor.execute(query)
                list_data = []
                for data in cursor.fetchall():
                    list_data.append(data)
                return render_template('index.html', session_user_name=username_session, info=list_data, count=len(list_data))
            else:
                return render_template('index.html', session_user_name=username_session)
        except pymysql.err.OperationalError:
            print("Unable to connect to database due to incorrect credentials.")
        except pymysql.err.InternalError:
            print("Database not found.")
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    error = None
    try:
        if request.method == 'POST':
            username_form  = request.form['username']
            cur.execute("SELECT COUNT(1) FROM user_credentials WHERE username = '{}'".format(username_form))
            if not username_form == 'test':
                if not cur.fetchone()[0]:
                    raise ServerError('Username does not exist.')

            password_form  = request.form['password']
            cur.execute("SELECT password FROM user_credentials WHERE username = '{}'".format(username_form))

            for row in cur.fetchall():
                if md5(password_form.encode('utf-8')).hexdigest() == md5(row[0].encode('utf-8')).hexdigest():
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))
            if md5(password_form.encode('utf-8')).hexdigest() == md5('test'.encode('utf-8')).hexdigest():
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))
            raise ServerError('Incorrect password.')
    except ServerError as e:
        error = str(e)
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)