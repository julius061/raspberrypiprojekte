var http = require('http').createServer(handler);
var fileSystem = require('fs'); // filesystem module
var io = require('socket.io')(http) // require socketio and pass http object (server)i
var GPIO = require("onoff").Gpio;
var LED = new GPIO(16, 'out');
http.listen(8080);

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

io.sockets.on("connection", function(socket) {
	var lightvalue = 0;
	socket.on("light", function(data) {
		lightvalue = data;
		if(lightvalue != LED.readSync()) {
			LED.writeSync(lightvalue);
		}
	});
});
