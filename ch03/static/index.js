const img = document.getElementById("image");

function ON_click() {
    img.src="../static/on.png"
	location.href='http://10.150.0.243:5000/on'
}

function OFF_click() {
    img.src = "../static/off.png"
location.href='http://10.150.0.243:5000/off'
}
