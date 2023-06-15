from flask import Flask, request, redirect, render_template
from api_call import *

import datetime

app = Flask(__name__)

PRINTER_IP = "192.168.0.120"
#PRINTER_IP = "192.168.0.114"


@app.route("/call_get_current_time")
def call_get_current_time():
    """This function will return the current time of the printer in utc"""
    current_time_utc = get_current_time(PRINTER_IP)["utc"]
    return str(current_time_utc)


@app.route("/call_get_printing_time_total")
def call_get_printing_time_total():
    """This function will return the estimated time to complete the print job"""
    printing_time_total_utc = get_printing_time_total(PRINTER_IP)
    #convert utc to HH:MM:SS
    printing_time_total = datetime.datetime.utcfromtimestamp(printing_time_total_utc).strftime('%H:%M:%S')
    return "Estimated print time: "+str(printing_time_total)


@app.route("/call_get_printing_time_elapsed")
def call_get_printing_time_elapsed():
    """This function will return the elapsed time of the print job"""
    printing_time_elapsed_utc = get_printing_time_elapsed(PRINTER_IP)
    #convert utc to HH:MM:SS
    printing_time_elapsed = datetime.datetime.utcfromtimestamp(printing_time_elapsed_utc).strftime('%H:%M:%S')
    return "Time elapsed: " +str(printing_time_elapsed)


@app.route("/call_get_printing_progress")
def call_get_printing_progress():
    """This function will return the progress of the print job"""
    return str(get_printing_progress(PRINTER_IP))


@app.route("/call_get_printer_name")
def call_get_printer_name():
    """This function will return the name of the printer"""
    return str(get_printer_name(PRINTER_IP))

@app.route("/call_get_printing_job")
def call_get_printing_job():
    """This function will return the current job of the printer"""
    printing_job_json = get_printing_job(PRINTER_IP)

    #printing_job_name = printing_job_json["name"]
    
    return str(printing_job_json)


@app.route("/call_get_printer_status")
def call_get_printer_status():
    """This function will return the status of the printer"""
    printer_status_json = get_printer_status(PRINTER_IP)
    printer_status = printer_status_json["status"] 
    if printer_status == "idle":
        printer_status = "<span style='font-weight:bold;color:#575757;'>Ready for print</span>"
    printer_bed_temperature = printer_status_json["bed"]["temperature"]["current"]
    printer_head = printer_status_json["heads"][0]
    
    printer_extruder_0_id = printer_head["extruders"][0]["hotend"]["id"]
    printer_extruder_0_temperature = printer_head["extruders"][0]["hotend"]["temperature"]["current"]
    
    printer_extruder_1_id = printer_head["extruders"][1]["hotend"]["id"]
    printer_extruder_1_temperature = printer_head["extruders"][1]["hotend"]["temperature"]["current"]
    
    #print_since_cleaned
    
    return {"status": "Status: "+printer_status, "bed_temperature": printer_bed_temperature, "extruder_0_id": printer_extruder_0_id, "extruder_0_temperature": printer_extruder_0_temperature, "extruder_1_id": printer_extruder_1_id, "extruder_1_temperature": printer_extruder_1_temperature}

@app.route("/")
def home():
    return render_template("index.html")
