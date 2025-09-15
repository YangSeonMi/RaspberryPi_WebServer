
send = document.getElementById("send");
plus = document.getElementById("plus");

n = 0

send.addEventListener("click", function() {
  location.href='http://10.150.0.243:5000/save'+n;
  n = 0;
  num.innerHTML = n;
});

plus.addEventListener("click", function() {
  n+=1;
});

setInterval(() => {
  document.querySelector("h2").innerHTML=n;  
}, 100);
