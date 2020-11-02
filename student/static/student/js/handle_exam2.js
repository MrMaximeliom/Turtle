$( document ).ready(function() {

var translations = JSON.parse(document.getElementById('my-translations').textContent);
var questions_of_exam = JSON.parse(document.getElementById('my-questions').textContent);
var questions_links = document.querySelectorAll('.js-question-page');
var language = $( "#lang" ).text();
let num_pages;
let per_page;
let answers = {};
var counter = 0;
if (!localStorage.getItem("counter_questions")){

localStorage.setItem("counter_questions",parseInt(0,10));
}

var counterQuestion = 0;
let selectedQuestion;
var page = 1;
if (questions_of_exam > 1 ){
 per_page =document.querySelector('#per_page').innerHTML;
 num_pages = document.querySelector('#num_pages').innerHTML;

for(i=0; i<questions_links.length;i++){
question_id = questions_links[i].querySelector( '#question_id' ).innerHTML;

questions_links[i].href = "?page="+page+"#"+question_id;
++counter;
if(counter % per_page == 0){
++page;
}
}
}
[...document.querySelectorAll('.js-question-page')].forEach(function(item) {
  item.addEventListener('click', function() {
     id = item.querySelector( '#question_id' ).innerHTML;
 localStorage.setItem("current_question",id);
valued = $("#"+id).offset();

if(typeof valued!== "undefined"){
        $('html, body').animate({
        scrollTop: $("#"+id).offset().top - 100

    }, 2000);

  console.log("in if now");
 localStorage.setItem("current_question",id);
 localStorage.setItem("executed","true");
 console.log( localStorage.getItem("current_question"));

           $("#"+id).css('transition', "box-shadow 0.5s ease-out");
$("#"+id).css('box-shadow',"0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)");
$("#"+id).css('border', "red");
}
else{
 console.log("in else now");
  localStorage.setItem("executed",false);
}







  });
   });
   function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
//changing answer text area to ckeditor

//[...document.querySelectorAll('.answer_class')].forEach(function(item) {
//var id = item.getAttribute("id");
////console.log("#"+id);
//if( language == 'ar'){
//ClassicEditor
//        .create( document.querySelector( "#"+id ), {
//
//				toolbar: {
//					items: [
//						'|',
//						'bold',
//						'italic',
//						'link',
//						'bulletedList',
//						'numberedList',
//						'|',
//						'indent',
//						'outdent',
//						'|',
//						'blockQuote',
//						'undo',
//						'redo'
//					]
//				},
//			language: {
//  ui: 'ar',
//  content: 'ar'
//},
//				licenseKey: '',
////				 contentsLangDirection: 'rtl',
//			} )
//			.then( editor => {
//				window.editor = editor;
//				editor.setData("");
////				editor.setData(setAnswers(id));
//			} )
//			.catch( error => {
//				console.error( 'Oops, something gone wrong!' );
//				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
//				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
//				console.error( error );
//			} );
//}
//else{
//ClassicEditor
//        .create( document.querySelector( "#"+id ), {
//
//				toolbar: {
//					items: [
//						'|',
//						'bold',
//						'italic',
//						'link',
//						'bulletedList',
//						'numberedList',
//						'|',
//						'indent',
//						'outdent',
//						'|',
//						'blockQuote',
//						'undo',
//						'redo'
//					]
//				},
//			language: {
//  ui: 'en',
//  content: 'en'
//},
//				licenseKey: '',
////				 contentsLangDirection: 'rtl',
//			} )
//			.then( editor => {
//				window.editor = editor;
//				editor.setData("");
////				editor.setData(setAnswers(id));
////                getAnswers(editor.getData(),id);
//			} )
//			.catch( error => {
//				console.error( 'Oops, something gone wrong!' );
//				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
//				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
//				console.error( error );
//			} );
//}
//
//});
[...document.querySelectorAll('.answer_class')].forEach(function(item) {
item.addEventListener('change', function() {
var id = item.getAttribute("id");
let my_answers = {};
temp_answers = localStorage.getItem("answers");
if(typeof temp_answers === 'undefined' || temp_answers === null || temp_answers === 'submitted'){
my_answers[`${id}`] = item.value;
localStorage.setItem("answers",JSON.stringify(my_answers));
console.log("first in setting, setted now",localStorage.getItem("answers"));
}
else{
if ( JSON.parse(localStorage.getItem("answers")) == 'submitted'){
my_answers[`${id}`] = item.value;
localStorage.setItem("answers",JSON.stringify(my_answers));
}
else{
my_answers = JSON.parse(localStorage.getItem("answers"));
my_answers[`${id}`] = item.value;
localStorage.setItem("answers",JSON.stringify(my_answers));
}
my_answers[`${id}`] = item.value;
localStorage.setItem("answers",JSON.stringify(my_answers));
console.log("second in setting","answers are:",my_answers.id,"pare: ",my_answers[`${id}`]);
}

//localStorage.setItem("answers", JSON.stringify(answers));
console.log("changed id is: ",id,"data is",answers.id);
console.log("changed now: ",JSON.parse(localStorage.getItem("answers")));
console.log($('#user_id').html());
});
});
[...document.querySelectorAll('.answer_class')].forEach(function(item) {
console.log("setting answers");
var id = item.getAttribute("id");
 item.innerHTML = setAnswers(id);

});
//function getAnswers(id){
//
//}
function setAnswers(id){
let my_answers;
answersss = localStorage.getItem("answers");
if(localStorage.getItem("answers") == "NaN" || localStorage.getItem("answers") == "submitted" ||  answersss == "null"){
return "";

}
else{
console.log("id is: ",id,"answers are:",localStorage.getItem("answers"));
my_answers =  JSON.parse(localStorage.getItem("answers"));
if(typeof my_answers[`${id}`] === "undefined"){
console.log("hero now");
return "";
}
else{

return my_answers[`${id}`];
}
}


}
function examPeriod(exam_period){
let translated_exam_period;
switch(exam_period){
case '10 minutes':
translated_exam_period = 10;
break;
case '15 minutes':
translated_exam_period = 15;
break;
case '30 minutes':
translated_exam_period = 30;
break;
case '1 hour':
translated_exam_period = 60;
break;
case '1:30 hour':
translated_exam_period = 90;
break;
case '2 hours':
translated_exam_period = 120;
break;

}
return translated_exam_period;
}
var exam_period = examPeriod(document.querySelector('#exam-period').innerHTML);
let examTime;
if(localStorage.getItem("current_time") != "NaN"){


if(localStorage.getItem("current_time") == "finished"){
examTime = exam_period;

}
else{
examTime = parseFloat(localStorage.getItem("current_time"))

}

}
else{
examTime = exam_period;

}
//examTime (originally here ))
var time_in_minutes = examTime;
var current_time = Date.parse(new Date());
var deadline = new Date(current_time + time_in_minutes*60*1000);


function time_remaining(endtime){
	var t = Date.parse(endtime) - Date.parse(new Date());
	var seconds = Math.floor( (t/1000) % 60 );
	var minutes = Math.floor( (t/1000/60) % 60 );
	var hours = Math.floor( (t/(1000*60*60)) % 24 );
	var days = Math.floor( t/(1000*60*60*24) );
	return {'total':t, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds};
}
function run_clock(id,endtime){
	var clock = document.getElementById(id);
	function update_clock(){
		var t = time_remaining(endtime);
		if(t.minutes == 1 || t.minutes == 0 ){
  $('#exam-period').css('color','red');
		}
		if(endtime == 60 || endtime > 60){
						clock.innerHTML = t.hours+":"+t.minutes+':'+t.seconds;
						current_time = (t.hours*60)+(t.minutes)+(t.seconds/60);

						 localStorage.setItem("current_time",current_time);

		}
		else{
				clock.innerHTML = t.minutes+':'+t.seconds;
				current_time = (t.minutes)+(t.seconds/60);
						 localStorage.setItem("current_time",current_time);



		}
		if(t.total<=0){ clearInterval(timeinterval);
		localStorage.setItem("current_time","finished");
		localStorage.setItem("send_answers",localStorage.getItem("answers"));
		localStorage.setItem("answers","submitted");
		console.log("now im clock");
		handle_data();


		}
	}
	update_clock(); // run function once at first to avoid delay
	var timeinterval = setInterval(update_clock,1000);
}
run_clock('exam-period',deadline);

function handle_data(){
csrfmiddlewaretoken = $("#parent-div").find("input[name='csrfmiddlewaretoken']" ).val();
    formData = $('#parent-div').serializeArray();
    formData = JSON.stringify(formData);
$.ajax({
        url: $('#parent-div').attr("data-report-url"),
        data: {
        'answers' :  JSON.parse(localStorage.getItem("send_answers")) ,
//        "form_data": JSON.stringify($('#parent-div').serialize()) ,
        "csrfmiddlewaretoken" : csrfmiddlewaretoken,
            'user_id':$('#user_id').html(),
            'exam_id':$('#exam_id').html(),
            'second_answers':JSON.parse(localStorage.getItem("send_answers")),

        } ,
        dataType: 'json',
        success: function (data) {
        window.location = data.url;

        }
        });

}


$("form").submit(function(){
localStorage.setItem("current_time","finished");
});

});
$(window).bind("load", function() {
if ( localStorage.getItem("executed") == "true"){

}
else{

selectedQuestion =  localStorage.getItem("current_question");
    $('html, body').animate({

        scrollTop:  $("#"+selectedQuestion).offset().top - 180

    }, 2000);
$("#"+selectedQuestion).css('transition', "box-shadow 0.5s ease-out");
$("#"+selectedQuestion).css('box-shadow',"0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)");
$("#"+selectedQuestion).css('border', "red");
}





});
