from flask import Flask
from flask import render_template
from flask import request
from flask import flash

from flask import session
from flask import redirect
from flask import url_for

import os
import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('flask_key')

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def valid_password(self, password):
		return self.password == password

first_user = User('eduardo', '123')
second_user = User('cf', '123')
users = { first_user.username : first_user, second_user.username : second_user}

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		
		user = users.get(username, None)
		if user and user.valid_password(password):
			message = 'Bienvenido usuario {}'.format(username)
			flash(message, 'success')

			session['user'] = username
			return redirect(url_for('dashboard'))

		else:
			flash('Usuario o password invalidos.', 'danger')

	return render_template('login.html')


@app.route('/dashboard')
def dashboard():
	username = session['user']
	return render_template('dashboard.html', username=username)


@app.route('/logout')
def logout():
	session.pop('user')
	return redirect( url_for('login'))



if __name__ == "__main__":
	app.run(debug=True)
