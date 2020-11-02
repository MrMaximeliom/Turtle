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

//examTime (originally here ))
function handle_timer(examTime){
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
		form = document.querySelector('#confirm-form');
		form.submit();
		// direct to exam report page
//		 window.location = data.url;
	    // make page submitting


		}
	}
	update_clock(); // run function once at first to avoid delay
	var timeinterval = setInterval(update_clock,1000);
}
run_clock('exam-period',deadline);
}