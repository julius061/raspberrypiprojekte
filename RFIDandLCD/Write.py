import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text=input("New data:")
    print("Please place your tag / card to write")
    reader.write(text)
    print("Data successfully written.")

finally:
    GPIO.cleanup()
