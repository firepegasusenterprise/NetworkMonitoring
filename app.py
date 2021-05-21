# Importing requirements

from flask import Flask, render_template, request, redirect, url_for, flash
from flask.wrappers import Request
from flask_mysqldb import MySQL

# Executing requirements

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin1234'
app.config['MYSQL_DB'] = 'advancedfirehearthcompany'
mysql = MySQL(app)

# Initializing Settings

app.secret_key = "mysecret.key"

# Creating The Main Page

@app.route('/')
def Index():
    return render_template('form.html')

# Creating The Devices Page

@app.route('/devices')
def devices():
    return 'Devices Page For The Application'

@app.route('/new_devices', methods=['POST'])
def new_devices():
    if request.method == 'POST':
        fullname = request.form['fullname']
        hostname = request.form['hostname']
        company = request.form['company']
        type = request.form['type']
        cores = request.form['cores']
        ram = request.form['ram']
        storage = request.form['storage']
        server = request.form['server']
        os = request.form['os']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO devices (fullname, hostname, company, type, cores, ram, storage, server, os) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (fullname, hostname, company, type, cores, ram, storage, server, os))
        mysql.connection.commit()
        flash('Succesfull Added')
        return redirect(url_for('Index'))


@app.route('/edit_devices')
def edit_devices():
    return 'Devices Creator For The Application'

@app.route('/remove_devices')
def remove_devices():
    return 'Devices Remover For The Application'

# Starting The Applications

if __name__ == '__main__':
    app.run(port=5190, debug=True)