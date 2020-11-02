$( document ).ready(function() {
var attempt_period = document.querySelector("#attempt_period");
last_time =  localStorage.getItem("last_time");
exam_period = localStorage.getItem('exam_period');
attempt_period.innerHTML = handleAttemptPeriod(last_time);
function handleAttemptPeriod(last_time){
let attempt_period_time;
if(last_time == "undefined" || last_time == null || last_time == "finished"){
attempt_period_time = exam_period;
console.log("here in if");
console.log("last time: ",last_time);
}
else{
attempt_period_time = exam_period - last_time;
console.log("here in else");
console.log("exam period",exam_period,"last time",last_time);

}
return Math.round(attempt_period_time);
}
localStorage.setItem("current_time","finished");
console.log("current_time in exam final report is:",localStorage.getItem("current_time"));

});