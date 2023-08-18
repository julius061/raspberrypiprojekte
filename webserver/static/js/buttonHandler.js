document.getElementById("test-btn").addEventListener("click", function() {
	console.log("debug");
	sendDataToServer();
});

document.getElementById("add-component-btn").addEventListener("click", function() {
	addComponent();
});

function addComponent() {
	var component_data = {
		"PinNum" : document.getElementById("add-component-input").value,
		"ComponentType" : document.getElementById("component-type").value,
	};
	console.log(component_data);
}

function sendDataToServer() {
	var testValue = "test value"
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/send-variable", true);
	xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4 && xhr.status === 200) {
				
		}
	};
	xhr.send(JSON.stringify(({ variable: testValue })));

}
