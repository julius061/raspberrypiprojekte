import RPi.GPIO as GPIO
# This is definitely not the smartest way to solve this problem because there is no good way to do client / server communication trough http.server. It would be much smarter
# to use Flask or Django, however it works in this case and if not scaled, fits our needs as of right now and is more lightweight

import http.server
import socketserver
import user_input

HOSTNAME, HOSTPORT = user_input.getUserInput()
LED = 16
HIGH = GPIO.HIGH
LOW = GPIO.LOW
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.find("isButtonOnPressed=true") != -1:
            print("Button LED On Clicked!")
            GPIO.output(LED, HIGH)
        elif self.path.find("isButtonOffPressed=true") != -1:
            print("Button LED Off Clicked!")
            GPIO.output(LED, LOW)
        return super().do_GET()
     
with socketserver.TCPServer((HOSTNAME, HOSTPORT), Handler) as httpd:
    try:
        print("Webserver started at %s:%s." % (HOSTNAME, HOSTPORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Webserver stopped by user.")
        httpd.server_close()

