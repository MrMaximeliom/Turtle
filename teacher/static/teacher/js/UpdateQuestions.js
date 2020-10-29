$( document ).ready(function() {
var translations = JSON.parse(document.getElementById('my-translations').textContent);
var questions_of_exam = JSON.parse(document.getElementById('my-questions').textContent);
var counter = 0;
var createCounter = 0;
let questionToBeDeleted;
let questions ;
var parent_div = document.querySelector( '.j-question-form' );
var language = $( "#lang" ).text();
if (questions_of_exam.count > 0 ){

initialCreateQuestions(questions_of_exam.count);

}
$( "#add-questions" ).click( function(){
if(document.querySelector( '#num_questions' ).value != ''){
createQuestions(document.querySelector( '#num_questions' ).value);

}

});
function initialCreateQuestions(num_questions){

//if(createCounter > 0){
//questions = questions_of_exam.count + createCounter;
//}
//else{
//questions = questions_of_exam.count;
//}
var questions = document.querySelectorAll( '#question_text_' );
console.log(questions.length)
    for (i = 0; i < questions.length ; i++) {
var question = document.querySelector( '#question_text_' );
question.setAttribute("id","question_text_"+(counter+1));
question.querySelector( '#question_number_' ).innerHTML = translations.question+"("+(counter+1)+")";
question.querySelector( "#question_number_").setAttribute("id","question_number_"+(counter+1));
question.querySelector( '#remove-question_' ).setAttribute("id","remove-question_"+(counter+1));
question.querySelector( '#remove-question_'+(counter+1) ).innerHTML = translations.remove_question;
//question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-toggle","modal");
//question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-target","#deleteModal");
++counter;
console.log('iam else')
console.log('counter is'+localStorage.getItem("current_counter"))


}

}
function createQuestions(num_questions){
    let controlButtons = document.querySelector("#controlButtons")
    console.log(counter+"in creatoo");
    console.log("counter",localStorage.getItem("lastQuestion"));
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS");
    let questionForm = document.querySelectorAll(".question");
    let formNum = questionForm.length-1;

for (i = 0; i < num_questions; i++) {
formNum++;
totalForms.setAttribute('value', `${formNum+2}`);
var question_original = document.querySelector( '#create_question_text_' );
var question = question_original.cloneNode(true);
question.setAttribute("id","create_question_text_"+(createCounter+1));
question.style.display = 'block';
question.querySelector( '#create_question_number_' ).innerHTML = translations.question+"("+("New Question")+")";
question.querySelector( "#create_question_number_").setAttribute("id","create_question_number_"+(createCounter+1));
question.querySelector( "#id_form-0-question_degree").setAttribute("id","id_form-"+(createCounter+1)+"-question_degree");
question.querySelector( "#id_form-"+(createCounter+1)+"-question_degree").value = "";
question.querySelector( "#id_form-"+(createCounter+1)+"-question_degree").setAttribute("name","form-"+(createCounter+1)+"-question_degree");
question.querySelector( '#create-remove-question_' ).setAttribute("id","create-remove-question_"+(createCounter+1));
question.querySelector( '#create-remove-question_'+(createCounter+1) ).innerHTML = translations.remove_question;
question.querySelector( '#create-remove-question_'+(createCounter+1) ).setAttribute("data-toggle","modal");
question.querySelector( '#create-remove-question_'+(createCounter+1) ).setAttribute("data-target","#deleteModal");
question.querySelector( '#id_form-0-question_text' ).setAttribute("id","id_form-"+(createCounter+1)+"-question_text");
question.querySelector( "#id_form-"+(createCounter+1)+"-question_text" ).value="";
question.querySelector( "#id_form-"+(createCounter+1)+"-question_text" ).setAttribute("name","form-"+(createCounter+1)+"-question_text");
question.querySelector( '#id_form-0-question_optimal_answer' ).setAttribute("id","id_form-"+(createCounter+1)+"-question_optimal_answer");
question.querySelector( "#id_form-"+(createCounter+1)+"-question_optimal_answer" ).value="";
question.querySelector( "#id_form-"+(createCounter+1)+"-question_optimal_answer" ).setAttribute("name","form-"+(createCounter+1)+"-question_optimal_answer")
controlButtons.before(question);
++createCounter;

}
questions = questions_of_exam.count + num_questions;
}
$(document).on('focus', ".question_class", function() {
var id = $(this).attr("id");
//console.log("#"+id);
if( language == 'ar'){
ClassicEditor
        .create( document.querySelector( "#"+id ), {

				toolbar: {
					items: [
						'|',
						'bold',
						'italic',
						'link',
						'bulletedList',
						'numberedList',
						'|',
						'indent',
						'outdent',
						'|',
						'blockQuote',
						'undo',
						'redo'
					]
				},
			language: {
  ui: 'ar',
  content: 'ar'
},
				licenseKey: '',
//				 contentsLangDirection: 'rtl',
			} )
			.then( editor => {
				window.editor = editor;
//				editorQuestions[id]
				abc = editor.getData();
			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
}
else{
ClassicEditor
        .create( document.querySelector("#"+id ), {

				toolbar: {
					items: [
						'|',
						'bold',
						'italic',
						'link',
						'bulletedList',
						'numberedList',
						'|',
						'indent',
						'outdent',
						'|',
						'blockQuote',
						'undo',
						'redo'
					]
				},
			language: {
  ui: 'en',
  content: 'en'
},
				licenseKey: '',
//				 contentsLangDirection: 'rtl',
			} )
			.then( editor => {
				window.editor = editor;
//				editorQuestions[id]
				abc = editor.getData();
			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
}
console.log(id);
});
$(document).on('focus', ".answer_class", function() {
var id = $(this).attr("id");
//console.log("#"+id);
if( language == 'ar'){
ClassicEditor
        .create( document.querySelector( "#"+id ), {

				toolbar: {
					items: [
						'|',
						'bold',
						'italic',
						'link',
						'bulletedList',
						'numberedList',
						'|',
						'indent',
						'outdent',
						'|',
						'blockQuote',
						'undo',
						'redo'
					]
				},
			language: {
  ui: 'ar',
  content: 'ar'
},
				licenseKey: '',
//				 contentsLangDirection: 'rtl',
			} )
			.then( editor => {
				window.editor = editor;
//				editorAnswers[id] = editor.getData();
			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
}
else{
ClassicEditor
        .create( document.querySelector( "#"+id ), {

				toolbar: {
					items: [
						'|',
						'bold',
						'italic',
						'link',
						'bulletedList',
						'numberedList',
						'|',
						'indent',
						'outdent',
						'|',
						'blockQuote',
						'undo',
						'redo'
					]
				},
			language: {
  ui: 'en',
  content: 'en'
},
				licenseKey: '',
//				 contentsLangDirection: 'rtl',
			} )
			.then( editor => {
				window.editor = editor;
//				editorAnswers[id] = editor.getData();
			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
}

});
$(document).on('click', '.raw-button , .remove-question', function() {
questionToBeDeleted = $(this).attr("id");
console.log('hi');
});
$(document).on('click', '#remove_question_modal', function() {
var button = document.getElementById(questionToBeDeleted);
var element = document.getElementById( button.parentNode.getAttribute('id') );

parent_div.removeChild(element);

});

});