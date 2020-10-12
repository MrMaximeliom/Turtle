$( document ).ready(function() {
var language = $( "#lang" ).text();
if(language == "ar"){
$("h1",".col-md-4").css('direction','rtl');
$(".col-md-4").css('text-align','right');
$("article").css('direction','rtl');
$("article").css('text-align','right');
$(".article-img").css('margin-left','16px');
$("#searchForm").css('direction','rtl');
$("#searchForm").css('margin-right','200px');
}
});

