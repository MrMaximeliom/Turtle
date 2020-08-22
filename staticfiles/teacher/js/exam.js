$( document ).ready(function() {
var language = $( "#lang" ).text();
if(language == "ar"){
$("h1").css('direction','rtl');
$("article").css('direction','rtl');
$("article").css('text-align','right');
$(".article-img").css('margin-left','16px');
}
});

