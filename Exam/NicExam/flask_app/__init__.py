from flask import Flask
import re

app = Flask(__name__)
app.secret_key = "this_is_secret"

DATABASE = "car_dealz"
app.secret_key = "gettingtired"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9,+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')