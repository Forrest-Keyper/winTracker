from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient()
db = client.Tracker
users = db.users

app = Flask(__name__)


@app.route('/')
def tracker_index():
    return render_template('index.html')


@app.route('/register')
def user_register():

    return render_template('register.html', user={}, title='New User')


@app.route('/user/register', methods=['POST'])
def register():
    user = {
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'public': request.form.get('public')
    }
    user_id = users.insert_one(user).inserted_id
    return redirect(url_for('dashboard', user_id=user_id))


@app.route('/user/register/<user_id>')
def dashboard(user_id):
    user = users.find_one({'_id': ObjectId(user_id)})
    return render_template('dashboard.html', user=user)


@app.route('/register/confirm')
def confirmRegistration():
    return('templates/dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)
