import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostname = "127.0.0.1"
hostport = 8000

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) # 200 = OK
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))

if __name__ == '__main__':
    webServer = HTTPServer((hostname, hostport), WebServer)
    print("Server started on http://%s:%s" % (hostname, hostport))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print("Server stopped by user.")