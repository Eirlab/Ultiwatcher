# Ultiwatcher

This project is a follow up to Eirlab's [ultimaker-screen](https://github.com/Eirlab/ultimaker-screen) made by Antoine Pringalle and Sébastein Delpeuch. 

This app's purpose is to monitor Eirlab's Ultimaker 3D printers using Ultimakers local API. It is made to run locally with Flask in order to display the printers status on a Eirlab's TV screen.

## Installation

```bash
    pip install Flask
    git clone https://github.com/Eirlab/Ultiwatcher
    cd Ultiwatcher
    python3 -m venv .venv
    . .venv/bin/activate
```

## Usage

```bash
    flask --app app run
```

Currently printers' IP addresses are hardcoded in the app.py file. You can change them to match your printers' IP addresses in the IP_LIST variable.

## Contribution

New features and ideas for features of this screen are welcome! Access to the 3D printers API can only be done via the eirlabIoT network currently.