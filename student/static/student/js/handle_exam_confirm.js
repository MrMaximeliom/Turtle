$( document ).ready(function() {
var language = $( "#lang" ).text();
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
handle_timer(examTime);
form = document.querySelector('#confirm-form');
confirm = document.querySelector('#confirm');
form.addEventListener('submit', (event) => {
    localStorage.setItem("last_time",localStorage.getItem("current_time"));
    localStorage.setItem("current_time","finished");
    localStorage.setItem("answers","submitted");
});
//$( "#confirm" ).click(function() {
//    localStorage.setItem("last_time",localStorage.getItem("current_time"));
//    localStorage.setItem("current_time","finished");
//    localStorage.setItem("answers","submitted");
//    console.log("confirmed");
//});


if(language == "ar"){
[...document.querySelectorAll('.js-answer-status')].forEach(function(item) {
if(item.innerHTML == "Answer Saved"){
item.innerHTML = "تم حفظ الإجابة";
}
else{
item.innerHTML = "لم تتم إجابته";
}
});


}


console.log("current_time in exam confirm is:",localStorage.getItem("current_time"));


});