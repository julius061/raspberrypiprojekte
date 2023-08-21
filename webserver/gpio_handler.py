import RPi.GPIO as GPIO

PREFIX = "[GPIO Handler] --> "

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print(f"{PREFIX} GPIO setup complete.")

def handle_gpio_cmd(pinNum):
    GPIO.setup(pinNum, GPIO.OUT)
    if GPIO.input(pinNum):
        GPIO.output(pinNum, GPIO.LOW)
    else:
        GPIO.output(pinNum, GPIO.HIGH)
