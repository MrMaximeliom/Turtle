//  ClassicEditor
//                                .create( document.querySelector( '#optimal1' ) )
//                          .catch( error => {
//            console.error( error );
//        } );
//element.parentNode.removeChild(element);
function createQuestionDiv(counter,div_type){
if (div_type == "question"){
 var question = document.createElement('div');
 question.innerHtml = "dg";
 question.classList.add("question");
 question.setAttribute("id", "question_text"+(counter+1));
 question.classList.add("question");
 return question;
 }
 else
{
var question_title = document.createElement('div');
 question_title.classList.add("border-bottom-question");
 question_title.classList.add("mb-3");
 return question_title;
}

}
function createRowGroupDiv(row_type){
if(row_type == "form_row"){
var form_row = document.createElement('div');
form_row.classList.add("form-row");
return form_row;
}
else if(row_type == "form_row_question"){
  var form_row_question = document.createElement('div');
  form_row_question.classList.add("form-row");
  form_row_question.classList.add("fit-border-bottom");
  return form_row_question;
}
else if(row_type == "form_group_question_answer"){
  var form_group_question_answer = document.createElement('div');
  form_group_question_answer.classList.add("form-group");
  form_group_question_answer.classList.add("col-md-6");
  return form_group_question_answer;

}
else{
  var form_group = document.createElement('div');
  form_group.classList.add("form-group");
  form_group.classList.add("col-md-4");
  return form_group;

}
}
function createSpan(counter){
var question_title_text = document.createElement('span');
question_title_text.innerHTML = "Question ("+(counter+1) +")";
return question_title_text;
}
function createRemoveQuestionButton(counter){
  var remove_question = document.createElement('button');
  remove_question.classList.add("raw-button");
  remove_question.classList.add("remove-question");
  remove_question.setAttribute("id", "remove-question"+(counter+1));
  remove_question.innerHTML = translations.remove_question
  return remove_question;
}
function createInput(){
  var form_input = document.createElement('input');
  form_input.setAttribute("type", "number");
  form_input.setAttribute("min", "1");
  form_input.setAttribute("max", "100");
  form_input.setAttribute("placeholder", "question full degree");
  return form_input;
}
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
function createQuestion(counter){

// create question section
var question = createQuestionDiv(counter,"question");
parent_div.appendChild(question);
var question_title = createQuestionDiv(counter,"question_title");
var question_title_text = createSpan(counter);
var remove_question = createRemoveQuestionButton(counter);
question.appendChild(question_title);
question.appendChild(remove_question);
question_title.appendChild(question_title_text);
// create degree section
var form_row_degree = createRowGroupDiv("form_row");
var form_input_degree = createInput();
var form_group_degree = createRowGroupDiv("form_group");
question.appendChild(form_row_degree);
form_row_degree.appendChild(form_group_degree);
form_group_degree.appendChild(form_input_degree);
// create question_answer section
var form_row_question = createRowGroupDiv("form_row_question");
question.appendChild(form_row_question);
var form_group_question = createRowGroupDiv("form_group_question_answer");
var form_textarea_question = createTextArea(counter,"question");
var form_group_answer =  createRowGroupDiv("form_group_question_answer");
var form_textarea_answer = createTextArea(counter,"answer");
form_row_question.appendChild(form_group_question);
form_row_question.appendChild(form_group_answer);
form_group_question.appendChild(form_textarea_question);
form_group_answer.appendChild(form_textarea_answer);

}
//  var question = document.createElement('div');
//  question.classList.add("question");
//  question.setAttribute("id", "question_text"+(counter+1));
//  parent_div.appendChild(question);
//  question.classList.add("question");
//  var question_title = document.createElement('div');
//  question_title.classList.add("border-bottom-question");
//  question_title.classList.add("mb-3");
//  var question_title_text = document.createElement('span');
//  var remove_question = document.createElement('button');
//  remove_question.classList.add("raw-button");
//  remove_question.classList.add("remove-question");
//  remove_question.setAttribute("id", "remove-question"+(counter+1));
//  remove_question.innerHTML = translations.remove_question
//  question_title_text.innerHTML = "Question ("+(counter+1) +")"
//  question.appendChild(question_title);
//  question.appendChild(remove_question);
//  question_title.appendChild(question_title_text);
//  //////////////////////////////////////////////////////
//  var form_row_degree = document.createElement('div');
//  question.appendChild(form_row_degree);
//  form_row_degree.classList.add("form-row");
//  var form_group_degree = document.createElement('div');
//  form_group_degree.classList.add("form-group");
//  form_group_degree.classList.add("col-md-4");
//  var form_input_degree = document.createElement('input');
//  form_input_degree.setAttribute("type", "number");
//  form_input_degree.setAttribute("min", "1");
//  form_input_degree.setAttribute("max", "100");
//  form_input_degree.setAttribute("placeholder", "question full degree");
//  form_row_degree.appendChild(form_group_degree);
//  form_group_degree.appendChild(form_input_degree);
//  //////////////////////////////////////////////////////////
//  var form_row_question = document.createElement('div');
//  question.appendChild(form_row_question);
//  form_row_question.classList.add("form-row");
//  form_row_question.classList.add("fit-border-bottom");
//  var form_group_question = document.createElement('div');
//  form_group_question.classList.add("form-group");
//  form_group_question.classList.add("col-md-6");
//  var form_textarea_question = document.createElement('textarea');
//  form_textarea_question.setAttribute("placeholder", "question here");
//  form_textarea_question.setAttribute("id", "question"+(counter+1));
//  var form_group_answer = document.createElement('div');
//  form_group_answer.classList.add("form-group");
//  form_group_answer.classList.add("col-md-6");
//  var form_textarea_answer = document.createElement('textarea');
//  form_textarea_answer.setAttribute("placeholder", "optimal answer here");
//  form_textarea_answer.setAttribute("cols", "20");
//  form_textarea_answer.setAttribute("id", "optimal"+(counter+1));
//  form_row_question.appendChild(form_group_question);
//  form_row_question.appendChild(form_group_answer);
//  form_group_question.appendChild(form_textarea_question);
//  form_group_answer.appendChild(form_textarea_answer);
  ///////////////////////////////////////////////////////
//  ClassicEditor
//                                .create( document.querySelector( '#question'+(counter+1) ) )
//                                .catch( error => {
//            console.error( error );
//        } );



//ClassicEditor
//        .create( document.querySelector( '#question'+(counter+1) ), {
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
//				language: 'en',
//				licenseKey: '',
//
//			} )
//			.then( editor => {
//				window.editor = editor;
//
//
//
//
//			} )
//			.catch( error => {
//				console.error( 'Oops, something gone wrong!' );
//				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
//				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
//				console.error( error );
//			} );
//			ClassicEditor
//        .create( document.querySelector( '#optimal'+(counter+1) ), {
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
//				language: 'en',
//				licenseKey: '',
//
//			} )
//			.then( editor => {
//				window.editor = editor;
//
//
//
//
//			} )
//			.catch( error => {
//				console.error( 'Oops, something gone wrong!' );
//				console.error( 'Please, report the following error in the https://github.com/ckeditor/ckeditor5 with the build id and the error stack trace:' );
//				console.warn( 'Build id: 3oic26nlqaps-l580ifb6a79x' );
//				console.error( error );
//			} );
