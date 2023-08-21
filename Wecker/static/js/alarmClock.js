const dateDisplay = document.getElementById("dateDisplay");
const timeDisplay = document.getElementById("timeDisplay");
const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
// Need to call this once so time will be displayed before 1 second is over when first loading site
updateTime();
function updateTime() {
	const NOW = new Date();
	const YEAR = NOW.getFullYear().toString();
	const MONTH = (NOW.getMonth() + 1).toString(); // index starts at 0:P
	const DAY = NOW.getDate().toString();
	const DAY_NAME = weekdays[NOW.getDay()];
	const HOURS = NOW.getHours().toString().padStart(2, '0');
	const MINUTES = NOW.getMinutes().toString().padStart(2, '0');
	const SECONDS = NOW.getSeconds().toString().padStart(2, '0');
	
	const timeDisplayText = `${HOURS}:${MINUTES}:${SECONDS}`;
	const dateDisplayText = `${DAY_NAME}, ${DAY}.${MONTH}.${YEAR}`;
	
	timeDisplay.innerHTML = timeDisplayText;
	dateDisplay.innerHTML = dateDisplayText;
}
setInterval(updateTime, 1000);
