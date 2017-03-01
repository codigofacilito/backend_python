from flask import Flask
from flask import render_template
from flask import request
from flask import flash

import datetime

app = Flask(__name__)

usuarios = {'eduardo': 'password'}

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		
		usuario = usuarios.get(username, None)
		if usuario and usuario == password:
			flash('Autenticacion valida!', 'error')
		else:
			flash('Usuario o password no validos', 'error')


	return render_template('login.html')

if __name__ == "__main__":
	app.run()