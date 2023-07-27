import requests

header = {"Accept": "application/json"}


def get_printer_name(PRINTER_IP):
    """This function will return the name of the printer to the server"""
    url = "http://" + PRINTER_IP + "/api/v1/system/variant"

    printer_name_request = requests.get(url, headers=header)

    return printer_name_request.json()


def get_printer_status(PRINTER_IP):
    """This function will return the status of the printer to the server"""
    url = "http://" + PRINTER_IP + "/api/v1/printer"

    printer_status_request = requests.get(url, headers=header)

    return printer_status_request.json()


def get_current_time(PRINTER_IP):
    """This function will return the current job of the printer to the server"""
    url = "http://" + PRINTER_IP + "/api/v1/system/time"

    printer_time_request = requests.get(url, headers=header)
    return printer_time_request.json()


def get_printing_time_total(PRINTER_IP):
    """This function will return the estimated time to complete the print job to the server"""
    url = "http://" + PRINTER_IP + "/api/v1/print_job/time_total"

    printer_time_total_request = requests.get(url, headers=header)

    return printer_time_total_request.json()


def get_printing_time_elapsed(PRINTER_IP):
    """This function will return the elapsed time of the print job to the server"""
    url = "http://" + PRINTER_IP + "/api/v1/print_job/time_elapsed"

    printer_time_elapsed_request = requests.get(url, headers=header)

    return printer_time_elapsed_request.json()


def get_printing_progress(PRINTER_IP):
    """This function will return the progress of the print job to the server"""
    url = "http://" + PRINTER_IP + "/api/v1/print_job/progress"

    printer_progress_request = requests.get(url, headers=header)
    return printer_progress_request.json()


def get_printing_job(PRINTER_IP):
    """This function will return the current job of the printer to the server"""
    url = "http://" + PRINTER_IP + "/cluster-api/v1/print_jobs/"

    return requests.get(url, headers=header)


def get_print_preview(PRINTER_IP, UUID):
    """This function will return the preview of the current job of the printer to the server"""
    url = (
        "http://" + PRINTER_IP + "/cluster-api/v1/print_jobs/" + UUID + "/preview_image"
    )

    return requests.get(url, headers=header).content
