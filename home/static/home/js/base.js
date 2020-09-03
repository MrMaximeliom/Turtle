window.addEventListener("load", function(){
const loader = document.querySelector(".pre-container");
const navBar = document.getElementById("nav");
loader.className += "  hidden";
$( "#pre-loader" ).css('display','none');
navBar.className += "   fixed-top";
});
$( document ).ready(function() {
var language = $( "#lang" ).text();
var message_box = document.getElementById("message-box");
if (language == "ar"){
$( ".message-box" ).css('direction','rtl');
}
setTimeout(function(){
   message_box.style.display = "none";
}, 2000);
});