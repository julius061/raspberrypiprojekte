document.getElementById("add-component-btn").addEventListener("click", function() {
	addComponent();
});

document.getElementById("del-component-btn").addEventListener("click", function() {
	delComponent();
});

let buttonList = []; // list of all buttons to be able to check for duplicates

function addComponent() {
	let isInList = false;
	// get component data from frontend for AJAX POST request
	var component_data = {
		"PinNum" : document.getElementById("add-component-input").value,
		"ComponentType" : document.getElementById("component-type").value,
	};
	for(var i = 0; i < buttonList.length; i++) {
	   if(buttonList[i] === `buttonfor${component_data.PinNum}`) {
	   	isInList = true;
	   }
	}
	if(isInList) {
	
	} else {
	buttonList.push(`buttonfor${component_data.PinNum}`);
	var new_button = document.createElement("button");
	new_button.classList.add('control_buttons');
	new_button.setAttribute("id", `buttonfor${component_data.PinNum}`);
	console.log(new_button);
	button_name = `Toggle PIN ${component_data.PinNum}`;
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
		};
		
		GPIOxhr.send(JSON.stringify((gpio_data)));
	};
		var container = document.getElementById("content-field");
		container.appendChild(new_button);
	} 
}

function delComponent() {
	let componentName = `buttonfor${document.getElementById("add-component-input").value}`;
	if(buttonList.includes(componentName)) {
		var component = document.getElementById(componentName);
		buttonList.splice(buttonList.indexOf(componentName), 1);
		return component.parentNode.removeChild(component);
	} else {
	}
}

