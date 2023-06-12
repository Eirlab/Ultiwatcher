from flask import Flask, request, redirect, render_template
from api_call import *

app = Flask(__name__)


@app.route("/call_get_current_job")
def call_get_current_job():
    '''This function will return the current job of the printer'''
    return str(get_current_job())

@app.route("/")
def home():
    return render_template("index.html")
