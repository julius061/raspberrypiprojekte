from PCF8574 import PCF8574_GPIO as GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD as LCD
import time
PCF8574_ADDR = 0x27
PCF8574A_ADDR = 0x3F
MAX_LEN = 17

try:
    mcp = GPIO(PCF8574_ADDR)
except:
    try:
        mcp = GPIO(PCF8574A_ADDR)
    except:
        print("Invalid I2C Address.")
        exit(1)

lcd = LCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
mcp.output(3,1)
lcd.begin(16,2)


# TODO: fix this hardcoded bullshit, animation does not work correctly yet
def input_one():
    input_str = str(input("Please enter something ( 14 or less characters is optimal )"))
    input_arr = [char for char in input_str]
    formatted_string = ""
    if len(input_str) < 16:
        whitespace_padding = " " * 16
        formatted_string = whitespace_padding + input_str
    back_arr = [char for char in formatted_string]
    
    while True:

        lcd.clear()
    
        lcd.setCursor(0,0)
        for i in range(MAX_LEN):
            print("in", i)
            lcd.clear()
            lcd.setCursor(0,0)
            for char in input_arr:
                lcd.message(char)
            input_arr.insert(0, " ")
            time.sleep(0.2)
            if i == MAX_LEN - 1:
                input_arr = [char for char in input_str]
    
        for i in range(MAX_LEN + len(input_str) - 1):
            print("out", i)
            lcd.clear()
            lcd.setCursor(0,1)
            for char in back_arr:
                lcd.message(char)
            back_arr.pop(0)
            time.sleep(0.2)
            if i == MAX_LEN + len(input_str) - 2:
                back_arr = [char for char in formatted_string]







while True:
    try:
        input_one()
    except KeyboardInterrupt:
        lcd.clear()
        break
