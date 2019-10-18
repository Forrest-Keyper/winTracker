from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient()
db = client.Tracker
users = db.users

app = Flask(__name__)


@app.route('/')
def tracker_index():
    # will eventually contain a popular trackers box and search option
    return render_template('index.html')


@app.route('/register')
def user_register():
    return render_template('register.html', user={}, title='New User')


@app.route('/user/register', methods=['POST'])
def register():
    # register a new user. will likely contain further options in the future
    user = {
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'public': request.form.get('public')
    }
    user_id = users.insert_one(user).inserted_id
    return redirect(url_for('dashboard', user_id=user_id))


@app.route('/user/login')
def loginForm():
    username = request.form.get('username')
    user = users.find_one({'username': username})
    user_id = user.inserted_id
    return render_template('login.html', user_id=user_id)

@app.route('/user/login/<user_id>')
def loginAct(user_id):

    return redirect(url_for('dashboard', user_id=user_id))


@app.route('/user/<user_id>/dashboard')
def dashboard(user_id):
    # eventually will display user's trackers which will link to individual tracker management page
    userObj = users.find_one({'_id': ObjectId(user_id)})
    user = userObj
    print(userObj)
    return render_template('dashboard.html', user=user)


@app.route('/user/<user_id>/update', methods=['POST'])
def update(user_id):
    # will eventually become a full user settings page including settings for sharing trackers the user has made
    user = {
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'public': request.form.get('public')
    }
    user_id = users.insert_one(user).inserted_id
    return redirect(url_for('dashboard', user_id=user_id))


@app.route('/user/<user_id>/edit')
def user_edit(user_id):
    # renders the form for user to update their settings
    print(user_id)
    user = client.db.users.find_one({'_id': ObjectId(user_id)})
    return render_template('updateUser.html', user_id=user_id)


if __name__ == "__main__":
    app.run(debug=True)
