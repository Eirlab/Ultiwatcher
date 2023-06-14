from flask import Flask, request, redirect, render_template
from api_call import *

app = Flask(__name__)


@app.route("/call_get_current_time")
def call_get_current_time():
    """This function will return the current time of the printer in utc"""
    current_time_utc = get_current_time()["utc"]
    return str(current_time_utc)


@app.route("/call_get_printing_time_total")
def call_get_printing_time_total():
    """This function will return the estimated time to complete the print job"""
    return str(get_printing_time_total())


@app.route("/call_get_printing_time_elapsed")
def call_get_printing_time_elapsed():
    """This function will return the elapsed time of the print job"""
    return str(get_printing_time_elapsed())


@app.route("/call_get_printing_progress")
def call_get_printing_progress():
    """This function will return the progress of the print job"""
    return str(get_printing_progress())


@app.route("/call_get_printer_name")
def call_get_printer_name():
    """This function will return the name of the printer"""
    return str(get_printer_name())


@app.route("/call_get_printer_status")
def call_get_printer_status():
    """This function will return the status of the printer"""
    printer_status_json = get_printer_status()
    printer_status = printer_status_json["status"]
    printer_bed_temperature = printer_status_json["bed"]["temperature"]["current"]
    printer_head = printer_status_json["heads"][0]
    
    printer_extruder_0_id = printer_head["extruders"][0]["hotend"]["id"]
    printer_extruder_0_temperature = printer_head["extruders"][0]["hotend"]["temperature"]["current"]
    
    printer_extruder_1_id = printer_head["extruders"][1]["hotend"]["id"]
    printer_extruder_1_temperature = printer_head["extruders"][1]["hotend"]["temperature"]["current"]
    
    #print_since_cleaned

    return str([ printer_status, printer_bed_temperature, printer_extruder_0_id, printer_extruder_0_temperature , printer_extruder_1_id, printer_extruder_1_temperature])


@app.route("/")
def home():
    return render_template("index.html")
