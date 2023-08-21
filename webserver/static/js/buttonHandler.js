document.getElementById("add-component-btn").addEventListener("click", function() {
	addComponent();
});

function addComponent() {

	// get component data from frontend for AJAX POST request
	var component_data = {
		"PinNum" : document.getElementById("add-component-input").value,
		"ComponentType" : document.getElementById("component-type").value,
	};
	
	let xhr = new XMLHttpRequest();
	xhr.open("POST", "/add-button", true);
	xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4 && xhr.status === 200) {
			// not needed as of right now
		}
	};
	// send AJAX POST request with component data, ( handling happens @app.route("add-button") )
	xhr.send(JSON.stringify((component_data)));
	
	var new_button = document.createElement("button");

	if(component_data.ComponentType === "button_on") {
		button_name = `Toggle PIN ${component_data.PinNum} on`;
		new_button.innerHTML = button_name;
		
		// Send AJAX request to handle buttons GPIO function
        	new_button.onclick = function() {
                let GPIOxhr = new XMLHttpRequest();
                GPIOxhr.open("POST", "/handle-gpio", true);
                GPIOxhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                GPIOxhr.onreadystatechange = function() {
                        if(GPIOxhr.readyState === 4 && GPIOxhr.status === 200) {
                                // not needed as of right now
                        }
                };
                var gpio_data = {
			"PinNum" : component_data.PinNum,
			"Command" : "on",
		};
		console.log("debug81273217");
		console.log(gpio_data);
		GPIOxhr.send(JSON.stringify((gpio_data)));
	};
	} else if(component_data.ComponentType === "button_off") {

		button_name = `Toggle PIN ${component_data.PinNum} off`;
		new_button.innerHTML = button_name;
 		// Send AJAX request to handle buttons GPIO function
        	new_button.onclick = function() {
                let GPIOxhr = new XMLHttpRequest();
                GPIOxhr.open("POST", "/handle-gpio", true);
                GPIOxhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                GPIOxhr.onreadystatechange = function() {
                        if(GPIOxhr.readyState === 4 && GPIOxhr.status === 200) {
                                // not needed as of right now
                        }
                };
		var gpio_data = {
			"PinNum" : component_data.PinNum,
			"Command" : "off",
		};
		console.log(gpio_data);
		GPIOxhr.send(JSON.stringify((gpio_data)));
	
		}
	};

	var container = document.getElementById("content-field");
	container.appendChild(new_button);
}
