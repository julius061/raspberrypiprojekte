from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from mfrc522 import SimpleMFRC522
from time import sleep, strftime
from datetime import datetime
import threading
import queue

PCF8574_ADDR = 0x27
PCF8574A_ADDR = 0x3F

text_queue = queue.Queue()  # Queue for storing RFID tag data

def getTime():
    return datetime.now().strftime('    %H:%M:%S')

def readInputLoop():
    reader = SimpleMFRC522()  # Initialize the RFID reader here
    while True:
        _, new_text = reader.read()  # Read the text
        sleep(2)
        text_queue.put(new_text)  # Put the text in the queue

def printDisplayLoop():
    try:
        mcp = PCF8574_GPIO(PCF8574_ADDR)
    except:
        try:
            mcp = PCF8574_GPIO(PCF8574A_ADDR)
        except:
            print("I2C Address Error.")
            exit(1)

    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)
    mcp.output(3,1)
    lcd.begin(16, 2)

    while True:
        try:
            current_text = text_queue.get(timeout=0.1)  # Get text from the queue
        except queue.Empty:
            current_text = ""

        lcd.setCursor(0, 0)
        lcd.message(getTime() + "\n" + current_text)
        sleep(1)

if __name__ == '__main__':
    lcd_thread = threading.Thread(target=printDisplayLoop)
    rfid_thread = threading.Thread(target=readInputLoop)

    try:
        lcd_thread.start()
        rfid_thread.start()

        lcd_thread.join()
        rfid_thread.join()
    except:
        lcd.clear()
        exit(1)
