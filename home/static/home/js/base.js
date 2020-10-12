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
$("#user-dropDown" ).css('text-align','right');
$("#user-dropDown" ).css('direction','rtl');


}
//disabled for now
//setTimeout(function(){
//   message_box.style.display = "none";
//}, 2000);
});