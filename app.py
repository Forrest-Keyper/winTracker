'''

'''

from flask import Flask, render_template, request
from bson.objectid import ObjectId
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
# home page, will expand in following commits
def index():
    return render_template('index.html')




@app.route('/register')
# registration page, sign up link should redirect here
def register():
    user = {
        'name': request.form.get('username'),
        'password': request.form.get('password')
    }
    # will eventually need to check for user unique identity
    # accept user form input for username and email (password later)

    # what does this return statement need to be for the confirmation function?
    return render_template('register.html')


'''
@app.route('/user')
@app.route('/register/confirm')
def confirmRegistration():

    # confirm user creation, move to dashboard
    return('templates/dashboard.html')

@app.route('/dashboard')
def dashboard('/dashboard')

    # checks for user log in, takes user id and displays associated trackers
    #
    return('/templates/dashboard.html')


'''

if __name__ == "__main__":
    app.run(debug=True)
