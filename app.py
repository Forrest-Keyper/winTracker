'''

'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def splash():
    return 'Hello World!'


'''

@app.route('/register')
def register():

    # will eventually need to check for user unique identity
    # accept user form input for username and email (password later)
    
    # what does this return statement need to be for the confirmation function?
    return('/templates/dashboard.html')

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
