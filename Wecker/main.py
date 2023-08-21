from flask import Flask
from app import create_app
import json
import sys
import RPi.GPIO as GPIO
from settings_handler import checkSettings

app = create_app()

if __name__ == '__main__':
    try:
        config = checkSettings()
        app.run(host=config['hostname'], port=config['port'])
    except:
        print("Error.") 
        exit(1)