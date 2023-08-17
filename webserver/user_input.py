import RPi.GPIO as GPIO

# saves us some writing later
OUT = GPIO.OUT
IN = GPIO.IN
LOW = GPIO.LOW
HIGH = GPIO.HIGH

# Handles user input in the beginning
def getUserInput():
    HOSTNAME = str(input("Please enter the hostname --> "))
    HOSTPORT = int(input("Please enter the port --> "))
    amountComponents = int(input("Please tell me how many components you need --> "))
    for x in range(amountComponents):
        location = int(input(f"Where should component {x} be located at? --> "))
        choice = str(input(f"Is component {x} IN or OUT? --> "))
        if choice == "IN":
           GPIO.setup(location, IN)
        elif choice == "OUT":
            GPIO.setup(location, OUT)
        else:
            print("Incorrect input.")

    return (HOSTNAME, HOSTPORT)


