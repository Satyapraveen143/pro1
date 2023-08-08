from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager(app)

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key

# Simulated user data (replace with your database logic)
USERS = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def home():
    return 'Welcome to the social media framework!'

@app.route('/profile')
def profile():
    return 'This is the user profile page.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
