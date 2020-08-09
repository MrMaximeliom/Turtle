$( document ).ready(function() {
    var language = $( "#lang" ).text();
     if( language == 'ar'){
     console.log( "arabic now!" );
     $(".field").addClass('arabic');
     $( "#exam-name" ).removeClass('exam-name');
      $( "#exam-name" ).addClass('exam-name-arabic');
      $( "#exam-notes" ).removeClass('exam-notes');
      $( "#exam-notes" ).addClass('exam-notes-arabic');
      $('.first-field').each(function(){
      $(this).removeClass('first-field');
      $(this).addClass('first-field-arabic');
      });
       $( "#save-btn" ).addClass('ml-5');
      $( "#cancel-btn" ).removeClass('ml-5');
       $("#exam-period-div").css('right','5%');
     }
     $("#id_exam_date").focus(function(){
      $("#id_exam_date").get(0).type='date';
     });
     });



