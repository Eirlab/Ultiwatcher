from flask import Flask, render_template, request
from api_call import *
import datetime
from flask import Response

app = Flask(__name__)

# list of all printer ips
IP_LIST = ["192.168.0.120", "192.168.0.111", "192.168.0.119"]


@app.route("/call_get_current_time/<printer_idx>")
def call_get_current_time(printer_idx):
    """This function will return the current time of the printer in utc"""
    printer_ip = IP_LIST[int(printer_idx)]
    current_time_utc = get_current_time(printer_ip)["utc"]
    current_time = datetime.datetime.utcfromtimestamp(current_time_utc).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    # add 2 hours to utc time
    current_time = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    current_time = current_time + datetime.timedelta(hours=2)
    # only return the time
    current_time = current_time.strftime("%H:%M")
    resp = Response(
        str(current_time)
        + "<img src='static/eirlab.png' style='margin-left:30px;' width='auto' height='80'>"
    )
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/call_get_printing_time_total/<printer_idx>")
def call_get_printing_time_total(printer_idx):
    """This function will return the estimated time to complete the print job"""
    printer_ip = IP_LIST[int(printer_idx)]
    printing_time_total_utc = get_printing_time_total(printer_ip)
    try:
        printing_time_total = datetime.datetime.utcfromtimestamp(
            printing_time_total_utc
        ).strftime("%H:%M:%S")
    except:
        printing_time_total = "00:00:00"
    return "Estimated print time: " + str(printing_time_total)


@app.route("/call_get_printing_time_left/<printer_idx>")
def call_get_printing_time_left(printer_idx):
    """This function will return the estimated time left to complete the print job"""
    printer_ip = IP_LIST[int(printer_idx)]
    printing_time_total_utc = get_printing_time_total(printer_ip)
    printing_time_elapsed_utc = get_printing_time_elapsed(printer_ip)
    try:
        printing_time_left = printing_time_total_utc - printing_time_elapsed_utc
        if printing_time_left <= 0:
            printing_time_left = "0"
        else:
            printing_time_left = datetime.datetime.utcfromtimestamp(
                printing_time_left
            ).strftime("%H:%M:%S")
    except:
        printing_time_left = "00:00:00"

    return "Time remaining: " + str(printing_time_left)


@app.route("/call_get_printing_time_elapsed/<printer_idx>")
def call_get_printing_time_elapsed(printer_idx):
    """This function will return the elapsed time of the print job"""
    printer_ip = IP_LIST[int(printer_idx)]
    printing_time_elapsed_utc = get_printing_time_elapsed(printer_ip)
    try:
        printing_time_elapsed = datetime.datetime.utcfromtimestamp(
            printing_time_elapsed_utc
        ).strftime("%H:%M:%S")
    except:
        printing_time_elapsed = "00:00:00"
    return "Time elapsed: " + str(printing_time_elapsed)


@app.route("/call_get_camera_feed/<printer_idx>")
def call_get_camera_feed(printer_idx):
    """This function will return the camera feed of the printer"""
    printer_ip = IP_LIST[int(printer_idx)]
    return (
        '<img id="camera_feed" class="printer_0 printer_1 printer_2" style="border-radius:10px; width: 400px; '
        'height: 300px;" src="http://'
        + str(printer_ip)
        + ':8080/?action=stream" alt="">'
    )


@app.route("/call_get_printing_progress/<printer_idx>")
def call_get_printing_progress(printer_idx):
    """This function will return the progress of the print job"""
    printer_ip = IP_LIST[int(printer_idx)]
    printing_progress = get_printing_progress(printer_ip)
    try:
        if printing_progress["message"] != None:
            printing_progress = 1
    except:
        print(printing_progress)
    return str(printing_progress)


@app.route("/call_get_printer_name/<printer_idx>")
def call_get_printer_name(printer_idx):
    """This function will return the name of the printer"""
    printer_ip = IP_LIST[int(printer_idx)]
    return str(get_printer_name(printer_ip))


@app.route("/call_get_printing_job/<printer_idx>")
def call_get_printing_job(printer_idx):
    """This function will return the current job of the printer"""
    printer_ip = IP_LIST[int(printer_idx)]
    printing_job_body = get_printing_job(printer_ip).content
    printing_job_body = printing_job_body.decode("utf-8")

    try:
        print_name = (
            printing_job_body.split('"name":')[1].split(",")[0].replace('"', "")
        )
        print_status = (
            printing_job_body.split('"status":')[1].split(",")[0].replace('"', "")
        )
        print_uuid = (
            printing_job_body.split('"uuid":')[1]
            .split(",")[0]
            .replace('"', "")
            .replace("}", "")
        )
        print_preview = (
            "<img src='http://"
            + str(printer_ip)
            + "/cluster-api/v1/print_jobs/"
            + str(print_uuid)
            + "/preview_image>"
        )

        if print_status == "printing":
            print_status = (
                "<span style='font-weight:bold;color:#3B7CDC;'>PRINTING</span>"
            )
        if print_status == "wait_cleanup":
            print_status = (
                "<span style='font-weight:bold;color:#E77C3F;'>FINISHED</span>"
            )
        if print_status == "pre_print":
            print_status = (
                "<span style='font-weight:bold;color:#75CD67;'>PREPARING</span>"
            )
    except:
        print_name = "No current print"
        print_preview = (
            "<img src='https://static.thenounproject.com/png/4959299-200.png' >"
        )
        print_status = "<span style='font-weight:bold;color:#575757;'>READY</span>"
    return {
        "name": "Print name: " + print_name,
        "preview": print_preview,
        "status": "Status: " + print_status,
    }


@app.route("/call_get_start_time/<printer_idx>")
def call_get_start_time(printer_idx):
    """This function will return the start time of the print job"""
    printer_ip = IP_LIST[int(printer_idx)]
    printing_job_body = get_printing_job(printer_ip).content
    printing_job_body = printing_job_body.decode("utf-8")

    try:
        start_time = (
            printing_job_body.split('"created_at":')[1].split(",")[0].replace('"', "")
        )
        start_time = start_time[len(start_time) - 15 : len(start_time) - 7]
        start_time = str(
            datetime.datetime.strptime(start_time, "%H:%M:%S")
            + datetime.timedelta(hours=2)
        )
        start_time = start_time[len(start_time) - 8 : len(start_time)]
    except:
        start_time = "00:00:00"
    print(start_time)
    return "Start time: " + str(start_time)


@app.route("/call_get_printer_status/<printer_idx>")
def call_get_printer_status(printer_idx):
    """This function will return the status of the printer"""
    printer_ip = IP_LIST[int(printer_idx)]
    printer_status_json = get_printer_status(printer_ip)
    printer_status = printer_status_json["status"]
    if printer_status == "idle":
        printer_status = "<span style='font-weight:bold;color:#575757;'>READY</span>"
    printer_bed_temperature = printer_status_json["bed"]["temperature"]["current"]
    printer_head = printer_status_json["heads"][0]

    printer_extruder_0_id = printer_head["extruders"][0]["hotend"]["id"]
    printer_extruder_0_temperature = printer_head["extruders"][0]["hotend"][
        "temperature"
    ]["current"]

    printer_extruder_1_id = printer_head["extruders"][1]["hotend"]["id"]
    printer_extruder_1_temperature = printer_head["extruders"][1]["hotend"][
        "temperature"
    ]["current"]

    prints_since_cleaned = printer_head["extruders"][0]["hotend"]["statistics"][
        "prints_since_cleaned"
    ]
    return {
        "status": "Status:  " + printer_status,
        "bed_temperature": printer_bed_temperature,
        "extruder_0_id": printer_extruder_0_id,
        "extruder_0_temperature": printer_extruder_0_temperature,
        "extruder_1_id": printer_extruder_1_id,
        "extruder_1_temperature": printer_extruder_1_temperature,
        "prints_since_cleaned": prints_since_cleaned + " total prints",
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/com")
def com():
    return render_template("com.html")


@app.route("/upload", methods=["POST"])
def upload():
    data = request.files["file"]
    data.save("static/" + "com.png")
    return "File uploaded"
