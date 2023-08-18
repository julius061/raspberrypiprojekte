from flask import Flask
from app import create_app
import json
import os, io, sys
from settings import checkSettings

app = create_app()

if __name__ == '__main__':
    try:
        config = checkSettings()
        app.run(host=config['hostname'], port=config['port'])
        
    except:
        print("Error.") 
        exit(1)
