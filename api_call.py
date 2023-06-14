import requests

PRINTER_IP = "192.168.0.120"

def get_printer_status():
    '''This function will return the status of the printer'''   
    url = "http://"+PRINTER_IP+"/api/v1/printer"
    header = {"Accept": "application/json"}

    printer_status_request = requests.get(url, headers=header)

    return printer_status_request.json()

def get_current_time():
    '''This function will return the current job of the printer'''
    url = "http://"+PRINTER_IP+"/api/v1/system/time"
    header = {"Accept": "application/json"}
    
    printer_time_request = requests.get(url, headers=header)
    
    return printer_time_request.json()

def get_printing_time_total():
    '''This function will return the estimated time to complete the print job'''
    url = "http://"+PRINTER_IP+"/api/v1/print_job/time_total"
    header = {"Accept": "application/json"}
    
    printer_time_total_request = requests.get(url, headers=header)
    
    return printer_time_total_request.json()

def get_printing_time_elapsed():
    '''This function will return the elapsed time of the print job'''
    url = "http://"+PRINTER_IP+"/api/v1/print_job/time_elapsed"
    header = {"Accept": "application/json"}
    
    printer_time_elapsed_request = requests.get(url, headers=header)
    
    return printer_time_elapsed_request.json()

def get_printing_progress():
    '''This function will return the progress of the print job'''
    url = "http://"+PRINTER_IP+"/api/v1/print_job/progress"
    header = {"Accept": "application/json"}
    
    printer_progress_request = requests.get(url, headers=header)
    
    return printer_progress_request.json()

def get_printer_name():
    '''This function will return the name of the printer'''
    url = "http://192.168.0.120/api/v1/system/variant"
    header = {"Accept": "application/json"}
    
    printer_name_request = requests.get(url, headers=header)
    
    return printer_name_request.json()