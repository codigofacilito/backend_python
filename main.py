from flask import Flask

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

if __name__ == "__main__":
	print("Hola")
	app.run()