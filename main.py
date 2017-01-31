from flask import Flask
from flask import render_template


import datetime

app = Flask(__name__)

@app.route('/login')
def login():
	autor = 'Eduardo'
	tags = ['Python', 'web']
	ahora = datetime.datetime.now()
	activo = False

	return render_template('login.html', autor=autor, tags=tags, ahora=ahora, activo=activo)

if __name__ == "__main__":
	app.run()