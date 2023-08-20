# from flask import Flask, redirect, render_template, request, url_for, session

# # app configuration
# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, session
from pymongo import MongoClient
from flask import render_template, redirect, url_for
from helper import login_required


app = Flask(__name__)

secret_key = "vinay"

# Set the secret key for the Flask app
app.secret_key = secret_key

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users = db["users"]


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # You should hash the password before storing it.
        users.insert_one({'username': username, 'password': password})
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username, 'password': password})
        
        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome to your dashboard, {session["username"]}!'

