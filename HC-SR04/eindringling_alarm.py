import RPi.GPIO as GPIO
import time

ECHO = 24 # ECHO sits at GPIO 24
TRIG = 16 # TRIG is located at GPIO 16
BUZZ = 13 # (optional) BUZZ is located at GPIO 13

# setup the program to the bcm (board numeration) mode, so it knows which GPIO pins to access
GPIO.setmode(GPIO.BCM)

# setup the trig and buzz for output and echo for input

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)

def distanz():

    # send short signal via the trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    StartZeit = time.time()
    EndZeit = time.time()

    while GPIO.input(ECHO) == 0:
        StartZeit = time.time()

    while GPIO.input(ECHO) == 1:
        StopZeit = time.time()

    TimeElapsed = StopZeit - StartZeit

    # measure distance

    distanz = (TimeElapsed * 34300) / 2 # calculates the distance with the equation distance = 1/2 * timeElapsed * speed of sonic waves (which is 343,2m/s or 1235,5km/h)
    
    return distanz

if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            # if the distance, which should usually be a constant, suddenly changed, something must have moved between the sensor and the doorway / whatever, therefore we start the alarm
            if abstand < 20:
                print("Eindringling")
                print("Gemessen Entfernung = %.1f cm" % abstand)
                GPIO.output(BUZZ, True)
                time.sleep(0.01)
            else:
                GPIO.output(BUZZ, False)
                print("Gemessen Entfernung = %.1f cm" % abstand)
                time.sleep(0.01)
    except KeyboardInterrupt:
        print("Messung gestoppt")
        GPIO.cleanup()



