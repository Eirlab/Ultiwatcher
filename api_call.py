import requests


def get_printer_status(PRINTER_IP):
    '''This function will return the status of the printer'''   
    url = "http://"+PRINTER_IP+"/api/v1/printer"
    header = {"Accept": "application/json"}

    printer_status_request = requests.get(url, headers=header)

    return printer_status_request.json()

def get_current_time(PRINTER_IP):
    '''This function will return the current job of the printer'''
    url = "http://"+PRINTER_IP+"/api/v1/system/time"
    header = {"Accept": "application/json"}
    
    printer_time_request = requests.get(url, headers=header)
    
    return printer_time_request.json()

def get_printing_time_total(PRINTER_IP):
    '''This function will return the estimated time to complete the print job'''
    url = "http://"+PRINTER_IP+"/api/v1/print_job/time_total"
    header = {"Accept": "application/json"}
    
    printer_time_total_request = requests.get(url, headers=header)
    
    return printer_time_total_request.json()

def get_printing_time_elapsed(PRINTER_IP):
    '''This function will return the elapsed time of the print job'''
    url = "http://"+PRINTER_IP+"/api/v1/print_job/time_elapsed"
    header = {"Accept": "application/json"}
    
    printer_time_elapsed_request = requests.get(url, headers=header)
    
    return printer_time_elapsed_request.json()

def get_printing_progress(PRINTER_IP):
    '''This function will return the progress of the print job'''
    url = "http://"+PRINTER_IP+"/api/v1/print_job/progress"
    header = {"Accept": "application/json"}
    
    printer_progress_request = requests.get(url, headers=header)
    
    return printer_progress_request.json()

def get_printing_job(PRINTER_IP):
    '''This function will return the current job of the printer'''
    url = "http://"+PRINTER_IP+"/api/v1/print_jobs/printing"
    header = {"Accept": "application/json"}
    
    return requests.get(url, headers=header)

def get_print_preview(PRINTER_IP, UUID):
    url = "http://"+PRINTER_IP+"/cluster-api/v1/print_jobs/"+UUID+"/preview_image"
    header = {"Accept": "application/json"}
    
    return requests.get(url, headers=header)

def get_printer_name(PRINTER_IP):
    '''This function will return the name of the printer'''
    url = "http://"+PRINTER_IP+"/api/v1/system/variant"
    header = {"Accept": "application/json"}
    
    printer_name_request = requests.get(url, headers=header)
    
    return printer_name_request.json()