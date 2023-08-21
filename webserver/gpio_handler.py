import RPi.GPIO as GPIO

PREFIX = "[GPIO Handler] --> "

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print(f"{PREFIX} GPIO setup complete.")

def handle_gpio_cmd(pinNum, command):
    GPIO.setup(pinNum, GPIO.OUT)
    if command == "off":
        GPIO.output(pinNum, GPIO.LOW)
        print(f"{PREFIX} GPIO {pinNum} off")
    elif command == "on":
        GPIO.output(pinNum, GPIO.HIGH)
        print(f"{PREFIX} GPIO {pinNum} on")
    else:
        print("There was an error with your input.")

