   window.onload = function() {
            document.getElementById("id_first_name").focus();
        }
$( document ).ready(function() {

    console.log( "ready!" );
    var language = $( "#lang" ).text();
    var button = $('#ar').text()
    const agreeCheckBox = document.getElementById('agreeCheckBox');
    const signupBtn = document.getElementById('signupBtn');
    console.log( language );
    console.log( button );
    if( language == 'ar'){
       $(".home-page").css('text-align','right');
       $(".home-page small").css('direction','rtl');
       $(".field label").css('margin-right','18px');
       $(".form-check").css('direction','rtl');
       $(".form-check").css('margin-left','auto');
       $("input[type='radio']").css('margin-left','5px');
        $("input[type='radio']").css('cursor','pointer');
       $("input[type='text']").css('text-align','right');
       $(".border-bottom-title").css('direction','rtl');
       $(".border-bottom-title ").css('margin-left','auto');
       $("#signup-btn").css('margin-left','auto');
       $("#agreeCheckBox").removeClass('handle-agree-checkbox');
       $("#agreeCheckBox").css('margin-left','8px');
       $("#agreeContainer").css('direction','rtl');
       $("#agreeContainer").css('position','relative');
       $("#agreeContainer").css('bottom','10%');


    }
    else{
 $("input[type='radio']").css('margin-right','5px');
 $("input[type='radio']").css('vertical-align','-3px');
 $("input[type='radio']").css('cursor','pointer');

    }

$(document).on('click', '#agreeCheckBox', function() {
if(agreeCheckBox.checked){
signupBtn.disabled = false;
signupBtn.style.setProperty('background', '#E77B73')
signupBtn.style.setProperty('cursor', 'pointer')
}
else{
signupBtn.disabled = true;
signupBtn.style.setProperty('background', '#FFA39B')
signupBtn.style.setProperty('cursor', 'not-allowed')


}
console.log(agreeCheckBox.checked)

});


});
