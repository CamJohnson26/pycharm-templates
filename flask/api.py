from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app = Flask(__name__)
allowed_origins = getenv('ALLOWED_ORIGINS')
CORS(app, origins=allowed_origins)


@app.route('/')
def hello_world():
    return 'Hello World!'
