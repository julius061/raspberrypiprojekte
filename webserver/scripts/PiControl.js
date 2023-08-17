// Add event listeners to button
document.getElementById("onButton").addEventListener("click", ledOn, false);;
document.getElementById("offButton").addEventListener("click", ledOff, false);

// Turn LED on
function ledOn() {
    document.getElementById("onButtonBool").value = true;
    location.reload();
} 

// Turn LED off
function ledOff() {
    document.getElementById("offButtonBool").value = true;
    location.reload()
}