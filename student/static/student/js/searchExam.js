for(var i = 0; i < exam_card.length; i++) {
exam_date = exam_card[i].querySelector('.exam_date').innerHTML;
exam_start_btn =  exam_card[i].querySelector('.update-exam-button');
if(exam_date == today)
{
exam_start_btn.style.cursor = 'pointer';
}
else{
exam_start_btn.style.cursor = 'not-allowed';
$(exam_start_btn).hover(function(){
  $(this).css("background-color", "white");
  $(this).css("color", "#E77B73");
  }, function(){
  $(this).css("background-color", "white");
   $(this).css("color", "#E77B73");
});
console.log('ht')

}

}