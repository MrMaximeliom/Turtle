//$( document ).ready(function() {
function examStatus(exam_status){
let translated_exam_status;
switch(exam_status){
case 'Active':
translated_exam_status = 'نشط';
break;
case 'Expired':
translated_exam_status = 'منتهي' ;
break;
}
return translated_exam_status;

}

function examPeriod(exam_period){
let translated_exam_period;
switch(exam_period){
case '10 minutes':
translated_exam_period = '10 دقائق';
break;
case '15 minutes':
translated_exam_period = '15 دقيقة';
break;
case '30 minutes':
translated_exam_period = '30 دقيقة';
break;
case '1 hour':
translated_exam_period = '1 ساعة';
break;
case '1:30 hour':
translated_exam_period = '1:30 ساعة';
break;
case '2 hours':
translated_exam_period = 'ساعتين';
break;
}
return translated_exam_period;
}
var language = $( "#lang" ).text();
var card_exam_status = document.querySelectorAll( '.card_exam_status' );
var exam_status_label = document.querySelectorAll( '.exam_status' );
var exam_period = document.querySelectorAll( '.exam-period' );
var exam_status_icon = document.querySelectorAll( '.exam_status_icon' );
if(language == "ar"){
$("h1",".col-md-4").css('direction','rtl');
$(".exam_notes").css('direction','rtl');
$(".col-md-4").css('text-align','right');
$("article").css('direction','rtl');
$("article").css('text-align','right');
$(".article-img").css('margin-left','16px');
$("#searchForm").css('direction','rtl');
$("#searchForm").css('margin-right','200px');
for(var i = 0; i < card_exam_status.length; i++) {
card_exam_status[i].style.direction = 'rtl'

}
for(var i = 0; i < exam_status_label.length; i++) {
status = examStatus(exam_status_label[i].innerHTML);
exam_status_label[i].innerHTML = status;

}
for(var i = 0; i < exam_period.length; i++) {
status = examPeriod(exam_period[i].innerHTML);
exam_period[i].innerHTML = status;
}
for(var i = 0; i < exam_status_label.length; i++) {
console.log(exam_status_label[i].innerHTML)
if (exam_status_label[i].innerHTML == 'منتهي'){
exam_status_icon[i].innerHTML = '<i class="fas fa-hourglass-end" style="color: red;"></i>'

}
else{
exam_status_icon[i].innerHTML = '<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 128 128" style="width: 19px;"><defs><style>.cls-1{fill:#67c40a;}</style></defs><title>Done</title><g id="Done"><path class="cls-1" d="M85.17,46.61l4.22,4.22L56,84.21,38.61,66.83l4.22-4.22L55.28,75.06a1,1,0,0,0,1.44,0Z"/><path class="cls-1" d="M64,19a45,45,0,1,0,45,45A45,45,0,0,0,64,19ZM91.55,51.55C54.39,88.71,56.65,86.68,56,86.68s1,1.37-19.55-19.13a1,1,0,0,1,0-1.44l5.66-5.66a1.05,1.05,0,0,1,1.44,0L56,72.9,84.45,44.45a1.05,1.05,0,0,1,1.44,0l5.66,5.66A1,1,0,0,1,91.55,51.55Z"/><path class="cls-1" d="M127,64c0-5.44-5.14-10.13-6.48-15.15-1.39-5.19.68-11.81-2-16.36s-9.46-6.11-13.2-9.86-5.25-10.53-9.86-13.2S84.34,8.87,79.15,7.48C74.13,6.14,69.44,1,64,1S53.87,6.14,48.85,7.48C43.66,8.87,37,6.8,32.49,9.43s-6.11,9.46-9.86,13.2S12.1,27.88,9.43,32.49,8.87,43.66,7.48,48.85C6.14,53.87,1,58.56,1,64S6.14,74.13,7.48,79.15C8.87,84.34,6.8,91,9.43,95.51s9.46,6.11,13.2,9.86,5.25,10.53,9.86,13.2,11.17.56,16.36,2c5,1.34,9.71,6.48,15.15,6.48s10.13-5.14,15.15-6.48c5.19-1.39,11.81.68,16.36-2s6.11-9.46,9.86-13.2,10.53-5.25,13.2-9.86.56-11.17,2-16.36C121.86,74.13,127,69.44,127,64ZM64,111a47,47,0,1,1,47-47A47.07,47.07,0,0,1,64,111Z"/></g></svg>'

}
}

}


else{
for(var i = 0; i < exam_status_label.length; i++) {
if (exam_status_label[i].innerHTML == 'Expired'){
exam_status_icon[i].innerHTML = '<i class="fas fa-hourglass-end" style="color: red;"></i>'

}
else{
exam_status_icon[i].innerHTML = '<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 128 128" style="width: 19px;"><defs><style>.cls-1{fill:#67c40a;}</style></defs><title>Done</title><g id="Done"><path class="cls-1" d="M85.17,46.61l4.22,4.22L56,84.21,38.61,66.83l4.22-4.22L55.28,75.06a1,1,0,0,0,1.44,0Z"/><path class="cls-1" d="M64,19a45,45,0,1,0,45,45A45,45,0,0,0,64,19ZM91.55,51.55C54.39,88.71,56.65,86.68,56,86.68s1,1.37-19.55-19.13a1,1,0,0,1,0-1.44l5.66-5.66a1.05,1.05,0,0,1,1.44,0L56,72.9,84.45,44.45a1.05,1.05,0,0,1,1.44,0l5.66,5.66A1,1,0,0,1,91.55,51.55Z"/><path class="cls-1" d="M127,64c0-5.44-5.14-10.13-6.48-15.15-1.39-5.19.68-11.81-2-16.36s-9.46-6.11-13.2-9.86-5.25-10.53-9.86-13.2S84.34,8.87,79.15,7.48C74.13,6.14,69.44,1,64,1S53.87,6.14,48.85,7.48C43.66,8.87,37,6.8,32.49,9.43s-6.11,9.46-9.86,13.2S12.1,27.88,9.43,32.49,8.87,43.66,7.48,48.85C6.14,53.87,1,58.56,1,64S6.14,74.13,7.48,79.15C8.87,84.34,6.8,91,9.43,95.51s9.46,6.11,13.2,9.86,5.25,10.53,9.86,13.2,11.17.56,16.36,2c5,1.34,9.71,6.48,15.15,6.48s10.13-5.14,15.15-6.48c5.19-1.39,11.81.68,16.36-2s6.11-9.46,9.86-13.2,10.53-5.25,13.2-9.86.56-11.17,2-16.36C121.86,74.13,127,69.44,127,64ZM64,111a47,47,0,1,1,47-47A47.07,47.07,0,0,1,64,111Z"/></g></svg>'

}

}

}






