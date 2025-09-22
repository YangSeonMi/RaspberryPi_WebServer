const on = document.getElementById("ON");
const off = document.getElementById("OFF");

function ON_click() {
    on.style.opacity = 1;
    off.style.opacity = 0;
}

function OFF_click() {
    on.style.opacity = 0;
    off.style.opacity = 1;
}
