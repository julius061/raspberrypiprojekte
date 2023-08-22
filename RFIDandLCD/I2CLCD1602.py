from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from mfrc522 import SimpleMFRC522
from time import sleep, strftime
from datetime import datetime
import threading

reader = SimpleMFRC522() # initialize rfid card io
loggedIn = False

def get_time_now():     
    return datetime.now().strftime('    %H:%M:%S')
 

def readRFID():
    global loggedIn
    _, text = reader.read()
    if text:
        loggedIn = True
    else:
        loggedIn = False
    return text

def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of lines and cols
    while(True):
        global loggedIn
        if not loggedIn:
            _, text = reader.read()
            if not text:
                lcd.setCursor(0, 0)
                lcd.message( get_time_now() + "\n")
                sleep(1)
                continue
            else:
                loggedIn = True
                lcd.setCursor(0,0)
                lcd.message( get_time_now() + "\n")
                lcd.sleep(1)
        else:
            lcd.setCursor(0,0)
            lcd.message( get_time_now() + "\n")   # display the time
            lcd.message(f"Hello, {text}")
            sleep(1)i
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)

# Create LCD, passing in MCP GPIO adapter
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
