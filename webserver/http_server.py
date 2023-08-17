#import RPi.GPIO as GPIO
import http.server
import socketserver

HOST_NAME = "127.0.0.1"
HOST_PORT = 8080

LED = 16 # For this example, we will use the website to control a single LED, which should be at GPIO16 (BCM)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, OUT)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST_NAME, HOST_PORT), Handler) as httpd:
    try:
        print("Webserver started at %s:%s." % (HOST_NAME, HOST_PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Webserver stopped by user.")
        httpd.server_close()
