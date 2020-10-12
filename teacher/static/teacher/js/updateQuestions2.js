$( document ).ready(function() {
var translations = JSON.parse(document.getElementById('my-translations').textContent);
var questions_of_exam = JSON.parse(document.getElementById('my-questions').textContent);
var counter = 0;
let questionToBeDeleted;
var parent_div = document.querySelector( '.j-question-form' );
var language = $( "#lang" ).text();
for (i = 0; i < questions_of_exam.count; i++) {
var question = document.querySelector( '#question_text_' );
question.setAttribute("id","question_text_"+(counter+1));
question.querySelector( '#question_number_' ).innerHTML = translations.question+"("+(counter+1)+")";
question.querySelector( "#question_number_").setAttribute("id","question_number_"+(counter+1));
//question.querySelector( '#remove-question_' ).setAttribute("id","remove-question_"+(counter+1));
//question.querySelector( '#remove-question_'+(counter+1) ).innerHTML = translations.remove_question;
//question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-toggle","modal");
//question.querySelector( '#remove-question_'+(counter+1) ).setAttribute("data-target","#deleteModal");
++counter;

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