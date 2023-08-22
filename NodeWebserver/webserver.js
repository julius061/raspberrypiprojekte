// I am new to JavaScript and the sole purpose of this project is for me to learn about certain things. 
// Therefore, everything here will be commented out explaining every single step

var http = require('http').createServer(handler); // Imports http module and uses createServer function that is passed another function named handler which will handle incoming http requests

var fileSystem = require('fs'); // filesystem module
var io = require('socket.io')(http) // import socketio and initializes it with the server, which allows the script to set up websocket communication between client and server

var GPIO = require("onoff").Gpio; // interface for GPIO pins, uses BCM (Broadcom) Pin numbering
var LED = new GPIO(16, 'out'); // create instance of LED at GPIO 16 as an output

http.listen(8080); // server should listen on port 8080


// the handler function reads contents of the index.html in the public folder and serves it as http response
function handler(req, res) {
	fileSystem.readFile(__dirname + '/public/index.html', function(err, data) {
		if(err) {
			res.writeHead(404,{'Content-Type' : 'text/html'});
			return res.end("404 Not Found");
		}
		res.writeHead(200, {'Content-Type' : 'text/html'});
		res.write(data);
		return res.end();
	});
}

// if there is a socket connection, the dfefault lightvalue will be 0, if someone send the light event ( triggered by the checkbox ) the lightvalue will be updated
io.sockets.on("connection", function(socket) {
	var lightvalue = 0;
	socket.on("light", function(data) {
		lightvalue = data;
		if(lightvalue != LED.readSync()) {
			LED.writeSync(lightvalue);
		}
	});
});
