from flask import Flask
import re

app = Flask(__name__)
app.secret_key = "this_is_secret"

DATABASE = "login_reg_db"
app.secret_key = "ohboyherewego"


