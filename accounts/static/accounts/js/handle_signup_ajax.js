$( document ).ready(function() {
$("#id_password1").change(function () {
      password1 =  $(this).val();
      var form = $(this).closest("form");
      error_container = document.querySelector("#password1_error")
      password1_hint = document.querySelector("#hint_id_password1")
      $.ajax({
        url: form.attr("data-validate-password-url"),
        data: form.serialize(),
        dataType: 'json',
        success: function (data) {
          if (data.is_invalid) {
//            alert(data.error_message);

         $("#id_password1").addClass("is-invalid");
          error = '<strong>'+data.error_message+'</strong>';
          $("#password1_error").css('display','block');
          $("#hint_id_password1").css('display','none');
          error_container.innerHTML = error;

          }
          else{
          $("#id_password1").removeClass("is-invalid");
           $("#password1_error").css('display','none');
           $("#hint_id_password1").css('display','block');
           console.log('here')
          }
        }
      });;

});

$("#id_username").change(function () {
      username =  $(this).val();
      var form = $(this).closest("form");
      error_container = document.querySelector("#username_error")
   $.ajax({
        url: form.attr("data-validate-username-url"),
        data: form.serialize(),
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
//            alert(data.error_message);

         $("#id_username").addClass("is-invalid");
          error = '<strong>'+data.error_message+'</strong>';
          $("#username_error").css('display','block');
          error_container.innerHTML = error;

          }
          else{
          $("#id_username").removeClass("is-invalid");
           $("#username_error").css('display','none');
          }
        }
      });;


    });

});