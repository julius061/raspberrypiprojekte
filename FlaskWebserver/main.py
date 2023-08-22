from flask import Flask
from app import create_app
import json
import os, io, sys
import RPi.GPIO as GPIO
from settings_handler import checkSettings
from gpio_handler import setup_gpio

app = create_app()

if __name__ == '__main__':
    try:
        config = checkSettings()
        setup_gpio()
        app.run(host=config['hostname'], port=config['port'])
    except:
        print("Error.") 
        exit(1)
