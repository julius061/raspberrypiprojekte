#import RPi.GPIO as GPIO
# This is definitely not the smartest way to solve this problem because there is no good way to do client / server communication trough http.server. It would be much smarter
# to use Flask or Django, however it works in this case and if not scaled, fits our needs as of right now and is more lightweight

import http.server
import socketserver

HOST_NAME = "127.0.0.1"
HOST_PORT = 8080

LED = 16 # For this example, we will use the website to control a single LED, which should be at GPIO16 (BCM)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, OUT)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.find("isButtonOnPressed=true") != -1:
            print("Button LED On Clicked!")
        elif self.path.find("isButtonOffPressed=true") != -1:
            print("Button LED Off Clicked!")
        
        return super().do_GET()
     
with socketserver.TCPServer((HOST_NAME, HOST_PORT), Handler) as httpd:
    try:
        print("Webserver started at %s:%s." % (HOST_NAME, HOST_PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Webserver stopped by user.")
        httpd.server_close()
