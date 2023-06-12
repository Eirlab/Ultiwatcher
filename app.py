from flask import Flask, request, redirect, render_template
from api_call import *

app = Flask(__name__)


@app.route("/call_get_current_time")
def call_get_current_time():
    '''This function will return the current time of the printer in utc'''
    return str(get_current_time())

@app.route("/call_get_printing_time_total")
def call_get_printing_time_total():
    '''This function will return the estimated time to complete the print job'''
    return str(get_printing_time_total())

@app.route("/call_get_printing_time_elapsed")
def call_get_printing_time_elapsed():
    '''This function will return the elapsed time of the print job'''
    return str(get_printing_time_elapsed())

@app.route("/call_get_printing_progress")
def call_get_printing_progress():
    '''This function will return the progress of the print job'''
    return str(get_printing_progress())

@app.route("/")
def home():
    return render_template("index.html")
