// Add event listeners to button
document.getElementById("onButton").addEventListener("click", ledOn, false);;
document.getElementById("offButton").addEventListener("click", ledOff, false);

// Turn LED on
function ledOn() {
	// Send a GET Request with parameters so the python backend knows what to do
	// It does not matter that this is not a valid URL, nothing will happen and it contains
	// isButtonOnPressed=true which is the only thing the python scripts looks for, therefore
	// this works ...
	fetch("isButtonOnPressed=true");

	
} 

// Turn LED off
function ledOff() {
	fetch("isButtonOffPressed=true");
}
