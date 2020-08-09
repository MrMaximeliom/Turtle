$( document ).ready(function() {
  var translations = JSON.parse(document.getElementById('my-translations').textContent);
var counter = 1;
var limit = 3;
let questionToBeDeleted;
var editorQuestions = {};
editorQuestions["myVarProperty"+1] = 5;
var parent_div = document.querySelector( '#parent-div' );
let theEditor;
     ClassicEditor
        .create( document.querySelector( '#question_1' ), {

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
				language: 'en',
				licenseKey: '',

			} )
			.then( editor => {
				window.editor = editor;
				editorQuestions["question"+(1)] = editor; // Save for later use.




			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
//			editor_question.setAttribute("id","TestId");

		  	ClassicEditor
        .create( document.querySelector( '#optimal_1' ), {

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
				language: 'en',
				licenseKey: '',

			} )
			.then( editor => {
				window.editor = editor;
				editorQuestions["answer"+(1)] = editor;




			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );

function createTextArea(counter,textAreaType){
if(textAreaType == "question"){
 var form_textarea_question = document.createElement('textarea');
  form_textarea_question.setAttribute("placeholder", "question here");
  form_textarea_question.setAttribute("id", "question"+(counter+1))
  return form_textarea_question;
}
else{
  var form_textarea_answer = document.createElement('textarea');
  form_textarea_answer.setAttribute("placeholder", "optimal answer here");
  form_textarea_answer.setAttribute("cols", "20");
  form_textarea_answer.setAttribute("id", "optimal"+(counter+1));
  return form_textarea_answer;

}
}
function rebuildCkeditor(question_data,answer_data){
 ClassicEditor
        .create( document.querySelector( '#question1' ), {

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
				language: 'en',
				licenseKey: '',

			} )
			.then( editor => {
				window.editor = editor;
				editorQuestions["question"+(1)] = editor; // Save for later use.
				editor.setData( question_data);




			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
//			editor_question.setAttribute("id","TestId");

		  	ClassicEditor
        .create( document.querySelector( '#optimal1' ), {

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
				language: 'en',
				licenseKey: '',

			} )
			.then( editor => {
				window.editor = editor;
				editorQuestions["answer"+(1)] = editor;
				editor.setData( answer_data);




			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );

}
$( "#add-questions" ).click(function() {
  var num_questions = document.querySelector( '#num_questions' ).value;
for (i = 0; i < num_questions; i++) {
var question_original = document.querySelector( '#question_text_' );
var question = question_original.cloneNode(true);
question.setAttribute("id","question_text_"+(counter+1));
question.style.display = 'block';
question.querySelector( '#question_number_' ).innerHTML = translations.question+"("+(counter+1)+")";
question.querySelector( "#question_number_").setAttribute("id","question_number_"+(counter+1));
question.querySelector( "#question_degree_").setAttribute("id","question_degree_"+(counter+1));
question.querySelector( "#question_degree_"+(counter+1)).value = "";
question.querySelector( '#remove-question_' ).setAttribute("id","remove-question_"+(counter+1));
question.querySelector( '#remove-question_'+(counter+1) ).innerHTML = translations.remove_question;
question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-toggle","modal");
question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-target","#deleteModal");
question.querySelector( '#question_' ).setAttribute("id","question_"+(counter+1));
question.querySelector( '#optimal_' ).setAttribute("id","optimal_"+(counter+1));
parent_div.appendChild(question);
++counter
}
});
$(document).on('click', '.question_class,.answer_class', function() {
var id = $(this).attr("id");
console.log("#"+id);
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
				language: 'en',
				licenseKey: '',
			} )
			.then( editor => {
				window.editor = editor;
				editorQuestions[id] = editor;
			} )
			.catch( error => {
				console.error( 'Oops, something gone wrong!' );
				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
				console.error( error );
			} );
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