from flask import Flask, request, redirect, render_template
from api_call import *

import datetime
import time

app = Flask(__name__)

PRINTER_IP_IDX = 0
IP_LIST= ["192.168.0.119","192.168.0.120","192.168.0.114"]
PRINTER_IP = IP_LIST[PRINTER_IP_IDX]



@app.route("/call_get_current_time/<printer_idx>")
def call_get_current_time(printer_idx):
    """This function will return the current time of the printer in utc"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    current_time_utc = get_current_time(PRINTER_IP)["utc"]
    current_time = datetime.datetime.utcfromtimestamp(current_time_utc).strftime('%Y-%m-%d %H:%M:%S')
    #add 2 hours to utc time
    current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
    current_time = current_time + datetime.timedelta(hours=2)
    #only return the time
    current_time = current_time.strftime('%H:%M')
    return str(current_time)


@app.route("/call_get_printing_time_total/<printer_idx>")
def call_get_printing_time_total(printer_idx):
    """This function will return the estimated time to complete the print job"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    printing_time_total_utc = get_printing_time_total(PRINTER_IP)
    try:
        printing_time_total = datetime.datetime.utcfromtimestamp(printing_time_total_utc).strftime('%H:%M:%S')
    except:
        printing_time_total = "00:00:00"
    return "Estimated print time: "+str(printing_time_total)

@app.route("/call_get_printing_time_left/<printer_idx>")
def call_get_printing_time_left(printer_idx):
    """This function will return the estimated time left to complete the print job"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    printing_time_total_utc = get_printing_time_total(PRINTER_IP)
    printing_time_elapsed_utc = get_printing_time_elapsed(PRINTER_IP)
    try:
        printing_time_left = datetime.datetime.utcfromtimestamp(printing_time_total_utc-printing_time_elapsed_utc).strftime('%H:%M:%S')
    except:
        printing_time_left = "00:00:00"
    return "Time remaining: "+str(printing_time_left)

@app.route("/call_get_printing_time_elapsed/<printer_idx>")
def call_get_printing_time_elapsed(printer_idx):
    """This function will return the elapsed time of the print job"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    printing_time_elapsed_utc = get_printing_time_elapsed(PRINTER_IP)
    try:
        printing_time_elapsed = datetime.datetime.utcfromtimestamp(printing_time_elapsed_utc).strftime('%H:%M:%S')
    except:
        printing_time_elapsed = "00:00:00"
    return "Time elapsed: " +str(printing_time_elapsed)


@app.route("/call_get_printing_progress/<printer_idx>")
def call_get_printing_progress(printer_idx):
    """This function will return the progress of the print job"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    printing_progress = get_printing_progress(PRINTER_IP)
    return str(printing_progress)

@app.route("/call_get_printer_name/<printer_idx>")
def call_get_printer_name(printer_idx):
    """This function will return the name of the printer"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    return str(get_printer_name(PRINTER_IP))

@app.route("/call_get_printing_job/<printer_idx>")
def call_get_printing_job(printer_idx):
    """This function will return the current job of the printer"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    printing_job_body = get_printing_job(PRINTER_IP).content
    #extract "name" from body
    printing_job_body = printing_job_body.decode("utf-8")
    
    try:
        print_name = printing_job_body.split('"name":')[1].split(',')[0].replace('"', '')
        print_uuid = printing_job_body.split('"uuid":')[1].split(',')[0].replace('"', '').replace('}' , '')
    except:
        print_name = "No current print"
        print_uuid = "nouuid"
    #print_preview = get_print_preview(PRINTER_IP, print_uuid)
    
    return {"name": "Print name: "+ print_name, "uuid": print_uuid}


@app.route("/call_get_printer_status/<printer_idx>")
def call_get_printer_status(printer_idx):
    """This function will return the status of the printer"""
    PRINTER_IP = IP_LIST[int(printer_idx)]
    printer_status_json = get_printer_status(PRINTER_IP)
    printer_status = printer_status_json["status"] 
    if printer_status == "idle":
        printer_status = "<span style='font-weight:bold;color:#575757;'>READY</span>"
    elif printer_status == "printing":
        printer_status = "<span style='font-weight:bold;color:#3B7CDC;'>PRINTING</span>"
    printer_bed_temperature = printer_status_json["bed"]["temperature"]["current"]
    printer_head = printer_status_json["heads"][0]
    
    printer_extruder_0_id = printer_head["extruders"][0]["hotend"]["id"]
    printer_extruder_0_temperature = printer_head["extruders"][0]["hotend"]["temperature"]["current"]
    
    printer_extruder_1_id = printer_head["extruders"][1]["hotend"]["id"]
    printer_extruder_1_temperature = printer_head["extruders"][1]["hotend"]["temperature"]["current"]
    
    prints_since_cleaned = printer_head["extruders"][0]["hotend"]["statistics"]["prints_since_cleaned"]
    print(prints_since_cleaned)
    return {"status": "Status:  "+printer_status, "bed_temperature": printer_bed_temperature, "extruder_0_id": printer_extruder_0_id,
            "extruder_0_temperature": printer_extruder_0_temperature, "extruder_1_id": printer_extruder_1_id,
            "extruder_1_temperature": printer_extruder_1_temperature, "prints_since_cleaned": prints_since_cleaned +  " total prints" }

@app.route("/")
def home():
    return render_template("index.html")
