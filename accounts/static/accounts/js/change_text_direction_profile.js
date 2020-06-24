$( document ).ready(function() {
    console.log( "ready!" );
    var language = $( "#lang" ).text();
    var button = $('#ar').text()
    console.log( language );
    console.log( button );
    if( language == 'ar'){
       $(".home-page").css('text-align','right');
       $(".home-page small").css('direction','rtl');
       $(".field label").css('margin-right','18px');
       $(".form-check").css('direction','rtl');
       $(".form-check").css('margin-left','auto');
       $("input[type='radio']").css('margin-left','5px');
       $("input[type='text']").css('text-align','right');
       $(".border-bottom-title").css('direction','rtl');
       $(".border-bottom-title ").css('margin-left','auto');
       $("#signup-btn").css('margin-left','auto');


    }

});
