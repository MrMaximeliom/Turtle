$( document ).ready(function() {
var translations = JSON.parse(document.getElementById('my-translations').textContent);
var questions_of_exam = JSON.parse(document.getElementById('my-questions').textContent);
var counter = 0;
var language = $( "#lang" ).text();
if (questions_of_exam.count > 0 ){
createQuestions(questions_of_exam.count);

}
else{
createQuestions(1);
}
let questionToBeDeleted;
var parent_div = document.querySelector( '#parent-div' );
$( "#add-questions" ).click( function(){
createQuestions(document.querySelector( '#num_questions' ).value);
});
function createQuestions(num_questions){
        let controlButtons = document.querySelector("#controlButtons")
//  console.log(document.querySelector( '#num_questions' ).value);
var parent_div = document.querySelector( '#parent-div' );
    let questionForm = document.querySelectorAll(".j-question-form")
        let container = document.querySelector(".question-form")
        let addButton = document.querySelector("#add-questions")
        let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
        let formNum = questionForm.length-1




  for (i = 0; i < num_questions; i++) {
   let formRegex = RegExp(`form-(\d){1}-`,'g')
        formNum++
        totalForms.setAttribute('value', `${formNum+2}`)
var question_original = document.querySelector( '#question_text_' );
var question = question_original.cloneNode(true);
question.setAttribute("id","question_text_"+(counter+1));
question.style.display = 'block';
question.querySelector( '#question_number_' ).innerHTML = translations.question+"("+(counter+1)+")";
question.querySelector( "#question_number_").setAttribute("id","question_number_"+(counter+1));
question.querySelector( "#id_form-0-question_degree").setAttribute("id","id_form-"+(counter+1)+"-question_degree");
question.querySelector( "#id_form-"+(counter+1)+"-question_degree").value = "";
question.querySelector( "#id_form-"+(counter+1)+"-question_degree").setAttribute("name","form-"+(counter+1)+"-question_degree");
question.querySelector( '#remove-question_' ).setAttribute("id","remove-question_"+(counter+1));
question.querySelector( '#remove-question_'+(counter+1) ).innerHTML = translations.remove_question;
question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-toggle","modal");
question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-target","#deleteModal");
question.querySelector( '#id_form-0-question_text' ).setAttribute("id","id_form-"+(counter+1)+"-question_text");
question.querySelector( "#id_form-"+(counter+1)+"-question_text" ).value="";
question.querySelector( "#id_form-"+(counter+1)+"-question_text" ).setAttribute("name","form-"+(counter+1)+"-question_text");
question.querySelector( '#id_form-0-question_optimal_answer' ).setAttribute("id","id_form-"+(counter+1)+"-question_optimal_answer");
question.querySelector( "#id_form-"+(counter+1)+"-question_optimal_answer" ).value="";
question.querySelector( "#id_form-"+(counter+1)+"-question_optimal_answer" ).setAttribute("name","form-"+(counter+1)+"-question_optimal_answer")
//parent_div.appendChild(question);
controlButtons.before(question);
//parent_div.after(question,questionForm)
++counter
}
//var controlButtons_original = document.querySelector( '#controlButtons' );
//var controlButtons = controlButtons_original.cloneNode(true);
//parent_div.appendChild(controlButtons);
//controlButtons.style.display = 'block';
  }
$(document).on('click', ".question_class", function() {
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
$(document).on('click', ".answer_class", function() {
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
});
$(document).on('click', '#remove_question_modal', function() {
var button = document.getElementById(questionToBeDeleted);
var element = document.getElementById( button.parentNode.getAttribute('id') );
if(button.parentNode.getAttribute('id') == "question_text1"){
button.parentNode.css('display','none');
}
else{
parent_div.removeChild(element);
}
});


});