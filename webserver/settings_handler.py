import os, sys
import json

SETTINGS_FILE = "settings.json"
DEFAULT_SETTINGS_FILE = "default_settings.json"

STATUS_JSON_CHECKING = f"Checking {SETTINGS_FILE}..."
STATUS_JSON_SUCCESS = f"{SETTINGS_FILE} successfully loaded."
STATUS_JSON_ERROR = f"There was an error with your {SETTINGS_FILE} file. Try restarting the program or generating a new one."
STATUS_JSON_PROMPT = f"{SETTINGS_FILE} does not exist or is not readable. Do you want to generate a new one? (y/n) --> "

def checkSettings():

    if os.path.isfile(SETTINGS_FILE) and os.access(SETTINGS_FILE, os.R_OK):
        try:
            with open(SETTINGS_FILE) as settings_file:
                settings_content = json.load(settings_file)
                print(STATUS_JSON_SUCCESS)
                return settings_content
        except OSError:
            print(STATUS_JSON_ERROR)
    else:
        # user should decide if he wants to generate a new settings file
        choice = str(input(STATUS_JSON_PROMPT))
        if choice == "y":

            with open(DEFAULT_SETTINGS_FILE , "r") as default_settings_file:
                default_settings = json.load(default_settings_file)

            with open(SETTINGS_FILE, 'w') as settings_file:
                json.dump(default_settings, settings_file, indent=4)

            return default_settings

        else:
            print(STATUS_JSON_ERROR)
            exit(1)
