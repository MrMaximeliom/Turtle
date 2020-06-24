$( document ).ready(function() {
    console.log( "ready!" );
    var language = $( "#lang" ).text();
    if (language == 'ar'){
      $(".home-page").css('text-align','right');
      $("#signup-btn").css('margin-left','-73px');

    }

    });
