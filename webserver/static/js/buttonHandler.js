document.getElementById("add-component-btn").addEventListener("click", function() {
	addComponent();
});

function addComponent() {
	var component_data = {
		"PinNum" : document.getElementById("add-component-input").value,
		"ComponentType" : document.getElementById("component-type").value,
	};
	
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/add-button", true);
	xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4 && xhr.status === 200) {
		
		}
	};
	xhr.send(JSON.stringify((component_data)));
	
	var new_button = document.createElement("button");
	var parsedData = JSON.parse(component_data);
	if(parsedData.ComponentType === "button_on") {
		button_name = ```Toggle PIN {parsedData.PinNum}```;
		new_button.textContent = button_name;
	} else if(parsedData.ComponentType === "button_off") {
		button_name = ```Toggle PIN {parsedData.PinNum} off}```;
		new_button.textContent = button_name;
	}
	console.log("debug123");
	button.onclick = function() {
		console.log("debug"); // TODO: actual AJAX request to server to handle GPIO
	};

	var container = document.getElementById("content-field");
	container.appendChild(new_button);
}
