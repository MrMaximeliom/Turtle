window.addEventListener("load", function(){
const loader = document.querySelector(".pre-container");
const navBar = document.getElementById("nav");
loader.className += "  hidden";
$( "#pre-loader" ).css('display','none');
navBar.className += "   fixed-top";
});
$( document ).ready(function() {
var message_box = document.getElementById("message-box");

setTimeout(function(){
   message_box.style.display = "none";
}, 2000);
});