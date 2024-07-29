from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def sign():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        if name.strip() and username.strip() and password.strip():
            with open('db.json') as infile:
                db = json.load(infile)
                for i in db:
                    if username in i['username']:
                        message = 'Username Already Exists Please Enter Another Username :)'
                        return render_template('signup.html', message=message)
            data = {'name': name, 'username': username, 'password': password}
            db.append(data)
            with open('db.json', 'w') as outfile:
                json.dump(db, outfile, indent=4)
            return render_template('signup.html', username=username)
        else:
            return render_template('signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username.strip() and password.strip():
            with open('db.json') as infile:
                db = json.load(infile)
                for i in db:
                    if username in i['username']:
                        return render_template('login.html', username=username)
                message = "You don't have an account, Please open account"
                return render_template('login.html', message=message)
        return render_template('login.html')
