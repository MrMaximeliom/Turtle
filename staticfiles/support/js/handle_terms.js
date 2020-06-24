$( document ).ready(function() {
    var language = $("#lang").text();
    if( language == 'ar'){
    $('.home-page').css('direction','rtl');
    $('.home-page').css('text-align','right');
    $(".baseContent").css('margin-left','280px');
    }
    else{
        $(".baseContent").css('margin-left','-140px');
    }
});